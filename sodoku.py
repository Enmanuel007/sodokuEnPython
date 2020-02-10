
import numpy as np
import random
from timeit import default_timer


#fila 0
bf0c0 = 5
bf0c1 = random.randrange(1, 10)
bf0c2 = random.randrange(1, 10)
bf0c3 = 18

#fila1
bf1c0 = random.randrange(1, 10)
bf1c1 = random.randrange(1, 10)
bf1c2 = random.randrange(1, 10)
bf1c3 = 11

#fila2
bf2c0 = random.randrange(1, 10)
bf2c1 = random.randrange(1, 10)
bf2c2 = random.randrange(1, 10)
bf2c3 = 16

#fila3
bf3c0 = 16
bf3c1 = 12
bf3c2 = 17
bf3c3 = 14


bandera = True
while bandera:
    bf0c1 = random.randrange(1, 10)
    bf0c2 = random.randrange(1, 10)

    bf1c0 = random.randrange(1, 10)
    bf1c1 = random.randrange(1, 10)
    bf1c2 = random.randrange(1, 10)
    
    bf2c0 = random.randrange(1, 10)
    bf2c1 = random.randrange(1, 10)
    bf2c2 = random.randrange(1, 10)
    
    b = np.array([
    [bf0c0,  bf0c1,  bf0c2,  bf0c3],
    [bf1c0,  bf1c1,  bf1c2,  bf1c3],
    [bf2c0,  bf2c1,  bf2c2,  bf2c3],
    [bf3c0,  bf3c1,  bf3c2,  bf3c3]])
    
#Condiciones suma fila
    if (bf0c0+bf0c1+bf0c2==18):
        
        
        
        if (bf1c0+bf1c1+bf1c2==11):
           
            

            if (bf2c0+bf2c1+bf2c2==16):
               
                
                #Condición suma diagonal
                if (bf0c0+bf1c1+bf2c2==14):
                   
                    
                    #Condiciones suma columna
                    if (bf0c0+bf1c0+bf2c0==16):
                        
                        
                        if (bf0c1+bf1c1+bf2c1==12):
                            
                            
                            if (bf0c2+bf1c2+bf2c2==17):
                                
                                
                                if (bf0c0!= bf0c1 and bf0c0!= bf0c2 and bf0c0!= bf1c0 and bf0c0!= bf1c1 and bf0c0!= bf1c2 and bf0c0!= bf2c0 and bf0c0!= bf2c1 and bf0c0!= bf2c2):
                                     

                                    if (bf0c1!= bf0c0 and bf0c1!= bf0c2 and bf0c1!= bf1c0 and bf0c1!= bf1c1 and bf0c1!= bf1c2 and bf0c1!= bf2c0 and bf0c1!= bf2c1 and bf0c1!= bf2c2): 
                                        

                                        if( bf0c2!= bf0c0 and bf0c2!= bf0c1 and bf0c2!= bf1c0 and bf0c2!= bf1c1 and bf0c2!= bf1c2 and bf0c2!= bf2c0 and bf0c2!= bf2c1 and bf0c2!= bf2c2):
                                            
                                            if(bf1c0!= bf0c0 and bf1c0!= bf0c1 and bf1c0!= bf0c2 and bf1c0!= bf1c1 and bf1c0!= bf1c2 and bf0c2!= bf2c0 and bf0c2!= bf2c1 and bf0c2!= bf2c2):
                                                
                                                if (bf1c1!= bf0c0 and bf1c1!= bf0c1 and bf1c0!= bf0c2 and bf1c1!= bf1c0 and bf1c1!= bf1c2 and bf1c1!= bf2c0 and bf1c1!= bf2c1 and bf0c2!= bf2c2):
                                                    
                                                    if (bf1c2!= bf1c0 and bf1c2!= bf0c1 and bf1c0!= bf0c2 and bf1c2!= bf1c0 and bf1c2!= bf1c1 and bf1c2!= bf2c0 and bf1c2!= bf2c1 and bf0c2!= bf2c2):
                                                        
                                                        if (bf2c0!= bf0c0 and bf2c0!= bf0c1 and bf2c0!= bf0c2 and bf2c0!= bf1c0 and bf2c0!= bf1c1 and bf2c0!= bf1c2 and bf2c0!= bf2c1 and bf2c0!= bf2c2):
                                                            
                                                            if (bf2c1!= bf0c0 and bf2c1!= bf0c1 and bf2c1!= bf0c2 and bf2c1!= bf1c0 and bf2c1!= bf1c1 and bf2c1!= bf1c2 and bf2c1!= bf2c0 and bf2c1!= bf2c2):
                                                                
                                                                if (bf2c2!= bf0c0 and bf2c2!= bf0c1 and bf2c2!= bf0c2 and bf2c2!= bf1c0 and bf2c2!= bf1c1 and bf2c2!= bf1c2 and bf2c2!= bf2c0 and bf1c2!= bf2c1):
                                                                    print(b)
                                                                    bandera = False
                                                                    


                            



  