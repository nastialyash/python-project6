def dobNum(list):
    dob = 1
    for i in list:
        dob *= i
        return dob
list = [1,2,3,4,5] 
result = dobNum(list)   
print(result)


def minNum(numbers):
   min = numbers[0]
   for i in numbers:
       if i < min:
           min = i
   return min
numbers = [1,2,5,4,8,0,2]
result = minNum(numbers)
print(result)





def delNum(a,number):
    count = 0
    for i in a:
        count += 1
        return count
result = [2,3,4,5,1,4,1,7,8,1]
number = 1
count = delNum(result,number)
print(count)
print(f"New list: {result}")    


       






def listNum(list1,list2):
    return list1+list2
list1 = [1,3,5]
list2 = [3,6,1]
list3 = listNum(list1,list2)
print(list3)



                                       
