from random import randint 

#lesson 1-11

#lab_5 q4

number=input("choose a number: ")
int_number=int(number)

if "7" in number or int_number%7==0:
    print("boom")
    
#lab_5 q5  

three_numbers=input("write 3 numbers (separated by space): ")
three_numbers=three_numbers.split()

numbers_list=[]
for i in three_numbers:
    num=int(i)
    numbers_list.append(num)
    
max_number=max(numbers_list)
print("the biggest number is:", max_number)

#lab_11 q6 (without bonus)

random_number = randint(1, 100)
#print (random_number)
user_number=0
while user_number!=random_number:
    user_number=int(input("try guessing a number from 1 to 100: "))
    if user_number> random_number:
        print("to big, try again")
    elif user_number< random_number:
        print("to small, try again")
    else:
      print("you are correct!")  
      
#lab_11 q2
try:
    age=input("how old are you in years: ")
    age=float(age)
    age_months=age*12
    print("you are ",age_months, "months old")
except ValueError:
    print("write your age in numbers")
    age=input("how old are you in years: ")
    age=float(age)
    age_months=age*12
    print("you are ",age_months, "months old")

