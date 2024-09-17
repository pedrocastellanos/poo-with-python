from estudio import Estudio
from tipo_estudio import TipoEstudio

class Especifico(Estudio):
    def __init__(self, fecha_realizacion: str, denominacion: TipoEstudio, resultado_v1: list[int], cant_reactivo: float) -> None:
        super().__init__(fecha_realizacion, denominacion)
        self._resultado_v1 = resultado_v1
        self._cant_reactivo = cant_reactivo
        
    def calcular_costo(self)-> float:
        return self._cant_reactivo * 1.34