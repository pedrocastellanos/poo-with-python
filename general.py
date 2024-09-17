from estudio import Estudio
from tipo_estudio import TipoEstudio

class General(Estudio):
    def __init__(self, fecha_realizacion: str, denominacion: TipoEstudio, resultado_v1: int, resultado_v2: int, resultado_v3: int, cant_reactivo: float, tiempo: int) -> None:
        super().__init__(fecha_realizacion, denominacion)
        self._resultado_v1 = resultado_v1
        self._resultado_v2 = resultado_v2
        self._resultado_v3 = resultado_v3
        self._cant_reactivo = cant_reactivo
        self._tiempo = tiempo
        
    def calcular_costo(self) -> float:
        return self._cant_reactivo * 11.8 + self._tiempo * 1.25
    