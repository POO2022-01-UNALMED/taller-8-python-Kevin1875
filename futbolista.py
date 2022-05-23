
from deportista import Deportista


class Futbolista(Deportista):
  
  listaFutbolistas=[]
  def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,rojas,pierna):
    
    super().__init__(nombre,edad,altura,sexo,"Futbol",añosPracticando)
    self.golesMarcados=golesMarcados
    self.rojas=rojas
    self.pierna=pierna
    Futbolista.listaFutbolistas.append(self)

  def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), str(self.getEdad()), str(self.getAñosPracticando()))

 

  def getGolesMarcados(self):
    return self._golesMarcados
    
  def getTarjetasRojas(self):
    return self._tarjetasRojas
    
  def getPiernaHabil(self):
    return self._piernaHabil

  
      
  @classmethod
  def getListaFutbolistas(cls):
    cls._listaFutbolistas
    
