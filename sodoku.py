


af0c0, af0c1, af0c2, af0c3 =    5,  None,  None,  18
af1c0, af1c1, af1c2, af1c3 = None,  None,  None,  11
af2c0, af2c1, af2c2, af2c3 = None,  None,  None,  16
af3c0, af3c1, af3c2, af3c3 =   16,    12,    17,  14


bf0c0, bf0c1, bf0c2, bf0c3 =    5,  4,  9,  18
bf1c0, bf1c1, bf1c2, bf1c3 =    8,  2,  1,  11
bf2c0, bf2c1, bf2c2, bf2c3 =    3,  6,  7,  16
bf3c0, bf3c1, bf3c2, bf3c3 =    16, 12, 17, 14



import numpy as np

a = np.array([
    [af0c0,  af0c1,  af0c2,  af0c3],
    [af1c0,  af1c1,  af1c2,  af1c3],
    [af2c0,  af2c1,  af2c2,  af2c3],
    [af3c0,  af3c1,  af3c2,  af3c3]])


b = np.array([
    [bf0c0,  bf0c1,  bf0c2,  bf0c3],
    [bf1c0,  bf1c1,  bf1c2,  bf1c3],
    [bf2c0,  bf2c1,  bf2c2,  bf2c3],
    [bf3c0,  bf3c1,  bf3c2,  bf3c3]])

#Condiciones números dígitos 
if 0<bf0c1<=9 and 0<bf0c2<=9 and 0<bf1c0<=9 and 0<bf1c1<=9 and 0<bf1c2<=9 and 0<bf2c0<=9 and 0<bf2c1<=9 and 0<bf2c2<=9:

    #Condiciones suma de fila
    if bf0c0==5 and bf0c1==4 and bf0c2==9:
        bf0c3 = (bf0c0+  bf0c1+ bf0c2);
        
        if bf1c0==8 and bf1c1==2 and bf1c2==1:
            bf1c3 = (bf1c0+  bf1c1+ bf1c2);
            
            if bf2c0==3 and bf2c1==6 and bf2c2==7:
                bf2c3 = (bf2c0+  bf2c1+ bf2c2);
               
               
                #Condiciones suma de columnas
                if bf0c0==5 and bf1c0==8 and bf2c0==3:
                    bf3c0 = (bf0c0+  bf1c0+ bf2c0);
                    

                    if bf0c1==4 and bf1c1==2 and bf2c1==6:
                        bf3c1 = (bf0c1+  bf1c1+ bf2c1);
                        
                        if bf0c2==9 and bf1c2==1 and bf2c2==7:
                            bf3c2 = (bf0c2+  bf1c2+ bf2c2);
                            print (b)
                        else:
                            print (a)
                            print ("Error el número no aplica para este ejercicio de sodoku")

                    else:
                        print (a)
                        print ("Error el número no aplica para este ejercicio de sodoku")

                else:
                    print (a)
                    print ("Error el número no aplica para este ejercicio de sodoku")


            else:
                print (a)
                print ("Error el número no aplica para este ejercicio de sodoku")

        else:
            print (a)
            print ("Error el número no aplica para este ejercicio de sodoku")
    else:
        print (a)
        print ("Error el número no aplica para este ejercicio de sodoku")
else:
    print (a)
    print ("Error el número no aplica para este ejercicio de sodoku")
