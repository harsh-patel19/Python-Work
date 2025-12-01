# Q1*

# if it,s hot..
#     it's a hot day
#     drink plenty of water
# otherwisw if it's cold
#     it's a clod day 
#     wear warm clothes
# otherwise
#     it's a lovely day 


# is_hot = False
# is_cold =True

# if is_hot:
#     print("it's a hot day")
#     print("drnik plenty of water")
# elif is_cold:
#     print("it's a clod play")
#     print("wear warm clothes")
# else:
#     print("it's lovely day")

# Q2*

# price of a house is 1$m.
# if buyer has good credit,
#     they need to put down 10%
# otherwise
#     they need to put down 20%
# print the down payment


# has_good_credit = True
# has_crimial_record = False

# if has_good_credit and not has_crimial_record:
#     print("Eligible for loan")



# price = 10000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"down_payment: ${down_payment}")





# Q3* 

# # if temperature is greater than 30
#     it's a hot day 
# otherwise if it's less than 10
#     it's a cold day
# otherwise
#     it's neither hot nor cold



temperature = 35

if temperature <= 35:
    print("It's a hot day")
elif temperature <=10:
    print("It's cold day")
else:
    print("not hot and cold weather")

#Q4*

# if name is less than 3 characters long 
#     name must be at least 3 characters
# otherwise if it's mpre than 50 characters long
#     name can be a maximum of 50 characters
# otherwise
#     name looks good! 

# name = "Harsh"
# if (len(name)) <3:
#     print("name must be at least 3 character")
# elif len(name) >50:
#     print("name must be at least 50 character")
# else:
#     print("name looks good!")


# weight = int(input("weight: "))
# unit = input("(L)bs or (K)g: ")


# if unit.upper() == "L":
#     converted = weight *0.45
#     print(f"you are{converted} kilos")
# else:
#       converted = weight / 0.45
#       print(f"you are {converted} pounds")

# ****  WHILE LOOP ****

# i = 1
# while i <= 5:
#     print("*" *i)
#     i = i + 1
# print("Done..")


# start - to start the car 
# stop - to stop the Car 
# qit - to exit

# asd>
# i don't understand that..

# start>
# car started...ready to go!

# stop >
# car stopped

# command =""
# while True:
# # while command != "quit":
#     command = input(">").lower()
#     if command == "start":
#         print("car started...")
#     elif command == "stop":
#         print("car stopped.")
#     elif command == "help":
#         print("""
#             start - to start the car
#             stop - to stop the car
#             quit - to quit 
#               """)
#     elif command =="quit":
#         break
#     else:
#         print("sorry, i don't understand that!")

# ****  FOR LOOP  ****

# for item in 'python':
#     print(item)

# for item in ['Harsh','Dhruvika','Patel','Chauhan']:
#     print(item)

# for item in range(1,10,2):
#     print(item)

# prices = [10,20,30]
# total = 0

# total = 0
# for price in prices:
#     total +=  price
# print(f"total: {total}")


# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
    

# $$$$$
# $$
# $$$$$
# $$
# $$

# numbers = [5,2,5,2,]
# for x_count in numbers:
#     print('x'*x_count)

# numbers  =[5,2,5,2,2,]
# for x_count in numbers:
#     output =''
#     for count in range (x_count):
#         output += 'x'
#     print(output)


# ******************* LIST******************


# name =["Harsh","Patel","Mary","john"]
# print(name[1])