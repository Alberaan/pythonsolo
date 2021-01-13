from tablesreader import *

def main():
    print("Bienvenido al programa de tablas aleatorias")
    tables = getTables()
    print(ayuda().data)
    while(1):
        print("Qué quieres hacer?:")
        aLlamar = input()
        datos = llamadaDinamica(tables, aLlamar)
        print(datos.message)
        print(datos.data)

if __name__ == "__main__":
    main()

