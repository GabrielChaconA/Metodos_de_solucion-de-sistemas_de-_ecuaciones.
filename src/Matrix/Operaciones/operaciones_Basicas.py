import numpy as np
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