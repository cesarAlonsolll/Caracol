nombreArchivo = "TextoCaracol.txt"

def cargarCaracol(nombre):
    lector = open(nombre,"r")
    laberinto = lector.read().replace(',',' ').split('\n')
    return tuple([tuple(linea.split()) for linea in laberinto])

def verificarMatriz(caracol):
    if len(caracol)>1 and len(caracol[0])>1:
        return True
    return False

def recorrerCaracol(caracol):
    
    def definirDireccion(direccion):
        return [direccion[1],-direccion[0]]
    
    def definirCoordenadas(coordenadas, direccion, dimension):
        return [coordenadas[0]+(direccion[0]*dimension[0])+definirDireccion(direccion)[0],
                coordenadas[1]+(direccion[1]*dimension[1])+definirDireccion(direccion)[1]]
    
    def recorrer(coordenadas, direccion, cantidad):
        if cantidad>1:
            return [caracol[coordenadas[0]][coordenadas[1]]]+recorrer([coordenadas[0]+direccion[0],coordenadas[1]+direccion[1]],
                                                                      direccion, cantidad-1)
        else:
            return [caracol[coordenadas[0]][coordenadas[1]]]
    
    def vertical(coordenadas, direccion, dimension):
        if dimension[0]>0:
            return recorrer(coordenadas, direccion, dimension[0])+horizontal(
                    definirCoordenadas(coordenadas, direccion, [dimension[0]-1,dimension[1]]),
                    definirDireccion(direccion), [dimension[0],dimension[1]-1])
        else:
            return []
    
    def horizontal(coordenadas, direccion, dimension):
        if dimension[1]>0:
            return recorrer(coordenadas, direccion, dimension[1])+vertical(
                    definirCoordenadas(coordenadas, direccion, [dimension[0],dimension[1]-1]),
                    definirDireccion(direccion), [dimension[0]-1,dimension[1]])
        else:
            return []
    
    return horizontal([0,0], [0,1], [len(caracol),len(caracol[0])])

caracol = cargarCaracol(nombreArchivo)

if verificarMatriz(caracol):
    print(recorrerCaracol(caracol))
else:
    print("Laberinto inadecuado.")
    