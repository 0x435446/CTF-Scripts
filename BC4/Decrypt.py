#By 0x435446/MeHigh
from Crypto.Util.number import bytes_to_long
def countTotalBits(num): 
      
     # convert number into it's binary and  
     # remove first two characters 0b. 
     binary = bin(num)[2:] 
     print(len(binary))  

L=2339817165
R=314527490
P=3525886283
dec=[]
ciphertext='e19bde665dd62d3c9a1c3001dc523a07fab5c8c15ff2c0eab482e3a37d6389dfa0b458cae535b841f24d8a2ae7361b1d16abd2031367c3bdfa7be21250361cc5d23c3803ee95b4342794fb749645e2'
for i in range(len(ciphertext)/8):
 #print str(i)+"/"+str(len(ciphertext)/8)
 cipher=ciphertext[(i*8):][:8]
 filepath = 'combinations'
 new_L=(5*L + 11)%P
 new_R=(7*R + 19)%P
 Z=new_L^new_R
 with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line=line[:-1]
       enc=bytes_to_long(line)
       enc=str(hex(enc^Z))[2:][:-1]
       if(enc==cipher):
         dec.append(line)
         L=new_L
         R=new_R
         break
       line = fp.readline()
       cnt += 1
print "this"+''.join(dec)+"gth"
