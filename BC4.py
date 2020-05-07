import random
import math 
from Crypto.Util.number import long_to_bytes,bytes_to_long

plaintext="this will be"
first_block=plaintext[:4]
Z1='99c989cf' #this xor eda1e0bc
Z1=int(Z1,16) 
Z2='c1ecb70a' # wil xor e19bde66
Z2=int(Z2,16)
Z3='31f64f59' #l be xor 5dd62d3c
Z3=int(Z3,16)
P=3525886283
n=pow(2,32)
print n
for L in xrange(0,n): #generez toate numerele de la 0 al 2 la puterea 32
 if(L%10000000==0): #doar pentru verificare
  print L
 R=L^Z1
 new_L=(5*L + 11)%P
 new_R=(7*R + 19)%P
 Z=new_L^new_R
 if(Z==Z2):
  print "AICI AM AJUNS LA AL DOILEA",str(L),str(R)
  new_L=(5*new_L + 11)%P
  new_R=(7*new_R + 19)%P
  Z=new_L^new_R
  if(Z==Z3):
    print L,R
