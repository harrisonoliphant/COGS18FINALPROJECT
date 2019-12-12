def callable_function():
    assert callable(run_bot)
    
def month_test():
    month=input("Welcome to Astro-Bot\nWhat is your birthday month? ").lower()
    assert (month=='january' or month=='february' or month=='march' or
            month=='april' or month=='may' or month=='june' or
            month=='july' or month=='august' or month=='september' or
            month=='october' or month=='november' or month=='december')
    
def day_test():
    day=int(input("What is your bithday day? "))
    assert 0<day<32