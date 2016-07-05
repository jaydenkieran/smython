from smite import SmiteClient
from smite import Endpoint

# Create a new instance of the client
smite = SmiteClient(1700, '2djsa8231jlsad92ka9d2jkad912j')
# Print JSON data for all of the gods in the game on PC
print(smite.get_gods())

# Make the library use the Xbox endpoint for future requests
smite._switch_endpoint(Endpoint.XBOX)
# Print JSON data for all of the gods in the game on Xbox
print(smite.get_gods())