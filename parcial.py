import random

class Nodo:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        self.liga = None

    def __str__(self):
        return f"{self.nombre}: {self.salario:.2f}"

class ListaEnlazada:
    def __init__(self):
        self.cab = None

    def insertar_ordenado(self, nombre, salario):
        nuevo_nodo = Nodo(nombre, salario)
        if self.cab is None or self.cab.nombre > nombre:
            nuevo_nodo.liga = self.cab
            self.cab = nuevo_nodo
        else:
            aux = self.cab
            while aux.liga is not None and aux.liga.nombre < nombre:
                aux = aux.liga
            nuevo_nodo.liga = aux.liga
            aux.liga = nuevo_nodo

    def obtener_promedio_salarios(self):
        total_salarios = 0
        contador = 0
        aux = self.cab
        while aux is not None:
            total_salarios += aux.salario
            contador += 1
            aux = aux.liga
        return total_salarios / contador if contador > 0 else 0

    def empleados_inferiores_iguales_promedio(self):
        promedio = self.obtener_promedio_salarios()
        empleados = []
        aux = self.cab
        while aux is not None:
            if aux.salario <= promedio:
                empleados.append(aux)
            aux = aux.liga
        return empleados

    def eliminar_menor_salario(self):
        if self.cab is None:
            return
        menor = self.cab
        menor_ant = None
        aux = self.cab
        ant = None
        while aux is not None:
            if aux.salario < menor.salario:
                menor = aux
                menor_ant = ant
            ant = aux
            aux = aux.liga
        if menor_ant is None:
            self.cab = menor.liga
        else:
            menor_ant.liga = menor.liga

    def disminuir_salario_ana_ruiz(self):
        aux = self.cab
        while aux is not None:
            if aux.nombre == "Ana Ruiz":
                aux.salario *= 0.9
                break
            aux = aux.liga

    def imprimir_lista(self):
        aux = self.cab
        while aux is not None:
            print(aux)
            aux = aux.liga

                ###PARTE 2 PARCIAL###

    def obtener_empleados_en_posiciones_pares(self):
        nueva_lista = ListaEnlazada()
        aux = self.cab
        i = 0
        while aux is not None:
            if i % 2 == 0:  
                nueva_lista.insertar_ordenado(aux.nombre, aux.salario)
            aux = aux.liga
            i += 1
        return nueva_lista

    def obtener_empleados_menor_al_ultimo(self):
        if self.cab is None or self.cab.liga is None:
            return 0


        aux = self.cab
        while aux.liga is not None:
            aux = aux.liga
        salario_ultimo = aux.salario

        
        count = 0
        aux = self.cab
        while aux is not None:
            if aux.salario < salario_ultimo:
                count += 1
            aux = aux.liga
        return count

def main():
    lista = ListaEnlazada()

    print("Ingrese los datos de 500 empleados:")
    for _ in range(5):
        while True:
            try:
                nombre = input("Nombre del empleado: ")
                salario = float(input("Salario del empleado: "))
                if salario < 0:
                    print("El salario no puede ser negativo. Intente de nuevo.")
                    continue
                lista.insertar_ordenado(nombre, salario)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número para el salario.")

    lista.insertar_ordenado("Ana Ruiz", 2000.00)

    print("\nLista de empleados:")
    lista.imprimir_lista()

    print("\nEmpleados con salarios inferiores o iguales al promedio de salarios:")
    empleados_inferiores = lista.empleados_inferiores_iguales_promedio()
    for emp in empleados_inferiores:
        print(emp)

    print(f"\nCantidad de empleados con salarios inferiores o iguales al promedio: {len(empleados_inferiores)}")

    lista.eliminar_menor_salario()
    print("\nLista después de eliminar el empleado con el salario más bajo:")
    lista.imprimir_lista()

    lista.disminuir_salario_ana_ruiz()
    print("\nLista después de disminuir el salario de Ana Ruiz en un 10%:")
    lista.imprimir_lista()

    nueva_lista_pares = lista.obtener_empleados_en_posiciones_pares()
    print("\nEmpleados en posiciones pares:")
    nueva_lista_pares.imprimir_lista()

    cantidad_menores_al_ultimo = lista.obtener_empleados_menor_al_ultimo()
    print(f"\nCantidad de empleados con salario menor que el último empleado: {cantidad_menores_al_ultimo}")

if __name__ == "__main__":
    main()
