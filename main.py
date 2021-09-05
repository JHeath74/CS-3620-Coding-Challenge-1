print("Job 1 - Calculate simple interest")

p=input('Enter a value for your Principal: ')

n=input('Enter a Number for Years for Loan: ')

r=input('Enter the Interest Rate: ')

p=int(p)
r=int(r)
n=int(n)
a=(p*r*n)/100
int(a)

print(a)

print("Job 2 - Create a list of your favorite food items")

myList = ["Watermelon", "Raspberries", "Beef Jerky", "Orange Creamsicles", "Strawberries"]

print(myList[2])

myList.append("Orange Juice")
myList.append("Pog Juice")

print(myList)

myList.insert(2,"Tacos")

print(myList)

print("Job 3 - Part 1")

text = "I am a programmer"

for x in range(5):
  print(text)

print("Job 3 - Part 1")

def math_function():
  l = list()
  for i in range(1, 10):
    l.append(i ** 2)
  print(l)

math_function()