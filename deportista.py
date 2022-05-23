from persona import Persona


class Deportista(Persona):
  def __init__(self,nombre,edad,altura,sexo,deporte,añosPracticando):
    super().__init__(nombre,edad,altura,sexo)
    self.deporte=deporte
    self.añosPracticando=añosPracticando


  def getDeporte(self):
    return self.deporte

  def setDeporte(self,deporte):
    self.deporte=deporte
  
    
  def getAñosPracticando(self):
    return self.añosPracticando

  
  def setAñosPracticando(self,añosPracticando):
    self.añosPracticando=añosPracticando