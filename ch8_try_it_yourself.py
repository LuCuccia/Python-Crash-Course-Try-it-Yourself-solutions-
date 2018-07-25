#8-1---------------------------------------------------------------------------
def display_message(user):
    """Display a message to the user"""
    print("Hello " + user.title() + ", today we will be learning about functions")
    
display_message('luca')

#8-3/4-------------------------------------------------------------------------
def make_shirt(text='I love python', size='large'):
    """Tell user the size and text of the shirt they are ordering"""
    print('\nThank you for ordering a ' + size + " shirt with " 
          + text + " written on it.")

make_shirt(size='medium',text='G')
make_shirt()

#8-5---------------------------------------------------------------------------
def describe_city(city, country='Italy'):
    """Output a city name and the country it is in"""
    print(city.title() + " is in " + country.title())
    
describe_city('milan')
describe_city('palermo')
describe_city('fez', 'morocco')
describe_city(country='turkey', city='istanbul')

#8-7----------------------------------------------------------------------------

def make_album(artist, album, tracks = "unknown"):
    """make a dictionary of artists and their albums"""
    info = {'musician':artist, 'work':album}
    if tracks:
        info = {'musician':artist, 'work':album, 'number_of_tracks':tracks}
    return info

music = make_album('tyler the creator', 'flower boy')
print(music)

music = make_album('anderson paak', 'malibu', '12')
print(music)

music = make_album('herbie hancock', 'thrust')
print(music)

#8-8----------------------------------------------------------------------------

def make_album(artist, album, track = "unknown"):
    """make a dictionary of artists and their albums"""
    info = {'musician':artist, 'work':album}
    if tracks:
        info = {'musician':artist, 'work':album, 'number_of_tracks':track}
    return info

while True:
    print("(Please enter 'q' at any time to quit)")
    
    artists = input("What is the artist's name? ")
    if artists == 'q':
        break
    
    albums = input("What is the name of the album? ")
    if albums == 'q':
        break
    
    tracks = input("Do you know the number of tracks on the album? ")
    if tracks == '':
        artist_discography = make_album(artists, albums)
        print(artist_discography)


    else:
        artist_discography = make_album(artists, albums, tracks)
        print(artist_discography)


      
#8-9---------------------------------------------------------------------------

magician_names = ['luca', 'sofia',
'kimiya']
show_magicians= []

def show_magicians(magicians):
    """Print a list of magicians"""
    for magician in magicians:
        print(magician.title())



show_magicians(magician_names)


#8-10--------------------------------------------------------------------------


def show_magicians(magicians):
    """Print a list of magicians"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians= ['luca', 'kimiya', 'sofia']

print("Original list:")
show_magicians(magicians)

make_great(magicians)

print("\n")
print("New list:")
show_magicians(magicians)

#8-11--------------------------------------------------------------------------

def show_magicians(magicians):
    """Print a list of magicians"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)
        
    return magicians


magicians= ['luca', 'kimiya', 'sofia']


print("New list:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
#here the modified list is saved in another list, rather than modifying the 
#original

print("\n")
print("Original list:")
show_magicians(magicians)


#8-12--------------------------------------------------------------------------

def make_sandwich(*toppings):
    """Print the list of ingredients going into a sandwich"""
    print("Here are the ingredients going into your sandwich:")
    
    for yum in toppings:
        print("-" + yum.title())
        
make_sandwich('turkey', 'lettuce','honey mustard')

#8-13--------------------------------------------------------------------------

def build_profile(first, last, **user_info):
    """Build a dictionary a users info"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('luca', 'cuccia', location ='montreal',
                             field='pharmacology', favorite_color='blue')

print(user_profile)

#8-14--------------------------------------------------------------------------

def car_profile(manufacturer, model_name,**more_info):
    """print a profile for a car you want to sell"""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model_name'] = model_name
    
    for key, value in more_info.items():
        profile[key] = value
    return profile
        
build_profile = car_profile('pagani', 'huayra', price = '$1,000,000+',
                            very_nice = True)

print(build_profile)

















