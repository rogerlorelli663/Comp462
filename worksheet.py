# import math
# notequal = [100,121]
# for i in range(21,300):
#     if i not in notequal and math.sqrt(i) == int(math.sqrt(i)):
#         print(i)
#
#
#
#
# start = 10
# end = 200
# iterative = 1
# for i in range(start,end + 1):
#     iterative *= i
#
# answer = math.factorial(end) / math.factorial(start - 1)
#
# print(f"Discrete:  {int(answer)}")
# print(f"Iterative: {iterative}")

# x = [1,'ok',3, 17.01, True]
# print(x[-1])


# x = [1,2,3,2,0]
# length = len(x)
# SecondList = [1, 1, 2, 2, 2, 2, 4, 6, 7, 88, 8]
# sum = 0
# for i in x:
#     sum += i
# avg = sum / length
# # (a)
# print(avg)
#
#
# # (b)
# y = []
# for i in range(0,length):
#     y.append(x[i] + i)
# print(y)
#
# # (c)
# intersection = []
# for i in x:
#     if i in SecondList and i not in intersection:
#         intersection.append(i)
# print(intersection)

# list1 = [9,-6, 0, 7, 1, 5, 6, 8]
# evens = []
# for i in list1:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)

# list1 = [9,-6, 0, 7, 1, 5, 6, 8]
# length = len(list1)
# odd_indices = []
# for i in range(0,length):
#     if list1[i] % 2 != 0:
#         odd_indices.append(i)
# print(odd_indices)

# message = input("Please enter a message: ")
# print("Replacing all instances of the letter 'o' with the letter 'a'.\n")
# new_message = message.replace('o','a')
# print(new_message)


# def S5Q2(list1, list2):
#     length = len(list1)
#     sum = 0
#     for i in list1:
#         sum += i
#     # (a)
#     avg = sum / length
#
#     # (b)
#     y = []
#     for i in range(0, length):
#         y.append(list1[i] + i)
#
#     # (c)
#     if len(list2) > 0:
#         intersection = []
#         for i in list1:
#             if i in list2 and i not in intersection:
#                 intersection.append(i)
#
#         return avg, y, intersection
#
#     else:
#         return avg, y
def frequency_counter(sentence):
    counter = {}
    length = len(sentence)
    for i in range(length):
        if sentence[i] not in counter.keys():
            counter.update({sentence[i]:1})
        else:
            counter[sentence[i]] += 1
    return counter


input1 = input("Please enter a message: ")
dups = frequency_counter(input1)

print(dups)