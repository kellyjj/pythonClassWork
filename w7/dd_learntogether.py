#kelly jaramillo, 9-16-2020 fcc python class learnTogether Week 7 learn together code, step 1
#we will be working wiht data dictionaries for a real life case.  
# we need to do the following

#     add a key to a dd
#     sort (ascending or descending) 
#         I know Al didn't cover sorting, so check out this site, (Links to an external site.) also sort might be more helpful in the list of dd below.  
#     check whether a given key already exists in a dd
#     iterate over dd using for loops
#     filter a dd based on values
#     take your dd and create a list of dd
#     iterate over the list of dd and output summary data (total, average, min, max etc)
#
#   for my dictionary, I will be using some data elements from water hydrants.  
#   this properties will be unitID,  date installed, cap color,model number


import datetime

wtrHydrants = [{"unitid":"hyd1","dateinstalled":"09/01/2019","numInspection":1, "capcolor":"blue"}]

print(wtrHydrants)

print(" ")
print("adding a key to the dictionary")
print(" ")
wtrHydrants[0]["modelnumber"]="1919"
print(wtrHydrants)

print(" ")
print("adding records so that we can sort them by install date")
print(" ")
wtrHydrants.append({"unitid":"hyd2","dateinstalled":"09/01/2020", "numInspection":1,"capcolor":"red","modelnumber":"1919"})

wtrHydrants.append({"unitid":"hyd3","dateinstalled":"09/01/2018", "numInspection":5,"capcolor":"yello","modelnumber":"1919"})

print(" ")
print("do the sort.  should be hyd3, hyd1, hyd2")
print(" ")
wtrHydrants = sorted(wtrHydrants,key= lambda x:x['dateinstalled'])

print(wtrHydrants)

print(" ")
print("check if a key is in my dictionary")
print(" ")
for i in range(len(wtrHydrants)):
    if ("manufactor" in wtrHydrants[i]):
        print("We Have  Key of manufactor")
    else:
        print("we have no key")

print(" ")
print("interate through the individual dictionaries")
print(" ")
#
for i in range(len(wtrHydrants)):
    for a , value in wtrHydrants[i].items():
        print(a+" "+str(value))

print(" ")
print("Filter out red cap colors")
print(" ")
newHydList = []
for i in range(len(wtrHydrants)):
    if (wtrHydrants[i]["capcolor"]!="red"):
        newHydList.append(wtrHydrants[i])

print(newHydList)

print(" ")
print("Sum of number of Inspections ")
print(" ")
suminsp = 0

for i in range(len(wtrHydrants)):
    try:
        temp = int(wtrHydrants[i]["numInspection"])
    except Exception as ex:
        temp = 0
    suminsp+=temp

print("num of insp "+str(suminsp))

print(" ")
print("Avg of Inspections ")
print(" ")
suminsp = 0

for i in range(len(wtrHydrants)):
    try:
        temp = int(wtrHydrants[i]["numInspection"])
    except Exception as ex:
        temp = 0
    suminsp+=temp

avginsp = suminsp / len(wtrHydrants)

print("avg of insp "+str(avginsp))


print(" ")
print("Hydrant with largest Inspection count ")
print(" ")
suminsp = 0
maxdict = {}
for i in range(len(wtrHydrants)):
    try:
        temp = int(wtrHydrants[i]["numInspection"])
    except Exception as ex:
        temp = 0
    if (temp >suminsp):
        suminsp = temp
        maxdict = wtrHydrants[i]


print("max of insp "+str(maxdict))


