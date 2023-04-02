import socket
import time
import zeroconf


# Définition d'une classe pour gérer les services
class MyListener:
    def __init__(self):
        self.service_info = None
    
    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            self.service_info = info
            print("Service Info:",self.service_info.name, self.service_info.parsed_addresses()[0], self.service_info.port)

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))
        


# Création d'un objet zeroconf
zeroconf_obj = zeroconf.Zeroconf()

# Création d'un écouteur pour les services
listener = MyListener()

# Recherche de tous les services disponibles pendant 10 secondes
browser = zeroconf.ServiceBrowser(zeroconf_obj, "_carnode._udp.local.", listener)
time.sleep(10)




# Fermeture de l'objet zeroconf
zeroconf_obj.close()
