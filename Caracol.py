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
    
    def definirDireccion(direccion):
        return [direccion[1],-direccion[0]]
    
    def definirCoordenadas(coordenadas, direccion, dimension):
        return [coordenadas[0]+(direccion[0]*dimension)+definirDireccion(direccion)[0],
                coordenadas[1]+(direccion[1]*dimension)+definirDireccion(direccion)[1]]
    
    def recorrer(coordenadas, direccion, cantidad):
        if cantidad>1:
            return [caracol[coordenadas[0]][coordenadas[1]]]+recorrer([coordenadas[0]+direccion[0],coordenadas[1]+direccion[1]],
                                                                      direccion, cantidad-1)
        else:
            return [caracol[coordenadas[0]][coordenadas[1]]]
    
    def ciclo2(coordenadas, direccion, dimension):
        if dimension>0:
            return recorrer(coordenadas, direccion, dimension)+ciclo1(
                    definirCoordenadas(coordenadas, direccion, dimension-1),
                    definirDireccion(direccion), dimension)
        else:
            return []
    
    def ciclo1(coordenadas, direccion, dimension):
        return recorrer(coordenadas, direccion, dimension)+ciclo2(
                definirCoordenadas(coordenadas, direccion, dimension-1),
                definirDireccion(direccion), dimension-1)
    
    return ciclo1([0,0], [0,1], len(caracol))

caracol = cargarCaracol(nombreArchivo)

if verificarMatriz(caracol):
    print(recorrerCaracol(caracol))
else:
    print("Laberinto inadecuado.")