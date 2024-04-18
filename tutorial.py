import pdb; pdb.set_trace()

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

print("Operaciones.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
  
op = input("Seleccione una operacion (1/2/3/4): ")

if op in ('1', '2', '3', '4'):
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
else:
    print("Entrada incorrecta. Ingrese un numero del 1 al 4.")

if op == '1':
            print(num1, "+", num2, "=", suma(num1, num2))

elif op == '2':
            print(num1, "-", num2, "=", resta(num1, num2))

elif op == '3':
            print(num1, "*", num2, "=", mult(num1, num2))

elif op == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        