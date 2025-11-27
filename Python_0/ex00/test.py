

# def my_function(name, age):
#     print("Hello", {name}, {age})



# name = "Ismael"
# age = 21
# print(f"Je m'appelle {name} et j'ai {age} ans")

# text = "Hello"
# print(text[0])      # H
# print(text[1:4])    # ell
# print(text[3])

# hi = "          hi   hi    ".strip()
# print(f"{hi}")

# hello = "hello world".split()
# print(f"{hello, hello[1]}")

# join = " ".join(["a", "b", "c"])
# print(f"{join}")


# my_function(name, age)


# numbers = [4, 21 , 89]
# numbers.append(5)

# for i, n in enumerate(numbers, start=1):
# 	print(f"index : [{i}] number: {n}")



# person = {"name": "Ismael", "age": 21}
# for key, value in person.items():
# 	print(f"{key} : {value}")


# print(person)

#exo A
string1 = "Bob"
string2 = "Jojo"

string3 = string1 + string2
print(string3[0:3])
print(len(string3))

#exo B
name = input("Nom : ")
print(f"Bonjour {name}, enchanté !")

#exo C
numbers = [1, 2, 3, 4]
numbers.append(5)
numbers.remove(2)
for n in numbers:
	print(n)

#exo D
dic = {"name": "Ismael", "language": "Python"}
print(f"Je m'appelle {dic['name']} et je code en {dic['language']}")


#exo E
def transform(s) -> str:
	return (s.swapcase().replace(" ", ""))

s = "Hello World"
print(transform(s))
