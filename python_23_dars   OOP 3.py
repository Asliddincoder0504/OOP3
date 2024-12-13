# #Instance  method
# from sympy.physics.mechanics.joint import Joint
#
#
# class Student:
#     school_name='ABC  school'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     @classmethod
#     def change_school(cls,name):
#         print(Student.school_name)
#         Student.school_name=name
#
#
#     def show(self):
#         print(self.name,self.age, "School",Student.school_name)
# jessa=Student("Jessa",17)
# jessa.show()
# Student.change_school('XYZ school')
# jessa.show()



# from datetime import date
#
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#     @classmethod
#
#     def calculated_age(cls,name,birth_year):
#         return cls(name,date.today().year-birth_year)
#
#     def show(self):
#         print(self.name+"' s age is: "+str(self.age))
#
# jessa=Student("Jessa",21)
#
# jessa.show()
#
# joy=Student.calculated_age("Joy",1995)
# joy.show()

#
# class Employee:
#     @staticmethod
#     def sample(x):
#         print("Inside static method",x)
#
# Employee.sample(10)
#
# emp=Employee()
# emp.sample(10)


# class Employee:
#     def __init__(self,name,salary,project_name):
#         self.name=name
#         self.salary=salary
#         self.project_name=project_name
#
#     @staticmethod
#     def gather_requirement(project_name):
#         if project_name=='ABC project':
#             requirement=['task_1','task_2','task_3']
#         else:
#             requirement=['task_1']
#         return requirement
#
#
#     def work(self):
#         requirement=self.gather_requirement(self.project_name)
#         for task in requirement:
#             print('Completed',task)
#
# emp=Employee('Kelly',12000,"ABC project")
# emp.work()

#
# class Test:
#     @staticmethod
#
#     def static_method_1():
#         print('static methot 1')
#
#     @staticmethod
#     def static_method_2():
#         Test.static_method_1()
#
#     @classmethod
#
#     def class_method_1(cls):
#         cls.static_method_2()
#
# Test.class_method_1()


# Encapsulation
#
# class Employee:
#
#     def __init__(self,name,salary,project):
#         self.name=name
#         self.salary=salary
#         self.project=project
#     def show(self):
#         print("Name:",self.name,"Salary:",self.salary)
#
#     def work(self):
#
#         print(self.name,'is working on',self.project)
#
# emp=Employee('Jessa',15000,'NLP')
# emp.show()
#
#
# emp.work()



#1-masala.Create a class BankAccount with an attribute balance.
# Implement methods deposit, withdraw, and check_balance to deposit,
# withdraw, and check the balance of the bank account, respectively.

# class BankAkkaount:
#     def __init__(self,boshlangich_hisob=0):
#         self.hisob=boshlangich_hisob
#
#
#     def depozit(self,miqdori):
#         if miqdori>0:
#             self.hisob+=miqdori
#             print(f" Hisobingizga   {miqdori}  qo'shildi ")
#
#         else:
#             print("Balans manfiy yoki 0 bo'lishi mumkin  emas")
#
#     def pul_yechish(self,miqdori):
#         if miqdori>0:
#             if 0< miqdori <= self.hisob:
#                 self.hisob-=miqdori
#                 print(f"Hisobingizdan  {miqdori} chiqarildi. ")
#             elif miqdori > self.hisob:
#                 print("Mablag'ingiz yetarli emas")
#         else:
#             print("Yechib  olinadigan  pul miqdori musbat bo'lsin")
#
#     def hisob_cheki(self):
#
#         print(f"Hozirgi balans {self.hisob} so'm")
#         return self.hisob
#
# account=BankAkkaount(100000)
# account.hisob_cheki()
#
#
# account.depozit(20000)
#
# account.pul_yechish(50000)
#
# account.hisob_cheki()


#2-masala Create a class Rectangle with attributes length and width.
# Implement methods area, perimeter, and is_square to calculate the area,
# perimeter, and check if the rectangle is a square, respectively.

