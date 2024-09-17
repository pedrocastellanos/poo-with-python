from embarazada import Embarazada
from tipo_estudio import TipoEstudio
from excepciones.excepcion_paciente import ExcepcionPaciente

class Sala:
    def __init__(self, nombre: str, capacidad: int) -> None:
        self._nombre = nombre
        self._capacidad = capacidad
        self_embarazadas = []
        
    def eliminar_paciente(self, ci: str) -> None:
        embarazda = self.obtener_embarazada_por_ci(ci)
        if embarazda is not None:
            self._embarazadas.remove(embarazda)
        else: raise ExcepcionPaciente("No se encontro el paciente con CI: " + ci)
            
    def obtener_estudios_por_tipo(self, tipo: TipoEstudio) -> int:
        cant = 0
        for embarazada in self._embarazadas:
            for estudio in embarazada.get_estudios():
                if estudio.get_denominacion() == tipo:
                    cant += 1
        return cant
    
    def calcular_costo_total_paciente(self, ci: str) -> float:
        embarazda = self.obtener_embarazada_por_ci(ci)
        if embarazda is not None:
            costo = 0
            for embarazada in self._embarazadas:
                if embarazada.get_ci() == ci:
                    for estudio in embarazada.get_estudios():
                        costo += estudio.calcular_costo()
            return costo
        else: raise ExcepcionPaciente("No se encontro el paciente con CI: " + ci)
    
    def obtener_embarazadas_sobre_umbral(self, umbral: float) -> int:
        cant = 0
        for embarazada in self._embarazadas:
            if embarazada.calcular_costo_total() > umbral:
                cant += 1
        return cant
        
    def obtener_embarazada_por_ci(self, ci: str) -> Embarazada:
        for embarazada in self._embarazadas:
            if embarazada.get_ci() == ci:
                return embarazada
        return None
    
    def guardar_reporte(self):
        try:
            with open("reporte_embarazada.txt", 'w') as archivo:
                archivo.write("Nombre" + "\t" + "Costo")
                for e in self.embarazadas:
                    archivo.write(e.get_nombre() + "\t" + str(e.calcular_costo_total()) + "\n")
            archivo.close()
            print(f"Archivo guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")