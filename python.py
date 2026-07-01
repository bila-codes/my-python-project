
 a=12
 name="bilal"
 a=12.5

# for i in range(5):
#    print(i)
# i=1
# while i<=20:
#     print(i)
#     i += 1
# name=input("enter name")
# print("Name:",name)
# for i in range(1,10,2):
#     print(i)
# name=["bilal","ali","sikander"]
# for name in range(0,1):
#     print(name)
# for i in range(len(name)):
#     print(i,name[i])

# for i in range(10):

#     if i == 5:
#        break
#     print(i)

# for i in range(10):
   
#     if i == 2:
#        continue
#     print(i)
    
# for i in range(5):
#     for j in range(10):
#         print(i,j)

# num=int(input("enter number"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)
# def Bilal():
#    name="bilal"
#    print(name)

# Bilal()
# def hasssan(name):
#     print("name",name)

# hasssan("umar")   
    

# def add(a, b):
#     return a + b

# result = add(3, 4)
# print(result)
# def table(num):
#     for i in range(1, 11):
#         print(num, "*", i, "=", num * i)

# table(5)

# name=[1,3,2]
# name.remove(2)
# print(name)
# num=[1,4,5]
# # for i in num:
# #     print(num)
# print(len(num))
# print(max(num))
# print(min(num))
# hasssan ={
#     "value":10,
#     "name":"bilal"
# }
# hasssan["city"]=("lahore")

# print(hasssan)
# print(hasssan["value"])
# numbers = [10, 20, 30, 40]

# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[-1])
# marks = {}
# x = int(input("Enter marks: "))
# marks.update({"Bilal": x})
# print(marks)
# list1=[1,2,3]
# list2=list1.copy()
# print(list1,list2)
# text = "ali loves python  "

# print("UPPER:", text.upper())
# print("LOWER:", text.lower())
# print("CAPITALIZE:", text.capitalize())
# print("STRIP:", text.strip())
# print("REPLACE:", text.replace("python", "Java"))
# print("FIND:", text.find("l"))
# print("COUNT:", text.count("o"))
# list1={1,2,3}
# list1.add(4)
# print(list1)

# def count(n):
#     if n == 0:
#         return
#     print(n)
#     count(n-1)

# count(3)

# class student:
#     def __init__(bilal,name,age):
#         bilal.name=age
#         bilal.age=name

# s1=student("bilal","ali")    
# print(s1.name)
# print(s1.age)
# import array

# a = array.array('i', [1, 2, 3, 4])

# print(a)
# import math
# print(math.sqrt(16))
# import time

# print("Hello")
# time.sleep(2)
# print("World")
# f = open("data.txt", "w")
# f.write("Hello World")
# f.close()
# f = open("data.txt", "r")
# print(f.read())
# f.close()
# import json

# data = {
#     "name": "Ali",
#     "age": 20,
#     "city": "Lahore"
# }

# f = open("data.json", "w")
# json.dump(data, f)
# f.close()
# import csv

# STEP 1: CSV me data likhna
# f = open("data.csv", "w", newline="")
# writer = csv.writer(f)

# writer.writerow(["name", "age", "city"])
# writer.writerow(["Ali", 20, "Lahore"])
# writer.writerow(["Ahmed", 25, "Karachi"])

# f.close()


# # STEP 2: CSV read karna
# f = open("data.csv", "r")
# reader = csv.reader(f)

# for row in reader:
#     print(row)

# # f.close()
# F=open("data.txt","w")
# F.write("hELLO WORLD")
# F.close()

# import json
# Data={
#     "Name":"Bilal",
#     "Age":20
# }
# f = open("Data.json","w")
# json.dump(Data,f)

# f=open("DATA.json","r")
# print(f.read())
# f.close()
# class Student:
#     def __init__(self,age):
#         self.__age = age

# s1 = Student(21)
# print(s1._Student__age)   
def set_age(self, age):
    self.__age = age