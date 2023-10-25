#!/usr/bin/env python

from hashlib import sha256
import string
from Crypto.Cipher import AES
import base64

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

password = "gBv#3%DXMV*7oCN2M71Zfe0QY^dS3ji7DgHxx2bNRCSoRPlVRRX*bwLO5eM&0AIOa&#$@u"

FLAG = "tnP+MdNjHF1aMJVV/ciAYqQutsU8LyxVkJtVEf0J0T5j8Eu68AxcsKwd0NjY9CE+Be9e9FwSVF2xbK1GP53WSAaJuQaX/NC02D+v7S/yizQ="

master = 0x0

test_print = ''

for char in password[::-1]: # this is to count the bits in reverse order
    c = ord(char)
    if char in ALPHABET[:len(ALPHABET)//2]:
        master+=1
        test_print+='1'
    else:
        test_print+='0'
    master<<=1

master>>=1  # this is to offset the additional extra shift that happens after reading the last bit
    
# master = 615817791220577480775
# test_print = 100001 01100010 00110000 01001010 01011111 01100100 00110000 00110000 01000111

byte_order = 'little'

b64decoded_flag = base64.b64decode(FLAG)
MASTER_KEY_reconstructed = master.to_bytes(9, byte_order)

encryption_key = sha256(MASTER_KEY_reconstructed).digest()
cipher = AES.new(encryption_key, AES.MODE_ECB)

try:
    print("the correct byte len is {9}")
    plaintext = cipher.decrypt(b64decoded_flag)
    print(bytearray(plaintext).decode('ascii'))

except:
    print("didn't work")


#for i in range(16, 7, -1):
#
#   MASTER_KEY_reconstructed = master.to_bytes(i, byte_order)
#
#    encryption_key = sha256(MASTER_KEY_reconstructed).digest()
#    cipher = AES.new(encryption_key, AES.MODE_ECB)
#
#    try:
#        print(f"the correct byte len is {i}")
#        plaintext = cipher.decrypt(b64decoded_flag)
#        print(bytearray(plaintext).decode('ascii'))
#    except:
#        print("didn't work")

# flag: HTB{00ps___n0t_th4t_h4rd_t0_r3c0v3r_th3_m4st3r_k3y_0f_my_p4ssw0rd_g3n3r4t0r}
