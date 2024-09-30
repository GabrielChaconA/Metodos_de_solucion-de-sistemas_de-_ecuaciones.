import numpy as np
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

