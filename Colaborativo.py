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



    
class Servicios:
  def__init__(self, alquiler_de_equipos, salas_de_reunion, asesorias_especializadas):
  self.alquiler_de_equipos = alquiler_de_equipos
  self.salas_de_reunion = salas_de_reuninon
  self.asesorias_especializadas = asesorias_especializadas 
  
class reservas:
  def__init__(self, cliente, servicios):
  self.cliente = cliente
  self.servicios = servicios
  def mostrar info(self):
  print("cliente:{self.cliente} servicios:{self.servicios}")
  c1=cliente ("ana")
  s1=servicios ("alquiler de equipos, salas de reunion, asesorias especializadas")
  r1=reservas(c1,s1)
  r1.mostrar info()

  