# class Restangle:
#
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#
#     def area(self):
#         return self.length*self.width
#
#     def peremetr(self):
#         return 2*(self.length+self.width)
#
#     def is_square(self):
#         return self.length==self.width
#
#
# rect1=Restangle(12,4)
# print(f"Yuzasi: {rect1.area()}")
# print(f"Peremetr: {rect1.peremetr()}")
# print(f"Kvadratmi: {rect1.is_square()}  bu kvadrat emas")
#
# rect2=Restangle(8,8)
# print(f"Yuzasi  {rect2.area} ")
# print(f"Peremetri  {rect2.peremetr()} ")
# print(f"Kvadratmi  {rect2.is_square()}  ha bu kvadrat ")


#3-masala. Create a class Student with attributes name, age, and grades.
# Implement methods add_grade, calculate_average, and print_summary to add a grade,
# calculate the average grade, and print the student's summary, respectively.

#
# class Student:
#     def __init__(self,name,age,baho):
#         self.name=name
#         self.age=age
#         self.grades=[]
#
#     def baho_qoshish(self,baho):
#         if 0<=baho<=100:
#             self.grades.append(baho)
#             print(f"{baho} baho qo'shildi")
#         else:
#             print("Baho  0 dan 100 gacha bo'lishi kerak")
#     def bahoni_hisoblash(self):
#         if self.grades:
#             return sum(self.grades)/len(self.grades)
#         else:
#             return 0
#     def chop_etish(self):
#         ortacha=self.bahoni_hisoblash()
#
#         print(f"Talaba: {self.name},Yoshi: {self.age},Ortacha baho : {ortacha:.2f}")
#
# student=Student("Asliddin",19,90)
#
# student.chop_etish()
# student.baho_qoshish(90)
# student.bahoni_hisoblash()
# student.chop_etish()



#4-masala..Create a class Circle with attribute radius.
# Implement methods area, circumference, and diameter to calculate the area,
# circumference, and diameter of the circle, respectively.

#
# import math
#
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def yuza(self):  # yuzani  hisoblash
#         return math.pi*(self.radius**2)
#
#     def aylana_uzunlik(self):  #aylana uzunligini  hisoblash
#         return 2*math.pi*self.radius
#
#     def diametr(self):    # aylana  diametrini hisoblash
#         return 2*self.radius
#
#
# radius=float(input("Radiusni kiriting="))
# aylana=Circle(radius)
#
# print(f" Doira yuzasi  {aylana.yuza():.2f}")
# print(f" Doira yuzasi  {aylana.diametr():.2f}")
# print(f" Doira yuzasi  {aylana.aylana_uzunlik():.2f}")



#5-masala..
"""Create a class Book with attributes title, author, and current_page.
Implement methods open, turn_page, and restart to open the book at a specific page,
turn the page, and restart the book at page 1, respectively."""
from numpy.ma.core import multiply
from sympy.physics.units import seconds, minutes

# class Book:
#     def __init__(self,title,author,current_page):
#         self.title=title
#         self.author=author
#         self.current_page=current_page
#
#     def open(self,page=1):
#         self.current_page=page
#         print(f"Kitob ochildi sahifa Sahifa: {self.title} , Muallif: {self.author}, Hozirgi sahifa: {self.current_page}")
#
#     def turn_page(self):
#         print(f" Siz {self.current_page} sahifadasiz")
#
#     def restart(self):
#         self.current_page=1
#         print("Siz birinchi sahifaga qaytdingiz")
#
# kitob=Book("GARRI POTER","MAYKL JEKSON",278)
# kitob.open(23)
# kitob.turn_page()
# kitob.restart()



#Class Method Tasks:


#6-masala..
"""Create a class Dog with a class-level attribute total_dogs
 and a method get_total_dogs that returns the number of dog instances created."""
