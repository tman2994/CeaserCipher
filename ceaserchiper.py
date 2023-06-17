import os
import sys


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

'''if direction != 'encode' or direction != 'decode':
            print('you did not type cleaarly if you wanted to encode or decode')
            sys.stdout.flush()
            os.execl(sys.executable, 'python', 'ceaserchiper.py')'''

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26 

def ceaserchiper( encode_or_decode, plain_text, Shift_amount):
        cipher_text = ''
        print(cipher_text)
        if encode_or_decode == 'encode':
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position + Shift_amount
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                else:
                    cipher_text += letter
            print(f'this is the cihper: {cipher_text}')
        elif encode_or_decode== 'decode':
            cipher_text = ''
            for letter in plain_text:
                if letter in alphabet: 
                    position = alphabet.index(letter)
                    new_position = position - Shift_amount
                    cipher_text += alphabet[new_position]
                else:
                    cipher_text += letter
            print(f'this is the cihper: {cipher_text}')
       

        #return 

ceaserchiper(encode_or_decode= direction, plain_text=text, Shift_amount= shift)

def restart():
    restart_cipher = input("press yes to restart cypher, or anyother import to exit: ".lower())
    if restart_cipher == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaserchiper(encode_or_decode= direction, plain_text=text, Shift_amount= shift)
    else: 
        exit

restart()



