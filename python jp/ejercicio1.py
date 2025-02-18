def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

# Solicitar entrada del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Ejecutar funciones
print(f"Suma: {suma(num1, num2)}")
print(f"Resta: {resta(num1, num2)}")
print(f"Multiplicación: {multiplicacion(num1, num2)}")
print(f"Division: {division(num1, num2)}")