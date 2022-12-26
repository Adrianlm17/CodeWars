
def loose_change(cents):
    
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    
    while cents >= 25:
        quarters = quarters + 1
        cents = cents - 25
    
    while cents >= 10:
        dimes = dimes + 1
        cents = cents - 10
        
    while cents >= 5:
        nickels = nickels + 1
        cents = cents - 5
        
    while cents >= 1:
        pennies = pennies + 1
        cents = cents - 1
        
    return {
        "Nickels" : nickels,
        "Pennies" : pennies,
        "Dimes" : dimes,
        "Quarters" : quarters
    }
