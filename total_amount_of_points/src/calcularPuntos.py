
def points(games):

    account = 0
    day = 0
    
    for i in games:
        
        if games[day][0] > games[day][2]:
            account = account + 3
            
        elif games[day][0] == games[day][2]:
            account = account + 1
        else:
            account = account + 0
        
        day = day + 1
    
    return account
