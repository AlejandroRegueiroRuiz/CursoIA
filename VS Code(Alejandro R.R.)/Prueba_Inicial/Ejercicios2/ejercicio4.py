import fibonacci,temperature_converter


def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Calcular la secuencia de Fibonacci hasta un número")
    print("2. Convertir temperatura de ºC a ºF")
    print("3. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            numero = int(input("Ingrese un número: "))
            resultado = fibonacci.fibonacci(numero) 
            print(f"La secuencia de Fibonacci hasta {numero} es: ", end="")
            for num in resultado:
                print(num, end=" ")
            print("")
        elif opcion == '2':

            escala = input("Introduzca F para convertir de Fahrenheit a Celsius(Si no introduces nada o tecleas C usa Celsius): ")
            while escala !="" and escala.upper() !="C" and escala.upper() !="F":
                escala = input("Introduzca F para convertir de Fahrenheit a Celsius(Por defecto convierte de Celsius a Fahrenheit): ")
            temp = float(input("Ingrese la temperatura en º: "))

            if escala == "" or escala == "C":
                print(temperature_converter.convertir_de_C_a_F(temp))
            else:
                print(temperature_converter.convertir_de_F_a_C(temp))
            
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        input("Presione enter para continuar ")
    