###############################################################################

#dictionaries used for functions below
element = {'Aries':'Fire', 'Taurus':'Earth', 'Gemini':'Air', 
           'Cancer':'Water', 'Leo':'Fire', 'Virgo':'Earth', 
           'Libra':'Air', 'Scorpio':'Water', 'Sagittarius':'Fire',
           'Capricorn':'Earth', 'Aquarius':'Air', 'Pisces':'Water'}

planet = {'Aries':'Mars', 'Taurus':'Earth', 'Gemini':'Mercury',
          'Cancer':'Moon', 'Leo':'Sun', 'Virgo':'Mercury', 
          'Libra':'Venus', 'Scorpio':'Pluto', 'Sagittarius':'Jupiter',
          'Capricorn':'Saturn', 'Aquarius':'Uranus', 'Pisces':'Neptune'}

color = {'Aries':'Red', 'Taurus':'Green', 'Gemini':'Yellow and Blue', 
         'Cancer':'Silver and White', 'Leo':'Purple and Gold', 'Virgo':'Tan', 
         'Libra':'Pink and Light-Blue', 'Scorpio':'Red and Black', 
         'Sagittarius':'Maroon and Navy Blue', 'Capricorn':'Brown', 
         'Aquarius':'Silver', 'Pisces':'Purple and White'}

###############################################################################

def error():
    """Prompts user input if the original input is not recognized 
    i.e. month or day are not valid."""
    
    #asks for month and day (integer) input from user
    #if not originally recognized(ie. error)
    month=input("Please try again. What is your birthday month? ").lower()
    day=int(input("Please try again. What is your bithday day? "))  

###############################################################################
    
def quit_function():
    """Prints thank you message after quitting bot."""
    
    print('I hope you enjoyed the astrology bot!')

###############################################################################   

def run_bot():
    """Determines astrology sign from month input and day input, 
    prompts additional information from user i.e. element, planet, etc.
    
    Primary function used in project. Code derived from
    https://www.geeksforgeeks.org/program-display-astrological
    -sign-zodiac-sign-given-date-birth/, but refactored and repurposed to
    better fit needs of project.
    """
    
    #asks for month and day input from user
    month=input("Welcome to Astro-Bot\nWhat is your birthday month? ").lower() 
    day=int(input("What is your bithday day? ")) 
    
    #tests whether day is a valid input. if not, calls error() function
    if day>32:                              
        error()
    #verifies that month is one of these 12 strings
    while month not in ('january','february', 'march',
                        'april','may','june', 'july',
                        'august','september','october',
                        'november','december'):
        month=input("Please try again. What is your birthday month? ").lower()
        day=int(input("Please try again. What is your bithday day? "))
        if day>32:
            error()
            
    #if month is 'december', evaluate day (integer) to get astrological sign
    if month=='december':   
        if day<22:
            sign='Sagittarius'
        else:
            sign='Capricorn'   
    elif month=='january':         #follows same procedure, but for 'january'
        if day<20:
            sign='Capricorn'
        else:
            sign='Aquarius'
    elif month=='february':        #follows same procedure, but for 'february'
        if day<19:
            sign='Aquarius'
        else:
            sign='Pisces'
    elif month=='march':           #follows same procedure, but for 'march'
        if day<21:
            sign='Pisces'
        else:
            sign='Aries'
    elif month=='april':          #follows same procedure, but for 'april'
        if day<20:
            sign='Aries'
        else:
            sign='Taurus'
    elif month=='may':            #follows same procedure, but for 'may'
        if day<21:
            sign='Taurus'
        else:
            sign='Gemini'
    elif month=='june':           #follows same procedure, but for 'june'
        if day<21:
            sign='Gemini'
        else:
            sign='Cancer'
    elif month=='july':           #follows same procedure, but for 'july'
        if day<23:
            sign='Cancer'
        else:
            sign='Leo'
    elif month=='august':         #follows same procedure, but for 'august'
        if day<23:
            sign='Leo'
        else:
            sign='Virgo'
    elif month=='september':      #follows same procedure, but for 'september'
        if day<23:
            sign='Virgo'
        else:
            sign='Libra'
    elif month=='october':        #follows same procedure, but for 'october'
        if day<23:
            sign='Libra'
        else:
            sign='Scorpio'
    elif month=='november':       #follows same procedure, but for 'november'
        if day<22:
            sign='Scorpio'
        else:
            sign='Sagittarius'

    #print statement including new variable
    #print statement that gives option to call element/planet/color dictionary
    #or compatibility function
    print("You are a "+sign+".")                            
    print("\nHere are a few options:")
    print("To view sign compatibility, type compatibility")
    print("To view "+sign+"'s element, type element")       
    print("To view "+sign+"'s planet, type planet")         
    print("To view "+sign+"'s color, type color")           
    print("To exit, type quit\n")
    
    def more_info():
        """Nested function - if certain strings are inputted, 
        triggers dictionary value for respected input"""
        
        string=None
        
        #verfies string is one of these 5 options, otherwise prompts
        #another user input
        while string not in ('element', 'planet', 'color',
                             'compatibility', 'quit'):
            string=input()
            
            if string=='element':
                print(sign+"'s element(s) are "+element[sign])
                more_info()
            if string=='planet':
                print(sign+"'s planet is "+planet[sign])
                more_info()
            if string=='color':
                print(sign+"'s color(s) are "+color[sign])
                more_info()
            if string=='compatibility':
                compatibility()
                more_info()
            if string=='quit':
                quit_function()
    more_info()


