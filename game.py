from random import choice, randrange
from datetime import datetime
import operator
# Operadores posibles
operators = ["+", "-", "*", "/"]

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}   

a = 0 
b = 0

# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")
    
    op_char = operator
    result1 = ops[op_char](number_1,number_2)
    print (result1)

    if float(result) == float(result1):
        print ("Correcto!")
        a += 1
    else:
        print ("incorrecto")
        b += 1
# Al terminar toda la cantidad de cuentas por resolver.
print (a,b)
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print("Tuviste ", a , " aciertos y ", b, "resultados incorrectos")