#
# class Dog:
#     jami_itlar=0
#
#     def __init__(self,nomi):
#         self.nomi=nomi
#         Dog.jami_itlar+=1
#
#     @classmethod
#
#     def jami_kuchuklar(cls):
#         return cls.jami_itlar
#
# it_1=Dog("Reks")
# it_2=Dog("Bobik")
# it_3=Dog("Simba")
# print(f"Jami yaratilgan itlar soni: {Dog.jami_kuchuklar()}")



#7-masala..
"""Create a class Computer with class-level attributes
total_computers and computers_list.
Implement a method add_computer that adds a computer
instance to the list and updates the total_computers count."""

# class Kompyuter:
#     jami_kompyuterlar=0
#     kompyuterlar_royxati=[]
#
#     def __init__(self,brand,model):
#         self.model=model
#         self.brand=brand
#
#     @classmethod
#
#     def add_kompyuter(cls,kompyuter):
#         cls.kompyuterlar_royxati.append(kompyuter)
#         cls.jami_kompyuterlar+=1
#
#     @classmethod
#
#     def jami_kompyuter(cls):
#         return cls.kompyuterlar_royxati
#
#
#     @classmethod
#     def kompyuter_royxati(cls):
#         return cls.kompyuterlar_royxati
#
# kompyuter1=Kompyuter("HP","Victus")
# kompyuter2=Kompyuter("Asus","Nitro")
# kompyuter3=Kompyuter("Acer","Aspire")
#
#
# Kompyuter.add_kompyuter(kompyuter1)
# Kompyuter.add_kompyuter(kompyuter2)
# Kompyuter.add_kompyuter(kompyuter3)
#
# print("Kompyuterlar ro‘yxati:")
# for comp in Kompyuter.kompyuter_royxati():
#     print(f"Model: {comp.model}, Brand: {comp.brand}")

#8-masala
"""
 Create a class Employee with class-level attributes total_employees 
 and employees_list. Implement a method hire_employee that adds 
 an employee instance to the list and updates the total_employees count.
"""

# class Xodimlar:
#     jami_xodimlar = 0
#     xodimlar_royxati = []
#
#     def __init__(self, ism, familiya, lavozim, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.lavozim = lavozim
#         self.yosh = yosh
#
#     @classmethod
#     def employee(cls, xodim):
#         cls.xodimlar_royxati.append(xodim)
#         cls.jami_xodimlar += 1
#
#     @classmethod
#     def barcha_xodimlar(cls):
#         return cls.jami_xodimlar
#
#     @classmethod
#     def barcha_xodim_royxati(cls):
#         return cls.xodimlar_royxati
#
#
# xodim_1 = Xodimlar("Asliddin", "Norqobilov", "Programmist", 20)
# xodim_2 = Xodimlar("Farrux", "Jumayev", "Dekan", 35)
#
# Xodimlar.employee(xodim_1)
# Xodimlar.employee(xodim_2)
#
# print("Jami xodimlar soni:", Xodimlar.barcha_xodimlar())
#
# for xodim in Xodimlar.barcha_xodim_royxati():
#     print(f"{xodim.ism} {xodim.familiya} - {xodim.lavozim}, Yosh: {xodim.yosh}")



#9-masala..
""" 
Create a class Television with a class-level attribute
 average_screen_size and a method update_average_screen_size that
  updates the average screen size when a new television instance is created.
  """

#
# class Television:
#     ortacha_ekran_olchami = 0
#     full_ekran_olchami = 0
#     umumiy_televezor = 0
#
#     def __init__(self, ekran_olchami):
#         self.ekran_olchami = ekran_olchami
#         Television.update_ortacha_ekran_olchami(ekran_olchami)
#
#     @classmethod
#     def update_ortacha_ekran_olchami(cls, ekran_olchami):
#         cls.full_ekran_olchami += ekran_olchami
#         cls.umumiy_televezor += 1
#         cls.ortacha_ekran_olchami = cls.full_ekran_olchami / cls.umumiy_televezor
#
#     @classmethod
#     def ortacha_ekran_olchami_olish(cls):
#         return cls.ortacha_ekran_olchami
#
#
# televezor1 = Television(43)
# televezor2 = Television(32)
# televezor3 = Television(55)
#
# print(f"O'rtacha ekran o'lchami: {Television.ortacha_ekran_olchami_olish()} dyuym")

