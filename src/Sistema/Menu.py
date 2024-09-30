from Sistema.Metodos.Metodo_jacobi import Metodo_jacobi
class Menu():
    def menu(self):
       matriz = [[-1,3,1],[3,-1,-1],[2,1,4]]
       isinstance_medotoJacobi = Metodo_jacobi()
     
       respuesta = input("Selecciones el metodo que deseas:")
       if respuesta == "1":
           isinstance_medotoJacobi.Metodo_jacobi(matriz)
           

       


