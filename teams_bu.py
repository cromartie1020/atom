#original team
from teams import TEAMS
with open('teams.txt', 'w') as test :
      
    for team in TEAMS:
        print (team)
        print(team[0])
        test.write(team[0])
  
   
