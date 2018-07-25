#7-1---------------------------------------------------------------------------

rental_car = input("What type of car are you interested in renting? ")

available_cars = ['subaru', 'toyota','chevy','ford']

if rental_car in available_cars:
    print("\nNo problem, we definitely have a " + rental_car.title() +
          " in our garage")
else:
    print("\nSorry, we do not have a " + rental_car.title() + 
          " in our garage, " + "is there any other car you are interested in?")
#7-2---------------------------------------------------------------------------

restaurant_seating = input("Hi, how many people are in your dinner group? ")
restaurant_seating = int(restaurant_seating)

if restaurant_seating > 10:
    print("\nSorry, you will have to wait for a table.")
else:
    print("\nWonderfuly, please follow me this way.")
#7-3---------------------------------------------------------------------------

number = input("Please enter a number: ")
number = int(number)

if number %10 == 0:
    print("The number " + str(number) + " is multiple of 10")
else:
    print("The number " + str(number) + " is not multiple of 10")
#7-4---------------------------------------------------------------------------

order = "\nWhat pizza toppings would you like?            "
order += "\nEnter 'quit' when you are done with your order.         "

topping = True

while True:
    toppings = input(order)
    
    if toppings == 'quit':
        break
    else:
        print("We will add " + toppings.title() + "'s to your pizza, " +
              "is there anything else you want to add?")
#7-5---------------------------------------------------------------------------

prompt = "\nHi, welcome to Cineplex, how old are you?      "
prompt += "\nplease enter 'quit' when you are done         "
prompt = int(input(prompt))



if prompt < 3:
    print("Your ticket is free :)")
elif prompt < 12:
    print("Your ticket is $10")
elif prompt > 12:
    print("Your ticket is $15")
#7-8---------------------------------------------------------------------------

sandwich_orders = ['salami', 'pastrami', 'turkey', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    complete_sandwiches = sandwich_orders.pop()
   
    print("Your " + complete_sandwiches.title() + " sandwich is ready!")
    finished_sandwiches.append(complete_sandwiches)
    
print("\nThe following sandwiches have been made: ")
#7-9---------------------------------------------------------------------------
sandwich_orders = ['pastrami', 'salami', 'pastrami', 'turkey', 'cheese', 
                   'pastrami']

print("Sorry, the deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
        
print("\nThe finished sandwiches are: ")
for grub in sandwich_orders:
    print(grub.title())
for done in finished_sandwiches:
    print(done.title())
#7-10--------------------------------------------------------------------------

dream_vacation = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would" +
                  " you go? ")
    
    dream_vacation[name] = place
    
    repeat = input("Would someone else like to respond to the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, place in dream_vacation.items():
    print(name.title() + " would love to visit " + place.title())