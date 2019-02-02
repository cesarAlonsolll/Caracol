nombreArchivo = "TextoCaracol.txt"

def cargarCaracol(nombre):
    lector = open(nombre,"r")
    laberinto = lector.read().replace(',',' ').split('\n')
    return tuple([tuple(map(int, linea.split())) for linea in laberinto])

def verificarMatriz(caracol):
    if len(caracol)>1 and len(caracol)==len(caracol[0]):
        return True
    return False

def recorrerCaracol(caracol):
    
    def definirCoordenadas(coordenadas, direccion, dimension):
        return [coordenadas[0]]
    
    def inicio(coordenadas, direccion, dimension):
        return recorrer(coordenadas, direccion, dimension)+ciclo(coordenadas, direccion, dimension)
        pass
    
    def ciclo(coordenadas, direccion, dimension):
        pass
    
    def recorrer(coordenadas, direccion, cantidad):
        pass
    
    return inicio([0,0], [0,1], len(caracol))

caracol = cargarCaracol(nombreArchivo)

if verificarMatriz(caracol):
    print(caracol)
else:
    print("Laberinto inadecuado.")