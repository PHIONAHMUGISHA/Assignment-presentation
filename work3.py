#loops
# Basic: Write a python program that prints all even numbers between 1 and 20 using a for loop.
for num in range(1,21,2):
    if num % 2== 0:
        print()

#qn2
# Intermidiate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
num = 0
while num <= 10:
      number =int(input("Enter a number greater than 10:"))
print(f"You entered {number},which is greater than 10")

#qn3
#Advanced: Write a program that prints the multiplication table (from 1 to 10)for numbers from 1 to 5 using the nested for loops 
print(f"Multiplication table for{1}:")
for j in range(1, 11): #inner loops for 1 to 5
    print(f"{1}" x {j} = {i * j})
    print()

#qn4
#Challange : Given a list intergers [4, 7, 2, 9, 12, 15],write a program using
#  a for loop to find the sum of all odd numbers and print the results.
odd_sum = 0
for number in number:
    if number % 2 !=0:
        odd_sum += number
print(f"sum of odd numbers:{odd_sum}")

#lists
#qn1 basic:
#Create a list of 5 fruits and print each fruit on a new line using a for loop
fruits =['apple','orange','grapes','maize','lemon']
for fruit in fruits:
    print(fruit)
#qn2
#intermediate:
#Wwrite a function that takes a list of numbers and returns a list with each number squared.
#example:[1,2,3,] should become [1,4,9].
numbers = [2,4,6,4,3,2,4]
squared = []
for num in numbers:
    squared.append(**2)
    print(squared)
#qn3
#Advanced: Write a python program that takes two lists,
#list1 = [1,2,3] and list2 = [4,5,6] and combines them into a single list,
#combined =[1,4,2,5,3,6].
list1 = [1,2,3]
list2 = [4,5,6]
combined_lists = list1 + list2
print(combined_lists)
#qn4
#Challange:Given a list of numbers,[3,1,4,1,5,9,2],
#Write a program to find and print the two largest numbers in the list without using the max()function
numbers = [3,1,4,1.5,9,2]
larget = float('-inf')
second_largest = float('-info') #iterate through the list
for number in numbers:
    if numbers >larget:
        second_largest = larget
        largest = number
    elif number > second_largest and number 1 = largest:
        second_largest = number
print("The largest number is:", largest)
print("The second largest number is", second_largest)

#Dictionaries:
#Basic: Create a dictionary with three key_value pairs representing a students information:
#name, age, and grade.print each key_value pair on a new line.
student_info = {"Name":"Arinda","Age":40,"Grade":"3rd"}
for key,value in student_info.items():#completed
    print(key,value)

#intermidiate:Write afunction that takes a dictionary of peoples names and thier ages,
#{'Alice': 24, 'Bob': 19, 'Charlie': 30},
#and returns a list of names of people who are 21 or older.
def select_adults(people):
    return [name for name,age,in people,items() if age > = 21 ]
    people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
print(select_adults(people))

#Advanced: Given a dictionary representing items in a store with their prices,{"Aplle": 0.5, "Banana":0.3,"Orange": 0.7}
#Write a program that takes a list of items bought, ["Apple","Banana","Bnanana"],and calculate the total cost
def calculate_tatal_cost(prices,items_bought):
    total_cost =sum(prices[item] for item in items_bought)
    print(total_cost)

    store = {"Apple": 0.5,"Banana": 0.3, "Orange": 0.7}
    items_bought = ["Apple","Orange","Banana","Banana"]
    print(calculate_tatal_cost(store,items_bought))

# challenge: write a program that counts the occurences of each word in a given sentence.
#example:For the sentence"hello world hello",the output should be {"hello": 2,"world": 1}.
def word_count(sentence):
    words = sentence.split()
    return {word:words.count(word) for word in set (words)}
    sentence = "hello world hello"
    print(word_count(sentence))












