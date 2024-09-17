from tipo_estudio import TipoEstudio
from abc import ABC, abstractmethod

class Estudio(ABC):
    def __init__(self, fecha_realizacion: str, denominacion: TipoEstudio) -> None:
        self._fecha_realizacion = fecha_realizacion
        self._denominacion = denominacion
    
    def get_denominacion(self) -> TipoEstudio:
        return self._denominacion
    
    @abstractmethod
    def calcular_costo(self) -> float:
        pass