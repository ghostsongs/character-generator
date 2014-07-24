from random import choice, randint

#Physical traits
EYE_COLOUR = ['Blue', 'Green', 'Brown', 'Hazel', 'Grey']
HAIR_COLOUR = ['Blonde', 'Brunette', 'Ginger', 'Auban', 'Black', 'Grey']
MIN_AGE = 14
MAX_AGE = 85

#Origin traits
NATIONALITY = {'Asia': ['China', 'Japan'],
                'Europe': ['UK', 'France', 'Germany'],
            }

#Belief traits
RELIGIONS = {'Christian': ['Catholic', 'Protestant', 'Baptist', 'Reformed'],
                'Muslim': ['Sunni', 'Shia'],
                'None': ['Atheist', 'Humanist', 'Agnostic'],
            }
            
def print_name():
    pass
    
def print_physical_traits():
    print "Eye colour: {0}".format(choice(EYE_COLOUR))
    print "Hair colour: {0}".format(choice(HAIR_COLOUR))
    print "Age: {0}".format(randint(MIN_AGE, MAX_AGE))

def print_origin_traits():
    key = choice(NATIONALITY.keys())
    print "Nationality: {0}".format(choice(NATIONALITY[key]))

def print_belief_traits():
    key = choice(RELIGIONS.keys())
    
    print "Relegion: {0} ({1})".format(key, choice(RELIGIONS[key]))
    
if __name__ == "__main__":
    print_name()
    print_physical_traits()
    print_origin_traits()
    print_belief_traits()