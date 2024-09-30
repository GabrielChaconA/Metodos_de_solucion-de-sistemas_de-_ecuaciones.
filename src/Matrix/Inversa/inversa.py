import numpy as np
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
           
                  
   
