import json
import pandas as pd

with open('./Cricket.json') as f:
    data = json.load(f)
    # print(data)
# print("press 1 for first innings, 2 for second innings")
innings_input = int(input("Press 1 for 1st innings, 2 for 2nd innings: "))
print(innings_input)
if innings_input == 1:
    print("You have choosen 1st innings")
    first_innings = pd.json_normalize(data['results']['live_details']['scorecard'][0])
    first_innings_details = int(input("Press 1 for Batting, 2 for Bowling, 3 for Batting Player, 4 for Bowling Player: "))
    if first_innings_details == 1:
        print(first_innings['batting'])
    elif first_innings_details == 2:
        print(first_innings['bowling'])
    elif first_innings_details == 3:
        batsman_name = input("Please enter the Player name: ")
        print("Entered player name is ", batsman_name)
    elif first_innings_details == 4:
        bowler_name = input("Please enter the Player name: ")
        print("Entered player name is ", bowler_name)
    else:
        print ("Invalid input, Please enter a valid input to display innings scorecard")
elif innings_input == 2:
    print("You have choosen 2nd innings")
    second_innings = pd.json_normalize(data['results']['live_details']['scorecard'][1])
else:
    print("You have provided wrong input. Press 1 for 1st innings, 2 for 2nd innings: ")

# batting_df = pd.json_normalize(data['results']['live_details']['scorecard'][0]['batting'])
# print(batting_df)