#10-masala..
""" Create a class Course with class-level attributes total_courses and courses_list.
 Implement a method add_course that adds a course instance to the list and updates the total_courses count.
"""

# class Course:
#     jami_kurslar=0
#     kurslar_royxati=[]
#
#     def __init__(self,kurs_nomi,kurs_vaqti):
#         self.kurs_nomi=kurs_nomi
#         self.kurs_vaqti=kurs_vaqti
#
#     @classmethod
#
#     def add_course(cls,kurs):
#         cls.kurslar_royxati.append(kurs)
#         cls.jami_kurslar+=1
#
#     @classmethod
#     def jami_kurslarni_olish(cls):
#         return cls.jami_kurslar
#
#     @classmethod
#     def kurslar_royxatini_olish(cls):
#         return cls.kurslar_royxati
#
# kurs1=Course("Backend","6 oy")
# kurs2=Course("Frontend","6 oy")
# kurs3=Course("FULLSTACK","12 oy")
#
#
# Course.add_course(kurs1)
# Course.add_course(kurs2)
# Course.add_course(kurs3)
#
# print(f"Jami kurslar soni: {Course.jami_kurslarni_olish()}")
#
# print("Kurslar ro'yxati:")
# for kurs in Course.kurslar_royxatini_olish():
#     print(f"{kurs.kurs_nomi} - {kurs.kurs_vaqti}")


#Static Method Tasks:


#11-masala..
"""
Create a class Math with a static method multiply that takes two numbers and returns their product.
"""


# class Math:
#     @staticmethod
#     def multiply(a,b):
#         return a*b
#
#
# a=6
# b=5
# natija=Math.multiply(a,b)
# print(f"{a}  va {b}  ning  mahsuloti  {natija}")



#12-masala..
"""
Create a class Temperature with a static method celsius_to_fahrenheit that converts a given Celsius temperature to Fahrenheit.
"""
# class Temperatura:
#     @staticmethod
#
#     def celsius_to_farangeyt(celsius):
#         return (celsius*9/5)+32
# celsius_temp=30
#
# farangeyt_temp=Temperatura.celsius_to_farangeyt(celsius_temp)
#
# print(f" {celsius_temp} gradus farangeytga  o'tkazilganda   {farangeyt_temp}  boladi")

#13-masala..
"""
Create a class Distance with a static method miles_to_kilometers that converts a given distance in miles to kilometers.
"""


# class Distance:
#     @staticmethod
#     def miles_to_kilometrs(miles):
#         return miles * 1.60934
# miles=10
#
# kilometrs_converter=Distance.miles_to_kilometrs(miles)
# print(f" {miles} mil = Kilometrs {kilometrs_converter}")


#14-masala..
"""Create a class Utility with a static method is_even that checks if a given number is even or not."""

# class Utilita:
#     @staticmethod
#     def is_even(number):
#         return number%2==0
#
# number1=16
# number2=9
#
# print(f" {number1} juftmi : Ha {Utilita.is_even(number1)} juft")
# print(f" {number2} juftmi : Ha {Utilita.is_even(number2)} toq")


#15-masala..
"""Create a class Time with a static method seconds_to_minutes that converts a given time in seconds to minutes and seconds (as a tuple)."""
class Time:
    @staticmethod
    def seconds_to_minutes(seconds):
        return seconds/60

seconds=120

minutes=Time.seconds_to_minutes(seconds)
print(f"{seconds} soniya = {minutes:.2f} daqiqa")

