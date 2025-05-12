🧮 Calculadora en Python
Esta es una calculadora de consola hecha en Python. Permite realizar operaciones con todo tipo de números (enteros, decimales, negativos) y soporta múltiples operadores: suma, resta, multiplicación, división, potencia, módulo y división entera.

🚀 ¿Cómo usar esta calculadora?
1. Ejecuta el programa
Asegúrate de tener Python instalado. Luego, abre una terminal y ejecuta el archivo .py con este comando:

bash
Copiar
Editar
python calculadora.py
2. Sigue las instrucciones
Verás un mensaje como este:

less
Copiar
Editar
Calculadora Básica
Operadores disponibles: +, -, *, /, ** (potencia), % (módulo), // (división entera)
Luego, ingresa:

El primer número

El operador (ej: +, -, **, etc.)

El segundo número

El programa calculará y mostrará el resultado. Puedes seguir usando la calculadora hasta que escribas salir.

🔧 ¿Qué hace cada parte del código?
📌 1. Función calcular()
python
Copiar
Editar
def calcular(num1, operador, num2):
Recibe dos números y un operador. Convierte los números a tipo float para permitir decimales.

Dentro de la función, se usa una serie de condiciones (if, elif) para determinar qué operación hacer.

Por ejemplo:

python
Copiar
Editar
if operador == '+':
    return num1 + num2
También verifica errores como división por cero o entradas inválidas.

📌 2. Función main()
python
Copiar
Editar
def main():
Es la parte que interactúa con el usuario. Muestra las instrucciones, pide los datos y llama a la función calcular().

Contiene un bucle while que sigue corriendo hasta que el usuario escriba "salir".

📌 3. Código principal
python
Copiar
Editar
if __name__ == "__main__":
    main()
Este bloque hace que la función main() se ejecute solo si estás ejecutando el archivo directamente (no si lo importas desde otro archivo).

✅ Operadores disponibles
Operador	Función	Ejemplo	Resultado
+	Suma	5 + 3	8
-	Resta	10 - 4	6
*	Multiplicación	6 * 7	42
/	División	8 / 2	4.0
**	Potenciación	2 ** 3	8
%	Módulo (residuo)	10 % 3	1
//	División entera (sin decimales)	10 // 3	3

💡 Notas importantes
Acepta números negativos y decimales.

Maneja errores como división entre cero o texto no válido.

Es una buena base para hacer una calculadora más avanzada (con interfaz gráfica, historial, etc.).
