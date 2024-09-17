from general import General
from especifico import Especifico
from estudio import Estudio
from tipo_estudio import TipoEstudio
from excepciones.excepcion_resultado_estudios import ExcepcionResultadoEstudios

class Embarazada():
    def __init__(self, ci: str, nombre: str, talla: str) -> None:
        self._ci = ci
        self._nombre = nombre
        self._talla = talla
        self._estudios = []


    def agregar_estudio(self, fecha_realizacion: str, resultado_v1: int, resultado_v2: int, resultado_v3: int, cant_reactivo: float, tiempo: int):
        if 3 <= resultado_v1 <= 17: raise ExcepcionResultadoEstudios("El resultado V1 debe estar entre 3 y 17")
        if 30 <= resultado_v2 <= 60: raise ExcepcionResultadoEstudios("El resultado V2 debe estar entre 30 y 60")
        if not resultado_v3: raise ExcepcionResultadoEstudios("El resultado V3 debe ser positivo")
        
        self.estudios.append(General(fecha_realizacion, TipoEstudio.GENERAL ,resultado_v1, resultado_v2, resultado_v3, cant_reactivo, tiempo))
        
    
    def agregar_estudio(self, fecha_realizacion: str, resultado_v1: list[int], cant_reactivo: float):
        if (isinstance(resultado_v1, list) and all(isinstance(elemento, int) and 10 <= elemento <= 100 for elemento in resultado_v1)): 
            raise ExcepcionResultadoEstudios("El resultado V1 debe ser una lista de números enteros entre 10 y 100")
        
        self.estudios.append(Especifico(fecha_realizacion, TipoEstudio.ESPECIFICO, resultado_v1, cant_reactivo))
        
    def get_ci(self) -> str:
        return self._ci
    
    def get_tipo_estudios(self) -> list[TipoEstudio]:
        return self.estudios
    
    def calcular_costo_total(self) -> float:
        return sum([estudio.calcular_costo() for estudio in self.estudios])
        
    


