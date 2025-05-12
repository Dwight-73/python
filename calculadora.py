def calcular(num1, operador, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                return "Error: División por cero"
            return num1 / num2
        elif operador == '**':
            return num1 ** num2
        elif operador == '%':
            return num1 % num2
        elif operador == '//':
            if num2 == 0:
                return "Error: División por cero"
            return num1 // num2
        else:
            return "Operador no válido"
    except ValueError:
        return "Error: Ingresa números válidos"

def main():
    print("Calculadora Básica")
    print("Operadores disponibles: +, -, *, /, ** (potencia), % (módulo), // (división entera)")

    while True:
        num1 = input("Ingresa el primer número (o 'salir' para terminar): ")
        if num1.lower() == 'salir':
            break

        operador = input("Ingresa el operador: ")
        num2 = input("Ingresa el segundo número: ")

        resultado = calcular(num1, operador, num2)
        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    main()
