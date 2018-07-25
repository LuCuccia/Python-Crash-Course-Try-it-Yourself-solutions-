#try it yourself 6-2
fav_numbers = {
        'luca':'82',
        'kimiya':'16',
        'mark':'23',
        'alex':'55',
        'anthony':'97',
        'james':'23',
        }

for key, value in fav_numbers.items():
    print('\n' + key.title() + "'s favorite number is " + value)
    #you do not need to use the variables key and value--------------
    #This would work just as well:
    #for name, language in fav_numbers.items():
        #print(G.title() + "'s favorite number is " + hello)
print('\n')
friends = ['luca', 'kimiya', 'katrina', 'erin']
for key in fav_numbers:
    if key in friends:
        print("Hey " + key.title() + ", I see your favorite number is " + value)
if 'erin' not in fav_numbers.keys():
        print("Erin, please take the poll!")
    #example of a way to see what is and is not in your dictionary

#how to get your keys in order... sort through your loop
print('\n')
for key in sorted(fav_numbers.keys()):
    print(key.title() + ', thanks for taking the poll')

print('\n')
#to list only values    
print("The following numbers have been chosen:")
for value in fav_numbers.values():
    print(value)
    
#to list only values without repeats  

print("\nThe following numbers have been chosen (without repeats):")
for value in set(fav_numbers.values()):
    print(value)

#try it yourself 6-4

rivers = {
        'nile':'egypt',
        'hudson':'new_york',
        'st.lawrence':'montreal',
        }
print('\n')
for water, place in rivers.items():
    print('The ' + water.title() + ' runs through ' + place.title())

#try it yourself 6-7 (people)
luca = {
        'first_name':'luca',
        'last_name':'cuccia',
        'age':'21',
        'city':'new_york',
        }

kimiya = {
        'first_name':'kimiya',
        'last_name':'adjedani',
        'age':'21',
        'city':'toronto',
        }

sofia = {
        'first_name':'sofia',
        'last_name':'cuccia',
        'age':'18',
        'city':'new_york',
        }

people = [luca, kimiya, sofia]

for info in people:
    print(info)

#try it yourself 6-9 (people)

favorite_places = {
        'luca':['jamaica','italy','thailand'],
        'sofia':['italy','france','uk'],
        'kimiya':['iran','greece','turkey']
        }

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are:")
    for place in places:
        print('\t' + place.title())
    print('\n')

#try it yourself 6-11 (cities)
cities = {
       'bangkok':{
               'country':'thailand',
               'population':'32,000',
               'fact':'There are a lot of ladyboys'
               }, 
       'montreal':{
               'country':'canada',
               'population':'45,000',
               'fact':'Justin Trudeau is the PM'
               },
       'austin':{
               'country':'usa',
               'population':'50,000',
               'fact':"It's weird"
               },
        }
       
for city, info in cities.items():
    print(city.title() + " facts include:")
    country = info['country']
    population = info['population']
    fact = info['fact']
    
    if country == 'usa':
        print('\t Country: ' + country.upper())
        print('\t Population: ' + population.title())
        print('\t Fact: ' + fact)
    else:
        print('\t Country: ' + country.title())
        print('\t Population: ' + population.title())
        print('\t Fact: ' + fact)
    print('\n')