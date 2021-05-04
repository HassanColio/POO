
class empleado:

def _init_(self,nombre,especialidad,carrera):
        self.nombre = nombre
        self.especialidad = especialidad
        self.carrera = carrera

    
    def detalles_programadores (self) :
        print ("Detalles del empleador")
        print("")
        print("Nombre", self.nombre)
        print("especialidad", self.especialidad)
        print("carrera",self.especialidad)

         def desarrolla(self):
        print("empleado desarrolla cualquier trabajo")
    
    def planifica(self):
        print("empleado  planifica cualquier trabajo")
   

class AdmProyect (empleado):

    def desarrolla(self):
        print("AdmProyect desarrolla")
    
    def planifica(self):
        print("AdmProyect planifica cualquier proyecto")


def desarrollo_test(AdmProyect):
    AdmProyect.desarrolla()


hassan = empleado()
leonardo = AdmProyect()

desarrollo_test(hassan)
desarrollo_test(leonardo)

class programador (empleado) :
     def desarrolla(self):
        print(" programador desarrolla software")
    
    def planifica(self):
        print("programador planifica proyectos de software")

    