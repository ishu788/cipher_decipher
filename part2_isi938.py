#!/usr/bin/python

import os
import pyfiglet
from modules import ceaser_cipher_isi938 as c

cmd1 = 'figlet -f slant -c  "Assign3 part2: Ceaser cipher"'
cmd2 = 'figlet -f smbraille -c "by Ishwinder 3003519348"'





figlet1 = os.popen(cmd1).read()
figlet2 = os.popen(cmd2).read()
print(figlet1)
print(figlet2)



rotation = int(input("Enter the number of rotations: "))
filename = input("Enter the filename: ")
cipher_value = 1


valid_option = False
while not valid_option:
    option = input("Do you want to 1) cipher or 2) decipher")
    if option == '1' or option == '2':
        if option == 1 :
            rotation = rotation %26
     
        elif option == 2:
            rotation  = (26-rotation) %26
        
        valid_option = True


valid_File = False
while not valid_File:
    try:
        with open(filename, 'r') as file:
            valid_File = True
            lines = file.readlines()
    except FileNotFoundError:
        print('{filename} not found')
    break




if option == '1':
    cipher_value = 1
elif option == '2':
    cipher_value = -1


cipher_var = []
for line in lines:
    cipher_line = c.cipher(line.strip(), rotation, cipher_value)
    cipher_var.append(cipher_line)

ciphertext = '\n'.join(cipher_var)




print("Ciphered/Deciphered text:")
print(ciphertext)


output_filename = 'output_part2_isi938.txt'
with open(output_filename, 'w') as file:
    file.write(ciphertext)

print("Output saved to {0}".format(output_filename))
