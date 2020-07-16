def user_name(f_name,l_name,m_name=''):
    full_name=f_name+m_name+l_name
    print(full_name)
    
    
def area_of_circle(radius):
    '''This function accepts only one parameter that is radius of circle anf output its area'''
    pi=3.142
    area=pi*(radius)**2
    return area


def build_person(f_name,l_name):
    person={'first name':f_name,'last name':l_name}
    return person



def describe_pet(pet_name,animal_type='cat'):
    print('I have a',animal_type)
    print('The name of my pet is',pet_name)
    
    
def make_pizza(size,*toppings):
    print('The size of my pizza should be',size)
    print('Toppings:',toppings)
    
    
    
def now_say_it(value):
    print(value)
    
def say_something():
    what_to_say = "Hi"
    now_say_it(what_to_say)
    
    
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)