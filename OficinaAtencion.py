from Queue import *
from Auxilios import *

# 2 colas: colaRemolque y colaReparacion
# interno de la central: 1 a 999
# cantidad critica de auxilios por defecto: 50
class OficinaAtencion():
    def __init__(self, nroInterno, cantCritica=50):
        self.colaRemolque = Queue()
        self.colaReparacion = Queue()
        self.interno = validar(interno)
        self.cantCritica = cantCritica
    
    def validar(self, interno):
        salida = None
        if 0 < interno < 1000:
            salida = interno
        else:
            salida = "Numero fuera de rango, por favor ingrese un número del 1 al 999"
        return salida
    
    def interno(self):
        return self.interno
    ###################################################################
    def recibirAuxilio(self, auxilio):
        if auxilio.tipo == 0:
            situacionCritica()
            self.colaRemolque.enqueue(auxilio)
        else:
            situacionCritica()
            self.colaReparacion.enqueue(auxilio)
    
    def primerAuxilioAEnviar(self):
        salida = None
        if self.colaRemolque.size() > 0:
            salida = self.colaRemolque.top()
        else:
            salida = self.colaReparacion.top()
        return salida

# recibe la zona donde se encuentra una grua
# devuelve y desencola el primer auxilio que se le puede enviar,
# la zonaDeGrua debe ser la zona De Partida del auxilio. remolques tienen prioridad
    def enviarAuxilio(self, zonaDeGrua):
        pass

# retorna la cantidad de auxilios de cada tipo:, ej: Remolque: n ; Reparacion: n
    def auxiliosPorTipo(self):
        # Ver el orden que se espera y si es lo esperado
        return self.colaRemolque.size(), self.colaReparacion.size()

# retorna la cantidad sumando las dos colas
    def cantidadTotalAuxilios(self):
        return self.colaRemolque.size() + self.colaReparacion.size()

# retorna true si alguna de las dos colas supera la cant critica
    def esCritica(self):
        return self.esCriticaRemolque() or self.esCriticaReparacion()
    #funciones auxiliares
    def esCriticaRemolque(self):
        return self.colaRemolque.size() >= self.cantCritica
    def esCriticaReparacion(self):
        return self.colaReparacion.size() >= self.cantCritica

# retorna el total de auxilios con estado: espera. sumando las dos colas
    def auxiliosEnEspera(self):
        return self.contarEnEspera(self.colaRemolque) + self.contarEnEspera(self.colaReparacion)

# recibe una patente
# retorna(sin eliminarlo) el auxilio pedido por esa patente si hay alguno en las colas
    def buscarAuxilio(self, nroPatente):
        pass

# recibe una patente
# elimina el auxilio pedido por esa patente  si hay.
    def eliminarAuxilio(self, nroPatente):
        pass

# recibe una patente
# verifica que exista un pedido de esa patente
# lo cambia de cola(reparacion - remolque)
    def cambiaDeTipo(self, nroPatente):
        pass
    
    def situacionCritica(self):
        if self.esCritica():
            print("Situación Crírtica")
        else: 
            pass 
    
    def contarEnEspera(self,cola):
        clon = cola.clone()
        count = 0
        for i in range(len(clon)):
            aux = clon.dequeue()
            if aux.enEspera():
                count += 1
        return count
    