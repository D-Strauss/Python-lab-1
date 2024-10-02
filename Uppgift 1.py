# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:48:44 2024

@author: Dahni Strauss
"""
#Uppgift 1: Skriv ett program som emot en sträng som input och skriver ut längden på strängen. Exempel-input: "thisIsAString" Förväntad output: 13
x = input("Enter a string")
print(len(x))

#--------------------------------------------------------------------------------------------------------------
#Uppgift 2 Skriv ett program som skriver ut frekvensen av tecken i en given sträng. Exempel-input: "banana" Förväntad output: {"b":1, "a":3, "n":2}
x = input("Enter a string and i will count the frequency of the letters")
dict = {} 

for i in x:
    if i in dict:
        dict[i] += 1
        
    else:
        dict[i] = 1 

print(dict)

#--------------------------------------------------------------------------------------------------------------
#Uppgift 3
#Skriv ett program som för en given sträng skriver ut de två första och de två sista tecknen i strängen (på valfritt format) Exempel-input: "banana" Förväntad output: "ba na"
x = input("Enter a string")

substring1 = x[0:2]
substring2 = x[-2:]
print(substring1,substring2)

#--------------------------------------------------------------------------------------------------------------
#Uppgift 4
#Skriv ett program som tar två strängar som input och skapar EN ny sträng där de två
#första tecken i varje sträng bytts ut. Exempel-input: "abc", "xyz" Förväntad output: "xyc abz"
input1 = input("Enter the first string")
input2 = input("Enter the second string") 

#Extracting the letters of each input and the rests
input1_first = input1[:2]
input2_first = input2[:2]
input1_rest = input1[2:]
input2_rest = input2[2:]

# Replaces the strings
input_new = input1_first + input2_rest
input_new2 = input2_first + input1_rest

# Final merge
input_final = input_new + "" + input_new2
print(input_final)

#--------------------------------------------------------------------------------------------------------------
#Uppgift 5
#Skriv ett program som lägger till "ing" i slutet av en given sträng, om strängen är kortare än 3 tecken ska den lämnas ofärndrad. Expempel-input: "Python" Förväntad output: "Pythoning"
x = input("Enter a string")
if len(x) <3:
    print(x)
    
else:
        print(x + "ing")
        
#--------------------------------------------------------------------------------------------------------------
#Uppgift 6
#Skriv ett program som först tar bort all whitespace (mellanslag, tab (\t), newline(\n)), och sedan även tar bort alla tecken på ojämna indexvärden, från given sträng. Exempel-input: "a string with spaces and a newline character\n" Förväntad output: "atigihpcsnaelncaatr"
x = input("Enter a string: ")

# Remove Whitespaces
x = x.replace(" ", "")
print("String with no whitespaces:", x)

# Convert string to a list and filter in one step
filtered_list = [char for index, char in enumerate(x) if index % 2 == 0]

print("String with all whitespaces removed and every uneven index removed:", ''.join(filtered_list))

# Uppgift 7
#Skriv ett program som tar en komma-separerad sekvens av ord och skriver ut de unika orden i alfabetisk ordning. Exempel-input: "red, white, black, red, green, black" Förväntad output: "black, green, red, white"
Wordsequence = ["green", "blue", "red", "black", "blue"]
Wordsequence.sort()
WS_set = set(Wordsequence)
print(WS_set)

# Uppgift 8
# Skriv en funktion som konverterar en given sträng till versaler (uppercase) om den innehåller minst 2 versaler bland de 4 första tecknen.
Word = input("Enter a string")
if Word[:4].isupper():
    print(Word.upper())
else: 
    print("nothing")

# Uppgift 9
# Skriv en funktion som vänder (reverse) på en sträng om dess längd är en multipel av 4.
Word = input("Enter a string")
if len(Word) % 4==0:
    print(Word[::-1])
else:
    print(Word)
    
    #Uppgift 10
#Skriv en funktion som skapar en ny sträng bestående av 4 kopior av de två sista tecken i en given sträng. Exempel-input: "Python" Förväntad output: "onononon"
Word = "Python"

print(Word[-2:]*4)

#Uppgift 11
#Skriv en funktion som tar emot en lista med ord och returnerar det längsta ordet samt dess längd

Wordlist = ["Apple", "Banana", "Cucumber"]
Word_count = len(Wordlist)
longest_word = max(Wordlist, key=len)
print(f"The number of words in the list is: {Word_count}", "The word with the greatest number of letter is", longest_word)

# Uppgift 12
#Skriv ett program som genererar en enkel multiplikationsmodell för tal 1-10. Hur snyggt kan du få tabellen? Läs på om sträng-formattering i Python.

multiplication = int(input("Enter a number between one to ten"))
multiplication = multiplication * multiplication
print(multiplication)

number = 0
counter = 0
while counter <10:
    number =  (counter +1) **2
    counter = counter+1
    print(number)

#Uppgift 13
#Skriv en funktion som beräknar fakulteten av ett givet tal
import math
number = int(input("enter a number"))
result = math.factorial(number)
print(result)

#Uppgift 14
#Skapa ett enkelt gissningsspel där datorn väljer ett slumpmässigt tal mellan 1-100 
#(eller annat intervall), och låt användaren gissa tills de hittar rätt nummer. För varje felaktig gissning berättar datorn om det rätta svaret är högre eller lägre än spelarens gissning.
## Create a variable with an integer input
## generate a fixed number for each game
## compare the integer of the user with the fixed number
## If its not the correct number, tell the user if the number is higher or lower.
import random
counter = 0
Correct_number = random.randrange(1,100)

while counter == 0: 
    User_input = int(input("Welcome to this number guessing game, enter a number between 1-100"))
    if User_input == Correct_number:
        print("Congratulations, you entered the right number!!")
        counter = counter+1
        
    else:
        if User_input < Correct_number:
            print("The number is higher than you entered")
        elif User_input > Correct_number:
            print("the number is lower than you entered")
        
#Uppgift 15
#Skriv ett program som kontrollerar om ett givet ord är ett palindrom (läses likadant framifrån som bakifrån).
Word = input("Enter a word, and see if its identical backwards")
Word_rev = Word[::-1]
print(Word_rev)
if Word == Word_rev:
    print("Yes the word is a palindrom")
else:
    print("The word is not a palindrome")
    
#Uppgift 16
#Skriv ett python program som itererar mellan 1 och 50,
#om talet är delbart med 3 printar den "fizz"
#om talet är delbart med 5 printar den "buzz",
#om talet är delbart med både 3 och 5 så printar den "FizzBuzz"
#annars printar den bara ut talet

def func():
    number = random.randrange(1,50)
    if number%3==0:
        print("fizz")
    else:
        print(number)
    if number%5==0:
        print("buzz")
    else:
        print(number)
    if number%5==0 and number%3==0:
        print("FizzBuzz")
    else:
        print(number)
func()