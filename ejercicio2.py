from ast import main
import math
from unicodedata import name


def run():
  #  diccionary = {}
     
   # for i in range(1,101):
    #   if i % 3 !=0: 
     #   diccionary[i] = i**3
        
    
   # dict= {i: i**3 for i in range(1,101) if i%3 !=0}

    #print(dict)
    dicc = {i:math.sqrt(i) for i in range(1,1001)}
    print(dicc)
    


if __name__=="__main__":
    run()