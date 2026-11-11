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




    

# trabaje la herencia y el poliformismo

class Servicios:
  def mostrar_detalles(self):
  return "informacion general de servicios"
class alquilerequipos(Servicios):
  def mostrar_detalles(self):
  return "alquiler de equipos de oficina, portatiles"
class salasreunion(Servicios):
  def mostrar_detalles(self):
  return "salas de reunion, equipos para videoconferencias"
class asesoriasespecializadas(Servicios):
  def mostar_detalles(self):
  return "asesorias especializadas, asesorias legales
  
class reservas:
  def__init__(self, cliente, servicios):
  self.cliente = cliente
  self.servicios = servicios
  def mostrar info(self):
  print(f"cliente:{self.cliente} / servicios:{self.servicios.mostrardetalles}")

servicio = salasreunion()
reserva = reserva ("ana",servicio)
reserva.mostrar_info()







 

 



