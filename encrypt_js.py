a = input(' -> ')
b = ''
c = ''
#for i in a:
#    c = ord(i)+10


pc=0    
for i in a:
    b += chr((ord(i)+107+pc-32)%95+32)
    pc=(ord(i)+107+pc)%95

pc=0
for i in b :
    dc= (ord(i)-107-pc+95-32)%95
    c += chr(dc+32)
    pc=ord(i)

#for i in b :
 #   a += chr(ord(i)-10)
    
import base64
    
print (b)
print(c)