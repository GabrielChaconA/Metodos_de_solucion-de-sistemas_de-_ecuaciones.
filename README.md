# Metodos_de_solucion-de-sistemas_de-_ecuaciones.

## Resoulucion de matrices 
### Inversa 
```python
class inversa:


   def inversa(self, matriz):
      inversa =  np.zeros((3, 3))
     
      adj = self.adjA(matriz, self.determinante_A(matriz))
      adj = np.array(adj, dtype=float)


      return adj

   def determinante_A(self, matriz):
    n = 2
    suma = 0
    resta = 0
    for i in range(len(matriz)):
       contador =0
       for j in range(len(matriz[i])):
          
          if i+2 <= n and  j+2<= n:
             contador+=1
             suma = suma + (matriz[i][j]*matriz[i+1][j+1]*matriz[i+2][j+2])
             resta = resta + (matriz[n-i][j]*matriz[(n-i)-1][j+1]*matriz[(n-i)-2][j+2])
            
          else:
           if  i+1 <= n and  j+1<= n:
              contador+=1
              suma = suma +( matriz[i][j]*matriz[i+1][j+1])
              resta = resta + (matriz[n-i][j]*matriz[(n-i)-1][j+1])
              
       return suma-resta

    
    
          
   def adjA(self, matriz,A):
        matriz_adj =  np.zeros((3, 3))
      
        

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz_adj[i][j]  = self.operation_adj(matriz,i,j,A)
                 
                 
                 
        matriz_adj = np.array(matriz_adj, dtype=float)

        return matriz_adj

   def operation_adj(self, matriz, i,j,A):
     R  =  np.zeros((3, 3))
     n = 2
     contador =0
     a=0
     b=0
     v1=1
     v2=1
     suma = 1
     resta = 1
     for k in range(len(matriz)):
        for s in range (len(matriz[i])):
           if k!=i and s != j :
                if contador ==0:
                  a= k
                  b= s 
                  suma = matriz[a][b] * self.encontrarSuma(matriz,i,j,a,b)
                resta =v1*self.encontrarResta(matriz,i,j,a,b)
               
     return (suma-resta)/A

   def encontrarSuma(self, matriz, i, j , a, b):
      for k in range(len(matriz)):
        for s in range (len(matriz[i])):
           if k!=i and s != j and k!=a and s!=b:
              
              return matriz[k][s]
   def encontrarResta(self, matriz, i, j , a, b):
      v1=0
      v2=0
      for k in range(len(matriz)):
        for s in range (len(matriz[i])):
           if k!=i and s != j and k!=a:
              v1= matriz[k][s]
           if k!=i and s != j and s!=b:
              v2= matriz[k][s]
      return round(v1*v2,4)






```
## Operaciones 
### Suma y resta 
```python
class operaciones_Basicas:

    def resta(self, m1,m2):
        r_matriz  = np.zeros((len(m1), len(m2[0])))
        r_matriz = np.array(r_matriz, dtype=float)
        for i in range(len(r_matriz)):
            for j in range(len(r_matriz[i])):
                r_matriz[i][j] = m1[i][j]-m2[i][j]
        return r_matriz
    
    def suma(self, m1,m2):
        s_matriz  = np.zeros((len(m1), len(m2[0])))
        s_matriz = np.array(s_matriz, dtype=float)
        for i in range(len(s_matriz)):
            for j in range(len(s_matriz[i])):
                s_matriz[i][j] = m1[i][j]+m2[i][j]
        return s_matriz



```
### multiplicacion
```python
class multiplication:
    def multiplication(self,matriz1, matriz2):
        matriz_R =  np.zeros((len(matriz1), len(matriz2[0])))
        matriz_R = np.array(matriz_R, dtype=float)
        suma = 0
        for i in range(len(matriz_R)):
            for j in range(len(matriz_R[i])):
                matriz_R[i][j]=self.mul(matriz1, matriz2,i,j)

        return matriz_R

    def mul(self, matriz1, matriz2,i,j):
        suma =0
        for k in range (len(matriz2)):
            suma = suma +(matriz1[i][k]*matriz2[k][j])

        return suma

```



## Metodo de jacobi
```python
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
                          
                    





```
