
length_of_land = 100
breadth_of_land = 100
bricks_Cost_per_price = 10.5
labour_mistri1 = "Jagmohan"
is_land = True


if length_of_land == 100:
    length_of_land = 200
else:
    length_of_land == 300

#print(length_of_land,bricks_Cost_per_price,labour_mistri1,labour_mistri1)
#print('length of land is ',length_of_land)
#print('breadth of land is ',breadth_of_land)
#print("my home is of 4bhk \n length of total land is 100 ")
#print('''my home is of 4bhk 
#length of total land is 100 ''')

print("my home is of \t\"4bhk\"  ")
print("my home is of \t \"4bhk\"  manish  ")

#string formating 
print('length of total land is ',length_of_land)
print(f"cost of bricks per unit is {bricks_Cost_per_price}")
print(f"cost of bricks per unit is {bricks_Cost_per_price} {bricks_Cost_per_price} {length_of_land}")

#.format
print("cost of bricks per unit is {}".format(bricks_Cost_per_price))
#print("cost of bricks per unit is {} {} {}".format(bricks_Cost_per_price,length_of_land,breadth_of_land))