
from deportista import Deportista
from persona import Persona


class Futbolista(Deportista):
  
  listaFutbolistas=[]
  def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,rojas,piernaHabil):
    
    super().__init__(nombre,edad,altura,sexo,"Futbol",añosPracticando)
    self.golesMarcados=golesMarcados
    self.rojas=rojas
    self.piernaHabil=piernaHabil
    Futbolista.listaFutbolistas.append(self)

  def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), str(self.getEdad()), str(self.getAñosPracticando()))



  def getGolesMarcados(self):
    return self.golesMarcados
    
  def getTarjetasRojas(self):
    return self.tarjetasRojas
    
  def getPiernaHabil(self):
    return self.piernaHabil

  
      
  @classmethod
  def getListaFutbolistas(cls):
    cls.listaFutbolistas
    
