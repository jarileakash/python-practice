
import logging
# Set up custom logging format
#logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - Line %(lineno)d - %(message)s', level=logging.DEBUG)


'''Q1. Define a variable of all the labours and print the name of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
    labour variable should be something like this 1st_labour, 2nd_labour and so on.  '''

s1_labour="Mahesh"
s2_labour="Mithilesh"
s3_labour="Ramesh"
s4_labour="Sumesh"
 
print(f"Labour names are:-{s1_labour}, {s2_labour} {s3_labour} {s4_labour}")

'''
Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
    labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,2nd_labour_wage and so on.
    You are bound to use string formatting
'''
s1_labour_name= "Mahesh"
s1_labour_wage= 500
s2_labour_name= "Mithilesh"
s2_labour_wage= 400
s3_labour_name= "Ramesh"
s3_labour_wage= 400
s4_labour_name= "Sumesh"
s4_labour_wage= 300
print(f"{s1_labour_name} salary is {s1_labour_wage}")
print(f"{s2_labour_name} salary is {s2_labour_wage}")
print(f"{s3_labour_name} salary is {s3_labour_wage}")
print(f"{s4_labour_name} salary is {s4_labour_wage}")

'''
Q3. I want to print this paragraph and its line number from which this paragraph is printing
    """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here."""
    Condition:- 
    You can't use triple quote.
    Triple quote at starting is also a part of paragraph. '''

text ="""  Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here."""

# Split the paragraph into lines and print each line with its line number
logging.info(text)




''' Q4. When do we get NameError?         '''

'''Q5. Python is a high level language. What does that mean by high level? '''

'''Q6. What is compiled and Inetrpreted language, list a few? : C is compiled and python is interpretor'''

'''Q7. Get all varibales address from RAM and you find if something is similar?   '''
print(f"Labour id and ram location :-{id(s1_labour)}, {id(s2_labour)} {id(s3_labour)} {id(s4_labour)}")


# Set up custom logging format
logging.info("This is an info message with a timestamp and level")
logging.info(f"{s1_labour}, {s2_labour}, {s3_labour} ,{s4_labour}")

###---------------------------------------------------------------------------------------------------------
''' Write a program that uses the str.format() method to display the following message:
The product is "Laptop"
The price is 1200                  '''

product="Laptop"
price =1200
print("The product is {} and the price is {}".format(product,price))
 
'''Q:Create a Python program that formats a string with your name and profession, and adds a new line and tab after each sentence using escape sequences.'''

name = "Alice"
profession = "Software Engineer"

print(f"my name is {name}.\n\tI im a {profession}")
