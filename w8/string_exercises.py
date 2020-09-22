#kelly jaramillo, 9-21-2020 fcc python class learnTogether Week 8 learn together code, step 1
# we have to do 10 string problems.  I am pulling them from 
# https://pynative.com/python-string-exercise/

import re

#Exercise Question 1:
# Given a string of odd length greater 7, return a string made of the middle three chars of a given String
mystr = "JhonDipPeta"
mystrlen = len(mystr)
mystrlen = int(mystrlen / 2)
print(mystrlen)
theanswer = mystr[mystrlen-1:mystrlen+2]
print(theanswer)

#Exercise Question 3: 
# Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string
s1 = "America"
s2 = "Japan"
mystr = s1[0]+s2[0]+s1[int(len(s1)/2)]+s2[int(len(s2)/2)]+s1[-1]+s2[-1]
print(mystr)

#Exercise Question 5: 
# Count all lower case, upper case, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
charcnt = 0
uppercnt = 0
lowercnt = 0
digcnt = 0
speccnt =0
for i in range(0,len(str1)):
    if str1[i].isupper():
        uppercnt = uppercnt+1
        charcnt = charcnt+1
    elif str1[i].islower():
        lowercnt = lowercnt+1
        charcnt = charcnt+1
    elif str1[i].isnumeric():
        digcnt = digcnt+1
    else:
        speccnt = speccnt+1
    
dbstr = "char {0} upper {1} lower {2} digit {3} special {4}".format(str(charcnt),str(uppercnt),str(lowercnt),str(digcnt),str(speccnt))
print(str(dbstr))

#Exercise Question 7: String characters balance Test
#We’ll say that a String s1 and s2 is balanced if all 
# the chars in the s1 are there in s2. characters position doesn’t matter.
#Googled Find

s1 = "YnX"
s2 = "PYnative"
mystr = "True"
for i in range(0,len(s1)):
    if (s2.find(s1[i])<0):
        mystr = "False"
print(mystr)

# Exercise Question 9: 
# Given a string, return the sum and average of the digits that appear in the string, 
# ignoring all other characters
str1 = "English = 78 Science = 83 Math = 68 History = 65"
str1_split = str1.split(" ")
strsum = 0
stravg = 0
strcnt = 0
for i in range(0,len(str1_split)):
    try:
        tmpnum = int(str1_split[i])
        strsum +=tmpnum
        strcnt+=1
    except Exception as ex:
        continue
stravg = strsum/strcnt

print("Sum is {0} Avg is {1}".format(str(strsum),str(stravg)))


#Exercise Question 11: Reverse a given string
#googled the slice, thought there was a reverse method.
str1 = "PYnative"
print(str1[::-1])


# Exercise Question 13: 
# Split a given string on hyphens into several substrings and display each substring

str1 = "Emma-is-a-data-scientist"
str1_split = str1.split("-")
for i in range(0,len(str1_split)):
    print(str1_split[i])


# Exercise Question 15: 
# Remove special symbols/Punctuation from a given string
#googled regular expression method.

str1 = "/*Jon is @developer & musician"
newstr1 = re.sub("[^a-z,A-Z,' ']","",str1)
print(newstr1)


# Exercise Question 17: 
# Find words with both alphabets and numbers
#googled global flag for reg ex
str1 = "Emma25 is Data scientist50 and AI Expert"
str1_split = str1.split(" ")
print(str1_split)
for i in range(0,len(str1_split)):
     if (re.findall("[/a-z,A-Z/g]",str1_split[i]) and re.findall("[/0-9/g]",str1_split[i])):
        print(str1_split[i])



