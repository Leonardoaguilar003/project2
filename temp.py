import math 

people = int(input("Enter the amount of people attending: "))
hotdogs_per_person = int(input("Enter how many hotdogs each person will recieve: "))

total_hotdogs = people * hotdogs_per_person
total_buns = total_hotdogs

hot_dog_packs_required = math.ceil(total_hotdogs / 10)
hot_dog_buns_required = math.ceil(total_buns / 8)

hot_dogs_leftover = total_hotdogs % 10 
hot_dog_buns_leftover = total_buns % 8


print("The number of hotdog packages required are", hot_dog_packs_required)
print("The number of bun packs required are", hot_dog_buns_required)
print("There are", hot_dogs_leftover, "hotdogs left over." )
print("There are", hot_dog_buns_leftover, "hotdog buns left over.")
