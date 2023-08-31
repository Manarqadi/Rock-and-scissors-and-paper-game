# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
print("\n rock , paper and scissors game:)")
Choice=["rock","paper","scissors"]
for _ in range(6):
 experience=input("enter your experience:")
 select=random.choice(Choice)

 print("computer random is:",select)
 print("person  experience is:", experience )
#rock
 if (select=="rock" and experience=="rock"):
    print("poth is win")
 elif (select=="rock" and experience=="paper"):
    print("person is win")
 elif (select=="rock" and experience=="scissors"):
    print("computer  is win")

 #paper   
 elif(select=="paper" and experience=="paper"):
    print("poth is win")
 elif (select=="paper" and experience=="scissors"):
    print("person is win")
 elif (select=="paper" and experience=="rock"):
    print("computer  is win")

#scissors
 elif(select=="scissors" and experience=="scissors"):
     print("poth is win")
 elif (select=="scissors" and experience=="rock"):
     print("person is win")
 elif (select=="scissors" and experience=="paper"):
     print("computer is win")
     
 else:
     print(" your input is wrong")

