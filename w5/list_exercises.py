#kelly jaramillo, 8-31-2020 fcc python class learnTogether Week 5 learn together code, step 1
#this will solve the problems found on https://holypython.com/beginner-python-exercises/exercise-6-python-lists/
#there are 14 problems that we will be solving.

#Exercise 6-a: Calling Elements of a Python List (Index 0)
lst=[11, 100, 99, 1000, 999]
answer_1=lst[0]
print(answer_1)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-b: Calling List Elements and Indexing
lst=[11, 100, 101, 999, 1001]
print(lst[1])

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-c: Calling List Elements (Negative Index)
lst=[11, 100, 101, 999, 1001]
#Type your answer here.

answer_1=lst[-1]

print(answer_1)
#I was able to solve without any hints/google/stackOverflow

#Exercise 6-d: Append method to add items to the end of Python Lists
lgift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.

gift_list.append("pajamas")

print(gift_list)
#I was able to solve without any hints/google/stackOverflow

#Exercise 6-e: List inside List (Python Nested Data)

gift_list=['socks', '4K drone', 'wine', 'jam',["socks", "tshirt", "pajamas"]]

print(gift_list)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-f: Insert method to add to a specified index of a Python List
gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.insert(2,"slippers")


print(gift_list)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-g: Index method to get the index of a List Item

lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.


answer_1=lst.index(8679)
print(answer_1)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-h: Adding a different type of element to a List using Append
lst=[55, 777, 6, 76, 99]
#  Type your code here.
lst.append("Navigator")
print(lst)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-i: Removing the last item of a list (.remove() method)

lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.

lst.remove(99)

print(lst)


#I had to use a hint.  I thought the parameter was the index of what I wanted to remove, not the value

#Exercise 6-j: Reversing a Python list (.reverse() method)

lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.
lst.reverse()
print(lst)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-k: Count Method to get the amount of an item in a list

lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#  Type your code inside print() function.

answer_1=lst.count(6)

print(answer_1)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-l: Adding up all the items in a List w/ Sum Function

lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1=sum(lst)

print(answer_1)

#I had to use google find the method I wanted 

#Exercise 6-m: Max Function to Get the Lowest Value in a List
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1=min(lst)

print(answer_1)

#I was able to solve without any hints/google/stackOverflow

#Exercise 6-n: Max Function to Get the Highest Value in a List
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1=max(lst)

print(answer_1)

#I was able to solve without any hints/google/stackOverflow

