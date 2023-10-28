#Contact Book
#Creating two empty lists of phone_number and name

names = []
phone_numbers = []
num = 5 #Maximum number of contacts we need

for i in range(num):
    #Taking user input as name and phone_number
    name = input("name: ")
    phone_number = input("phone_number: ")
    names.append(name)
    phone_numbers.append(phone_number)

#Print the format of Output
print("\nName\t\t\tPhone Number\n")

#Running for loop over the variable
for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

#Giving option for user to search
search_term = input("\nEnter Search Terms: ")
print("Search Result")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name {}, Phone Number: {}".format(search_term, phone_number))
else:
    print("Name Not Found")