###############################################################################
    
def compatibility():
    """Tests for compatibility of two astrology signs."""
    
    as1=input("Please enter the first astrology sign"
                "(ex: taurus, aries) : ").lower()
    as2=input("Please enter the second astrology sign" 
                "(ex: taurus, aries) : ").lower()
    print("You entered "+as1+" and "+as2+".")
    #tests variables and evaluates (prints) if both conditions are true.
    if as1=='aries':                            
        if (as2=='gemini' or as2=='leo' or 
            as2=='sagittarius' or as2=='aquarius'):
            print('You are compatible.')
        else:
            print('You are not compatible.')            
    elif as1=='taurus':
        if (as2=='cancer' or as2=='virgo' or
            as2=='capricorn' or as2=='pisces'):
            print('You are compatible.')
        else:
            print('You are not compatible.')            
    elif as1=='gemini':
        if (as2=='aries' or as2=='leo' or 
            as2=='libra' or as2=='aquarius'):
            print('You are compatible.')
        else:
            print('You are not compatible.')            
    elif as1=='cancer':
        if (as2== 'taurus' or as2 =='virgo' or 
            as2=='scorpio' or as2 =='pisces'):
            print('You are compatible.')
        else:
            print('You are not compatible.')            
    elif as1=='leo':
        if (as2=='aries' or as2=='gemini' or 
            as2=='libra' or as2=='sagittarius'):
            print('You are compatible.')
        else:
            print('You are not compatible.')            
    elif as1=='virgo':
        if (as2=='taurus' or as2=='cancer' or 
            as2=='scorpio' or as2=='capricorn'):
            print('You are compatible.')
        else:
            print('You are not compatible.')
    elif as1=='libra':
        if (as2=='gemini' or as2=='leo' or 
            as2=='aquarius' or as2=='sagittarius'):
            print('You are compatible.')
        else:
            print('You are not compatible.')
    elif as1=='scorpio':
        if (as2=='cancer' or as2=='virgo' or 
            as2=='capricorn' or as2=='pisces'):
            print('You are compatible.')
        else:
            print('You are not compatible.')
    elif as1=='sagittarius':
        if (as2=='aries' or as2=='leo' or 
            as2=='libra' or as2=='aquarius'):
            print('You are compatible.')
        else:
            print('You are not compatible.')
    elif as1=='capricorn':
        if (as2=='taurus' or as2=='virgo' or 
            as2=='scorpio' or as2=='pisces'):
            print('You are compatible.')
        else:
            print('You are not compatible.')
    elif as1=='aquarius':
        if (as2=='aries' or as2=='gemini' or 
            as2=='libra' or as2=='sagittarius'):
            print('You are compatible.')
        else:
            print('You are not compatible.')
    elif as1=='pisces':
        if (as2=='taurus' or as2=='cancer' or 
            as2=='scorpio' or as2=='capricorn'):
            print('You are compatible.')
        else:
            print('You are not compatible.')
            
###############################################################################