print("------Mathematical Operations-----")

print("Addition: ",(2+3))
print("Subtraction: ",(22-10))
print("Multiplication: ",(4*5))
print("Division: ",(50/5))
print("Floor Division:",(30//10))
print("Exponentiation:",(4**2))
print("Modulo Division:",(5%2))
print("Expression 1:",(8+2*3))
print("Expression 2:",((8+2)*3))    # Using PEMDAS Rule

print("--------String Operations---------")

print("Shreya Sinha Roy") # Using Double Quotes
print('West Bengal')   # Using Single Quotes
print("SSR's Laptop")
print('"Dell" and "HP"')
print("SSR\'s 'Laptop'")
print("Tuk " * 10)
print(r"C:\docs\new")  # r means raw string. The string will be printed as it is
# it will ignore the special meaning of '\n' which is new line.

print("--------Built-in Functions-------")
print(abs(-32))
print(abs(+32))
print(type(2))
print(type(2.8))
print(type("SSR"))

print("-------Variables in Python------")
x = 2
y = 3
print("Old: ",(x+y))
y = 7
print("New: ",(x+y))
name = "YOUTUBE"
print(name)
print(name + " rocks")
print(name[3:10])
# name[0:3] = "My" this will not work
print('my ' + name[3:])
print(len("Shreya"))
