"""
#1 print
print("Hello World!")

#2 variables math
x=5
y=10
print(x*y)

#3 double variables
x="Sally"
x=5
print(x)

#4 print multiple variables in one line
x="Sally"
y=5
print(x,y)

#5 creating list 
a,b,c,d= ["hyppo", "lion", "zebra", "penguin"]

print("ANIMALS : ...")
print(a)
print(b)
print(c)
print(d)

#6 unpacking list
Animals = ["hyppo", "lion", "zebra", "penguin"]
a,b,c,d = Animals
print("ANIMALS : ...")
print(a)
print(b)
print(c)
print(d)

#7 Global variable inside function
x="Fantastic"
y="Something"
def Personality():
    print("Laiba is", x)
Personality()

#7.1 Global variable outside function
x="Sunny"

def Weather():
    x="Rainy"
    print("Today is:",x)
Weather()

print("and not:",x)

#8 random number generator
print("YOU DICED : ...")
import random 
print(random.randrange(1,6))

"""

#9 multiple strings like in poetry 
a= """ 
-- Sono una creature --

Come questa pietra 
e' il mio pianto
che non si vede
La morte
si sconta
vivendo.


    -Giuseppe Ungaretti 
print(a)
"""
"""
#9 select letter from string (array) starting position 0, space included
a="Hello, World!"
print(a[7])

#10 a for loop that prints all char in a string
for a in "BANANA":
    print(a)

          #OR, MY VERSION :

message="YOU MUST BREAK THE PATTERN OR THE LOOP WILL REPEAT TOMORROW"
for x in (message):
        print(x) 

#11 string length spaces get counted
message="YOU MUST BREAK THE PATTERN OR THE LOOP WILL REPEAT TOMORROW"
print(len(message))

a="LOOP"
for x in (a):
    print(x)

#12 checking word in a phrase 
txt="what about the parmesan cheese?"
if "cheese" in txt:
    print("Yes, cheese in present in the text")

#13 check if word not in a phrase
txt="--> I LIKE: Pepe's chicken rice with garlic mayo"
print(txt)
if "rubicon" not in txt:
    print("--> OH WAIT... You forgot to add rubicon!!!") 

#14 INPUTS!! calculate age by birth_year 
Birth_year = int(input("Enter Birth Year--> "))
age = (2026 - Birth_year)
print("Your age is --> ", age)

#15 INPUT for BMI and range
height = float(input("Insert height (2 d.p.) --> "))
weight = float(input("Insert weight (kg) --> "))

double_height= float(height * 2)
bmi = round(weight / double_height)
print("BMI --> " , bmi)

if bmi < 18.5:
    print("BMI range--> UNDERWEIGHT")

elif bmi >= 18.5 and bmi <=24.9:
    print("BMI range --> HEALTHY WEIGHT")

elif bmi >= 25.0 and bmi <= 29.9:
    print("BMI range --> OVERWEIGHT")

elif bmi >= 30.0:
    print("BMI range --> OBESE")

else:
    print("InHuMaN BoDy MaSs")
    

#16 Input matheMATIC PROBLEMS avg result of grade
grade1 = float(input("INSERT 1st GRADE --> "))
grade2 = float(input("INSERT 2nd GRADE --> "))
grade3 = float(input("INSERT 3rd GRADE --> "))
avg = round((grade1 + grade2 + grade3) / 3)
print("YOUR FINAL GRADE IS -----> ", avg)

#18 Method functions
course = "Python for beginners"
print (course.upper())
print(course)
print (course.find ("for"))
print(course.replace("for" , "4"))
print("Python" in course)

temp = 25                    #ordine operativo DALL'ALTO VERSO IL BASSO
if temp > 30:                #PRIMA 30, POI 20 --> RISULTATO = 222222
    print("111111")          #25 è > pure di 10 ma stampa solo 1 risultato (ELIF)

elif temp > 20:
    print("2222222")

elif temp > 10:
    print("333333")

else:
    print("Done")
    

#17 Input concatenation age and name 
age = str(input("INSERT AGE--> "))
name = str(input("INSERT NAME--> "))
info = "My name is " + name + ", and i'm " + age
print(info)

format = str(input("Select weight format (kg) or (lbs) --> "))
weight = int(input("Insert weight --> "))
if format == "kg":
    lbs = round(weight / 0.45)
    print("Your weight in Lbs is : ", lbs)

else:
    kg = round(weight * 0.45)
    print("Your weight in Kg is : ", kg)
    
# While loop
i = 1
while i<=7 :
    print(i * "*")
    i = i + 1
  
i = 1
while i <= 5:
    print (i )
    i+=1

#print  range of numbers / from / stop / step /
numbers = range(-2, 10, 2)
for num in numbers:
    print(num)
    

#format string f --> to combine strings with variables in print
first_name = "Cherry"
food = "ramen"
email = "supergalattica123@gmail.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is --> {email}")

#float number f-string
price = 10.99
print(f"This item costs £{price}")

#boolean 
is_student = False
if is_student:
    print("You are a student")
else: 
    print("You are NOT a student")
"""