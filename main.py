import random
list1 = []
list2 = [] 

list3 = []
for i in range(15):
    list1.append(random.randint(1,10))
    list2.append(random.randint(1,10))
for  i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
    print(list1,list2,list3)



for i in list1:
    if i not in list3:
        list3.append(i)   
for i in list2:
    if i not in list3:
        list3.append(i)   
print(list1,list2)
             

for i in range(len(list1)):
    for i in range(len(list2)):
        if list1[i] == list2[i]:   

         for i in range(len(list3)):
                if list1[i] == list3[i]:
                    break
         else:
                list.append(list1[i])
        break  
print(list1,list2,list3)



min  = list1[0]
max = list1[0]
for i in range(len(list1)):
    if list1[i] < min:
        min = list1[i]
    if list1[i] > max:
        max = list1[i]  
min1  = list2[0]
max1 = list2[0]
for i in range(len(list1)):
    if list2[i] < min1:
        min1 = list2[i]
    if list2[i] > max1:
        max1 = list2[i]
list3 =[min,max,min1,max1]
print(list1,list2,list3)                   

