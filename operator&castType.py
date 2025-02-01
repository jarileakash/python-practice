from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_Cost_per_price = 10.5
labour_mistri1 = "Jagmohan"
is_land = True

#calculate the total area of land
total_area_of_land = length_of_land * breadth_of_land
perimeter_of_land= 2 * (length_of_land + breadth_of_land)

logger.info(f" total area of land is {total_area_of_land} sq ft")
logger.info(f" perimeter of land is {perimeter_of_land} sq ft")

#modulo operator
print(15%6)    # 6 two sa 12 and 3 is remainder  ,armstrong number % modulo operator getting used for armsrong number
               #modules will give reminder values

#Floor Division
print(15//6)               #----->2.5---> 2 floor lower value from 2.5 (down)
print(math.ceil(15/6))     # ciel  2.5----->  above value of 2 that is 3

#contact
a="20"
b=35
#print(a+b)
print(int(a)+b)
print(a+str(b))

length_of_land = float(input("please entr the length of land: "))
breadth_of_land = float(input("please entr the breadth of land: "))
logger.info(f"{type(length_of_land)}")

#total_area_of_your_land= length_of_land * breadth_of_land
total_area_of_your_land= abs(length_of_land * breadth_of_land)   # will round of - value to give postitve value

logger.info(f" total area of your land is {total_area_of_your_land} sq ft")