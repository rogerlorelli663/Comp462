
'''
Lab 1
Roger Lorelli 8/28/2021
'''

########## Part 1 ###########

'''
   1) Create a variable, x, and set its value to 16
      Create a variable, y, and set its value to square root of x
      Divide x by three fifths of y, and store the result in x (hint: /=)

'''
# YOUR CODE GOES HERE
import math
x = 16
y = math.sqrt(x)
x /= ((3 / 5) * y)

'''
    2)  A cube has the edge defined below.

    Store its space diagonal, surface area and volume in new variables.
    Print out the results and check your answers.
    Change the value of the edge and ensure the results are still correct.
'''
# YOUR CODE GOES HERE
edge = 10

space_diagonal = math.sqrt(pow(edge,2) * 3)
area = 6*pow(edge,2)
volume = pow(edge,3)

print(f"Edge: {edge}")
print(f"Space Diagonal: {space_diagonal}")
print(f"Surface Area: {area}")
print(f"Volume: {volume}")



######### Part 2 ###########

'''
    1)  For each of the following Python expressions, write down the output value. If it would give an error then write error.

                (a)False == 0
                
                (b) True != 1
                
                (c) 40 // 2
                
                (d) 41 // 2
                
                (e) 41 % 2
                
                (f) True + 1.33
                
                (g) False - `True'
                
                (h) False + \True"
                
                (i) 15/7+5*8**4
                
                (j) ('Hello' == 'Hi') or ( 12 > -6 )

'''
'''
# YOUR CODE GOES HERE
                (a) True
                (b) False
                (c) 20
                (d) 20
                (e) 1
                (f) 2.33
                (g) error
                (h) error
                (i) 20482.14285714286
                (j) True
                
'''





######### Part 3 ###########


'''
    1) write a python code to calculate the age based on the user's birthdate (the year of birth, e.g.: age = 1989), if age is greater than 18 then outputs “adults' category” otherwise outputs “Children Category”.

'''
# YOUR CODE GOES HERE
import datetime
year = 1989
current_year = datetime.datetime.now().date().year
age = current_year - year
if age > 18:
    print("Adults' Category")
else:
    print("Children Category")


'''
	2) Repeat q1:
    If the year is not within 1910-2020 then prints an error message for the user
    Otherwise: calculates his/her age, if age is greater than 18 then outputs “adults' category” otherwise outputs “Children Category”.

'''
# YOUR CODE GOES HERE

year1 = 1989
year2 = 1857

year = year1
# using current_year from previous question
if year < 1910 or year > 2020:
    print("Error, age is either too old or too young")
else:
    age = current_year - year
    if age > 18:
        print("Adults' Category")
    else:
        print("Children Category")
    
######### Part 4 ###########



'''
    1) Write a python code to print all the perfect square numbers less than 300.
'''
# YOUR CODE GOES HERE
for i in range(1,300):
    if math.sqrt(i) == int(math.sqrt(i)):
        print(i)



'''
    2) Write a python code to print all the perfect square numbers less than 300 and greater than 20 except for 100 and 121.
'''
# YOUR CODE GOES HERE
notequal = [100,121]
for i in range(21,300):
    if i not in notequal and math.sqrt(i) == int(math.sqrt(i)):
        print(i)


'''
    3) Write a python code to calculate 100*101*102...*200
'''
# YOUR CODE GOES HERE
start = 10
end = 20
iterative = 1
for i in range(start,end + 1):
    iterative *= i

answer = math.factorial(end) / math.factorial(start - 1)

print(f"Discrete:  {int(answer)}")
print(f"Iterative: {iterative}")
# Oddly enough, looks like there is a bit of error in the discrete answer when the ints get too big.
# tested on smaller ints and both work.

######### Part 5 ###########

'''
    1) Given a list of values: x = [1,'ok',3, 17.01, True]
    Write a code to print the last element of it
'''
# YOUR CODE GOES HERE
x = [1,'ok',3, 17.01, True]
print(x[-1])

'''   2) Given a list of integers: e.g.: [1,2,3,2,0]
        (a) return the average
        (b) return the list resulted from adding up each number with its index. e.g.: output:[1,3,5,5,4]
        (c) given another list, return their common elements. e.g.: SecondList = [1; 1; 2; 2; 2; 2; 4; 6; 7; 88; 8], output :[1,2]
      
        
'''
  # YOUR CODE GOES HERE
def S5Q2(list1, list2):
    length = len(list1)
    sum = 0
    for i in list1:
        sum += i
    # (a)
    avg = sum / length

    # (b)
    y = []
    for i in range(0, length):
        y.append(list1[i] + i)

    # (c)
    if len(list2) > 0:
        intersection = []
        for i in list1:
            if i in list2 and i not in intersection:
                intersection.append(i)

        return avg, y, intersection

    else:
        return avg, y

######### Part 6 ###########

'''
    1)  Write a function to find the even numbers in the list and return a list of those numbers:
        e.g.: list1 = [9,-6, 0, 7, 1, 5, 6, 8]-->[-6, 0, 6, 8]
'''

# YOUR CODE GOES HERE
def evens(list1):
    even = []
    for i in list1:
        if i % 2 == 0:
            even.append(i)
    print(even)
    return even

'''
    2)  Write a function to find the odd numbers in the list and return a list of their indices: e.g.: list1 = [9,-6, 0, 7, 1, 5, 6, 8] --> [0,3,4,5]
'''
# YOUR CODE GOES HERE
def odd_index(list1):
    length = len(list1)
    odd_indices = []
    for i in range(0,length):
        if list1[i] % 2 != 0:
            odd_indices.append(i)
    print(odd_indices)
    return odd_indices

######### Part 7 ###########

'''
    1) Write a function to get a message as an input and to replace all instances of ‘o’ with ’a’ and to return the updated message.
'''

# YOUR CODE GOES HERE
def replaceOA():
    message = input("Please enter a message: ")
    print("Replacing all instances of the letter 'o' with the letter 'a'.\n")
    new_message = message.replace('o','a')
    print(new_message)
    return new_message

######### Part 8 ###########
'''
    1) Write a function to drop the duplications in a list of numbers.
    (Hint: use dictionary)  e.g.: 
    Input_list = [11,2,3,8,0,11,4,2,2,7,0]-->[11,2,3,8,0,4,7]

'''
# YOUR CODE GOES HERE
def duplication_counter(list1):
    counter = {}
    length = len(list1)
    for i in range(length):
        if list1[i] not in counter.keys():
            counter.update({list1[i]:1})
        else:
            counter[list1[i]] += 1
    return list(counter.keys())

######### Part 9 ###########
'''
    1) Write a function to get the radius of a circle and to return its area. (import pi and exponentiation from math module)
    
'''    
# YOUR CODE GOES HERE
from math import pi, pow
def area_of_circle():
    radius = float(input("Please Enter the radius of a circle: "))
    area = pi * pow(radius,2)
    return area

######### Part 10 ###########  
'''
   1) Write a python function to find the frequency of the characters in a sentence.
(Hint : Use a dictionary)

e.g.:  ‘Hhellloo’   -->  {‘H’:1 , ‘h’: 1, ‘e’:1, ‘l’:3 , ‘o’:2}
    
'''  
# YOUR CODE GOES HERE
def frequency_counter(sentence):
    counter = {}
    length = len(sentence)
    for i in range(length):
        if sentence[i] not in counter.keys():
            counter.update({sentence[i]:1})
        else:
            counter[sentence[i]] += 1
    return counter