import pickle
import os
import subprocess
import struct
import time



try:
    subprocess.run(["nasm", "boot.asm -o boot.bin"])
    os.system("gcc -nostdlib -masm=intel code.c")
    subprocess.run(["objcopy", "a.exe -O binary"])
except BaseException as e:
    print(str(e))

boot = []

with open('boot.bin', 'br') as of1, open('disc.bin', 'bw') as of2:
    boot = of1.read()  
    of2.write(boot)

print(len(boot))

with open('disc.bin', 'ba') as file:
    for i in range(len(boot),510):
        file.write(struct.pack('b',0))
    file.write(struct.pack('B',85))
    file.write(struct.pack('B',170))

with open('disc.bin', 'ba') as binary, open('a.exe', 'br') as code:
    boot = code.read()
    boot = boot[1:]
    binary.write(boot)

subprocess.run(["qemu-system-i386", "disc.bin"])
        

    

