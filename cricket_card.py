#1. Load the source data of cricket scorecard
import json
import pandas as pd
with open("./Cricket.json") as data_source:
    data = json.load(data_source)
#print(data)
import pprint
pprint.pprint(data)
# Get the input from user to display the batting or bowling of the respective innings Example
# 		a. Key 1 for 1st innings
# 			i. Key 1 for batting
# 			ii. Key 2 for bowling
# 			iii. Key 3 for batting player
# 				1. Get batsman name
# 			iv. Key 4 for bowling player
# 				1. Get bowler name
Match_Innings = int(input("Press 1 for First_innings,2 for Second_Innings : "))
print(Match_Innings)
if Match_Innings == 1:
    print("First_innings")
    First_innings = pd.json_normalize(data['results']['live_details']['scorecard'][0])
    print(First_innings)
    if First_innings == 1:
        print("You have chosen the First_innings")
        First_innings = pd.json_normalize(data['results']['live_details']['scorecard'][0])
        print("First_innings")
elif Match_Innings == 2:
    print("First_innings_bowling")
elif Match_Innings == 3:
    print("First_innings_batsman_details")
elif Match_Innings == 4:
    print("First_innings_bowler_details")
else:
    print("You press the Wrong Number,Please enter the vaild Number,Thank You ")