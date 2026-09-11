# class is blueprint which has collection of attributes and methods and does not have physical enity its just logical enity.
#object is physical entity and has memory location, object is instance of class each object gets its own set of attributes and function from the class

#different between function and method is that when we write the function inisde class its called method

#creating class and object

# class Myclass:
#     def myfuc(self):
#         pass
#     def myfucn(name):
#         print(name)

# mc1= Myclass()
# mc1.myfuc()
# mc1.myfucn("shreya")   # it will access its own method not class     

# mc2=Myclass()
# mc2.myfuc()
# mc2.myfucn("john") 

#static method -- self inside the static method is just a paramater name, it does not refer to object

# class Myclass:
#      def myfun(self):
#          print("instace method")
#      @staticmethod
#      def myfunc(num):
#          print(num)

# # mc1=Myclass()

# # # invoking directly using onject
# # mc1.myfun() #instance method
# # mc1.myfunc(6) #static method


# Myclass.myfun() #gives type error bcs class thinks myfun as static method and considers self as parameter 
# Myclass.myfunc(3) #static method can be directly accessed using class

# class variables -- variables called inside class are called object .need to use self keyword we use variable 

# class Myclass():
#     a,b=10,20
#     def add_num(self):
#         print(self.a+self.b)
#     def mul_num(self):
#         print(self.a*self.b)

# mc=Myclass()
# mc.add_num()
# mc.mul_num()

#global variables, local variables, class variables

# x,y=100,200 #global variable
# class Myclass():
#     a,b=10,20 #class variable
#     def add_num(self):
#         i,j=2,6 #local variable
#         print(self.a+self.b)
#         print(i+j)
#         print(x+y)
#     def mul_num(self):
#         print(self.a*self.b)

# mc=Myclass()
# mc.add_num()
# mc.mul_num()


# same variables name

# a,b=10,20 #global variable
# class Myclass():
#       a,b=100,200 #class variable
#       def add_num(self,a,b): #local variable
#             print(self.a + self.b)
#             print(a+b)
#             print(globals()['a']+globals()['b'])
# mc=Myclass()            
# mc.add_num(4,2)


#constructor
#in python we should __init__(self) to call constructor
#constructor is used to initlize the data
#constructor invoked automatically when object is created.
#only on constructor is enough in one class

# class Myclass:
#     def __init__(self):
#         print("This is constructor..")
#     def m1(self):
#         print("hello")
#     def m2(self,a,b):
#         return a+b 
# mc=Myclass()
# mc.m1()
# print(mc.m2(2,4))          


#Constructor with parameters and class varaibles

# class Myclass():
#     name="shreya" #class varibale
#     def __init__(self,name):
#         print(name) #print local variable 
#         print(self.name) #prints class variable

# m=Myclass("danaraddi")



# class Myclass():
#     a,b=2,8
#     def __init__(self,name):
#         print("hello",name)
#     def m1(self):
#         print(self.a+self.b)  

# m=Myclass("shreya")      # print the hello shreya as contructor intizase the data
# m.m1()        #prints m1 method print statemt


# class with constructor and method

class Employee():
    def __init__(self,empid, empname,empsal):
        self.empid=empid    #created class variable inisde constutor
        self.empname=empname
        self.empsal=empsal
    def display(self):
        print(self.empid,self.empname,self.empsal)    #calling the class variable inside the method

emp1=Employee(100,"shreya",60000) #While creating object need to pass the data 
emp1.display()

emp2=Employee(101,"john",40000)
emp2.display()         