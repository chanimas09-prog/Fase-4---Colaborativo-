# Fase-4---Colaborativo-
import datetime
import os 

print("Trabajo colaborativo")
self.title("Sistema Integral Orientado a Objetos")
Integrantes = ["Karen","Andersson","Sergio"]
print("Integrantes:", Integrantes)

# 1. Excepciones Personalizadas y Logger

class SoftwareFJException(Exception):
    """Excepción base del sistema"""
  pass
class ErrorValidacionException(SoftwareFJException)
  """Error cuando un dato ingresado no es válido"""
  pass 

class LoggerSistema: 
  """Clase para registrar eventos y errores automáticamente con fecha y hora"""
  LOG_FILE = "sistema_log.txt" 

  @classmethod 
  def registrar(cls, mensaje, tipo="INFO"):
    tiempo_actual = datetime. datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    linea = f"[{tiempo_actual}] [{tipo}] {mensaje}\n"
    print(f"LOG -> {linea.strip()}")
    try: 
        with open(cls.LOG_FILE, "a", encoding="utf-8") as f:
          f.write(linea)
    except Exception as e: 
      print(f"Error al escribir en el log: {e}")


# 2. Clases Base y Encapsulamiento

class EntidadSistema:
  def __init__(self, id_entidad):
    self.id_entidad = id_entidad


class Cliente(EntidadSistema):
  def __init__(self, id_entidad, nombre, correo):
    super().__init__(id_entidad)  
    self.nombre = nombre
    self.correo = correo

  @property
  def correo(self):
    return self._correo

  @correo.setter
  def correo(self, nuevo_correo):
    if "@" not in nuevo_correo:
      LoggerSistema.registrar(f"intento de correo inválido: {nuevo_correo}, "Error")
      raise ErrorValidacionException("El correo electrónico debe contener '@'.")
    self._correo = nuevo_correo

  def mostar_info(self):
    return f"Cliente:{self.nombre} | Correo: {self.correo}" 


# 3. Herencia y Polomorfismo (trabaje la herencia y el poliformismo)

class Servicios:
    def mostrar_detalles(self):
        return "Informacion general de servicios"

class AlquilerEquipos(Servicios):
  def mostrar_detalles(self):
      return "Alquiler de equipos de oficina, portatiles"
    
class SalasReunion(Servicios):
  def mostrar_detalles(self):
      return "Salas de reunion, equipos para videoconferencias"

      class AsesoriasEspecializadas(Servicios):
  def mostar_detalles(self):
      return "Asesorias especializadas, asesorias legales"

  # 4  clases de Reserva:

    def __init__(self, cliente, servicio, fecha_reserva=None):
        if not isinstance(cliente, Cliente):
            LoggerSistema.registrar(
                "Intento de crear reserva con un cliente inválido.", tipo="ERROR"
            )
            raise ErrorValidacionException("El objeto 'cliente' debe ser una instancia de Cliente.")

        if not isinstance(servicio, Servicios):
            LoggerSistema.registrar(
                f"Intento de crear reserva inválida para {cliente.nombre}.", tipo="ERROR"
            )
            raise ErrorValidacionException("El objeto 'servicio' debe ser una instancia de Servicios.")

        self.cliente = cliente
        self.servicio = servicio
        self.fecha_reserva = fecha_reserva or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def resumen(self):
        detalles_servicio = self.servicio.mostrar_detalles()
        return (
            f"-- DETALLES DE LA RESERVA --\n"
            f"Fecha: {self.fecha_reserva}\n"
            f"Cliente: {self.cliente.nombre} (ID: {self.cliente.id_entidad})\n"
            f"Servicio contratado: {detalles_servicio}\n"
            f"-----------------------------"
        )

    def mostrar_info(self):
        detalles_servicio = self.servicio.mostrar_detalles()
        LoggerSistema.registrar(
            f"Reserva generada para {self.cliente.nombre} con servicio: {detalles_servicio}",
            tipo="INFO",
        )
        print(self.resumen())



    







 

 



