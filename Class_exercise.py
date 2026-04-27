#create a function and list out the items in the list 
class subFieldsinAI():
    def subfields(self) :
        subFieldsList=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub fields in AI are :")
        for fields in subFieldsList:
            print(fields)

#Create a function that checks whether the given number is odd or even
class oddEven():
    def oddEven(self):
        num=int(input("Enter a number : ")) 
        if (num%2 == 0) : 
           print(num, "is even number")
        else : 
           print(num, "is odd number") 

#Create a function that tells eligibility of marriage for male and female according to their age limit 
#like 21 for male and 18 for female
class eligible():
     def eligible(self):
        gender = input("Enter your gender :")
        age = int(input("Enter your age :"))
        if (gender == "male") :
           if (age >= 21) : 
               print("Eligible")
           else: 
               print("Not Eligible")
        elif (gender == "female") :
           if (age >= 18) : 
               print("Eligible")
           else: 
               print("Not Eligible")

#Find percentage of 10th mark
class percentage():
    def percentage(self):
        subjects = ["English","Tamil","Mathematics","Science","Social Science"]
        total = 0 
        for sub in subjects :
            print("Enter your marks in ",sub, ":")
            marks = int(input())
            total = total + marks
        print("Percentage in tenth : ", total/5)

#print area and perimeter of triangle using functions
class area_triangle():
    def area_triangle(self) :
        h1 = int(input("Enter height of the triangle  1:"))
        b1 = int(input("Enter breadth of the triangle 1:"))
        area = (h1 * b1 )/2
        h3 = int(input("Enter height 1 of the triangle 2 :"))
        h4 = int(input("Enter height 2 of the triangle 2 :"))
        b2 = int(input("Enter breadth of the triangle 2 :"))
        perimeter = h3 + h4 + b2 
        print("The area of first triangle is : ",area)
        print("The perimeter of second triangle is : ", perimeter)  
