import json
from types import SimpleNamespace

class charactersheet:
    
    def __init__(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        
        character = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
        self.__dict__ = character.__dict__

Alberaan = charactersheet("./charactersheets/data.txt")
print(Alberaan.Atributos.Fuerza)
