num = 7
num1 = 8
num2 = 77

if num >= num1 and num >= num2:
    print("el numero "+str(num) + " es el mayor")

elif num1 >= num and num1 >= num2:
    """el elif se puede usar cuantas veces quieras"""

    print("el numero " + str(num1) + " es el mayor")
else:
    print("el numero "+str(num2) + " es el mayor")