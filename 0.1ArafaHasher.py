#!/usr/bin/python3

import hashlib

print("\n","\t"*5,"===>    Simple Hasher    <===","\n"),print("\t"*4,"By : Abd Almoen Arafa (0.1Arafa)"),print("\t"*4,"Age : 15\n"),print("\t"*2,"#"*75,"\n")
hashvalue=input("[*] Enter a string to hash: ")

hashobj1=hashlib.md5()
hashobj1.update(hashvalue.encode())
print("\nmd5   : ",hashobj1.hexdigest())

hashobj2=hashlib.sha1()
hashobj2.update(hashvalue.encode())
print("sha1  : ",hashobj2.hexdigest())

hashobj3=hashlib.sha224()
hashobj3.update(hashvalue.encode())
print("sha224: ",hashobj3.hexdigest())

hashobj4=hashlib.sha256()
hashobj4.update(hashvalue.encode())
print("sha256: ",hashobj4.hexdigest())

hashobj5=hashlib.sha512()
hashobj5.update(hashvalue.encode())
print("sha512: ",hashobj5.hexdigest())

print("\n","\t"*2,"#"*75,"\n")
#By : Abd Almoen Arafa (0.1Arafa)
#Age : 15
