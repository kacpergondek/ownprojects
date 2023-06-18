import random

player_list = input("Input all player names, separated by spaces. ").split()
team_count = int(input("Enter the amount of players "))

#Check if you can split evenly
def even_check():
    even_check = (len(player_list) % team_count)
    if even_check == 0:
        return(True)

#Create teams
teams = []
# Teams are even
if even_check():
    for _ in range(team_count):
        x = random.sample(player_list, k = team_count)
        teams.append(x)
        player_list = [item for item in player_list if item not in x]
# Teams cannot be even
else:
    team_capacities = ([len(player_list) // team_count + (1 if x < len(player_list) % team_count else 0)  for x in range (team_count)])
    index_count = 0      
    for _ in range(team_count):
        x = random.sample(player_list, k = team_capacities[index_count])
        teams.append(x)
        player_list = [item for item in player_list if item not in x]
        index_count += 1

# Print teams 
print([(f"Team {index}: {item}") for index, item in enumerate(teams)])