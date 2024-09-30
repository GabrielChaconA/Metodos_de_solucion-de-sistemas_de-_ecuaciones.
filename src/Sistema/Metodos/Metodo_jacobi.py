from Matrix.Operaciones.Multiplicacion import multiplication
from Matrix.Operaciones.operaciones_Basicas import operaciones_Basicas
from Matrix.Inversa.inversa import inversa
from Sistema.Errores.Error_Relativo import Error_Relativo
import numpy as np
class Metodo_jacobi:
    #Se resuelven los pasos de la matriz 
    def Metodo_jacobi(self, A):
        isinstance_multuplication = multiplication()
        isinstance_opereaciones = operaciones_Basicas()
        isinstance_inversa = inversa()
        ##declare ,as matrices 
        valor_Inicial = [0],[0],[0]
        B = [3],[1],[7]
        D = [[A[0][0], 0, 0],
            [0, A[1][1], 0],
            [0, 0, A[2][2]]]
        print(type(str(D)))

        ##convierto a float las matrices para poder hacer las operaciones
        D = np.array(D, dtype=float)
        B = np.array(B, dtype=float)

        ##empiezo a ejecutar los procedimientos
        Tx = isinstance_opereaciones.resta(D,A)
        print("Tx")
        print(Tx)

       ## Matriz inversa
        D1 = isinstance_inversa.inversa(D)
        print("Inversa")
        print(D1)
        T = isinstance_multuplication.multiplication(D1,Tx)
        print("T")
        print(T)
        C = isinstance_multuplication.multiplication(D1,B)
        print("C")
        print(C)
        self.encontrar_Valor(T,C,valor_Inicial)


        return None
    
    ##En este metodo se buscara el error relativo y se ejecutara el codigo para encontrar
    def encontrar_Valor(self,T, C,valor_Inicial):
        ##creo las matricecs para guardar valores 
        r_matriz  = np.zeros((3, 1))
        valoresF  = np.zeros((3, 1))
        flag = True
        flag_While= True
        cont =0

        ##convierto a flotante para evitar errores
        r_matriz = np.array(r_matriz, dtype=float)
        valoresF = np.array(valoresF, dtype=float)
        error = 0


        isinstance_error = Error_Relativo()
        isinstance_opereaciones = operaciones_Basicas()
        isinstance_multuplication = multiplication()
        while(flag_While):
             for i in range (len(r_matriz)) :
                  for j in range(len(r_matriz[i])):
                      r_matriz = isinstance_opereaciones.suma(isinstance_multuplication.multiplication(T, valor_Inicial), C )
                      print ("Paso 4: \n {} ".format(r_matriz))
                      print("Error: ")
                      print(error)
                      if flag:
                          vAnterio= r_matriz[i][j]
                          flag = False
                      if isinstance_error.Error_Relativo(r_matriz[i][j], vAnterio ) < 0.005:
                          error =isinstance_error.Error_Relativo(r_matriz[i][j], vAnterio )

                          vAnterio= r_matriz[i][j]
                      else:
                          cont+=1
                          valoresF[i][j] = r_matriz[i][j]
                          if cont==3:
                              flag_While =  False
                      valor_Inicial= r_matriz
                          
                    
                 
           
            
            

        
       

    