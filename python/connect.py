import socket

# IP et port du service à se connecter
ip = "192.168.24.105"
port = 4210

# Création d'un objet socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connexion au service
sock.connect((ip, port))

# Boucle d'écoute des données
while True:
    # Réception des données du service
    data = sock.recv(1024)
    
    # Vérification que des données ont été reçues
    if not data:
        break
    
    # Affichage des données reçues
    print(f"Received data: {data}")

# Fermeture de la connexion
sock.close()
