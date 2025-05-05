# calculadora.py

import operadores  # Importamos el módulo de operadores

def obtener_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

def obtener_operador():
    operadores_validos = ['+', '-']
    while True:
        operador = input("Ingresa un operador (+, -): ")
        if operador in operadores_validos:
            return operador
        else:
            print("Operador no válido. Intenta de nuevo.")

def main():
    print("Bienvenido a la calculadora.")
   
    # Obtener los números y el operador
    num1 = obtener_numero("Ingresa el primer número: ")
    num2 = obtener_numero("Ingresa el segundo número: ")
    operador = obtener_operador()

    try:
        # Ejecutar la operación correspondiente
        if operador == '+':
            resultado = operadores.suma(num1, num2)
        elif operador == '-':
            resultado = operadores.resta(num1, num2)
      

        print(f"El resultado de {num1} {operador} {num2} es: {resultado}")
   
    except ValueError as e:
        print(f"Error: {e}")
   
if __name__ == "__main__":
    main()
