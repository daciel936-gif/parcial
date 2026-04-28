peliculas = {
    "Mortal Kombat": {"precio": 12000, "boletas": 10, "horarios": ("2pm", "5pm")},
    "Matrix": {"precio": 15000, "boletas": 8, "horarios": ("3pm", "6pm")},
    "Interestelar": {"precio": 18000, "boletas": 5, "horarios": ("4pm", "7pm")}
}

historial = []

def mostrar_peliculas():
    print("\npeliculas disponibles:")
    for i, peli in enumerate(peliculas, 1):
        datos = peliculas[peli]
        print(f"{i}. {peli}, ${datos['precio']}, disponibles: {datos['boletas']}")
def elegir_pelicula():
    try:
        opcion = int(input("elige una pelicula (numero): "))
        nombres = list(peliculas.keys())
        return nombres[opcion - 1]
    except:
        print("error, opcion invalida")
        return None
def comprar():
    mostrar_peliculas()
    peli = elegir_pelicula()
    if peli is None:
        return
    try:
        cantidad = int(input("cuantas boletas quieres?: "))
        disponibles = peliculas[peli]["boletas"]
        if cantidad > disponibles:
            print("no hay suficientes boletas")
            return
        total = cantidad * peliculas[peli]["precio"]
        print(f"total a pagar: ${total}")
        confirmar = input("confirmar compra? (s/n): ")
        if confirmar == "s":
            peliculas[peli]["boletas"] -= cantidad
            historial.append({
                "pelicula": peli,
                "cantidad": cantidad,
                "total": total
            })
            print("compra realizada con exito")
        else:
            print("compra cancelada")
    except:
        print("error al ingresar datos")

def ver_historial():
    print("\nhistorial:")
    for compra in historial:
        print(compra)
def menu():
    while True:
        print("\n1.comprar")
        print("2.historial")
        print("3.salir")
        opcion = input("elige una opcion:")
        if opcion == "1":
            comprar()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("adios")
            break
        else:
            print("opcion invalida")

menu()
