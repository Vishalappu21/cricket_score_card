import json

import pandas as pd

with open('./Cricket.json') as data:
     data_source = json.load(data)
     # print(data_source)
import pprint
pprint.pprint(data_source)
while True:
    Innings_details = int(input("Press 1 for first_innings, 2 for second_innings : "))
    print(Innings_details)
    if Innings_details == 1:
         print("you have chosen the first_innings")
         first_innings = pd.json_normalize(data_source['results']['live_details']['scorecard'][0])
         # print(first_innings)
         first_innings_data = int(input("Press 1 for batting. 2 for bowling, 3 for batting player, 4 for bowling player :"))
         print(first_innings_data)
         if first_innings_data == 1:
              batting_data = pd.json_normalize(data_source['results']['live_details']['scorecard'][0]['batting'])
              first_innings_batting_data = batting_data.drop('minutes', axis=1)
              print(first_innings_batting_data)
         elif first_innings_data == 2:
             first_innings_bowling = pd.json_normalize(data_source['results']['live_details']['scorecard'][0]['bowling'])
             print(first_innings_bowling)
         elif first_innings_data == 3:
             player_name = input("\nEnter player name: ")
             player_details = next((player for player in data_source['results']['live_details']['scorecard'][0]['batting'] if
                                    player['player_name'].lower() == player_name.lower()), None)
             if player_details:
                 print("\nPlayer Details:")
                 print(json.dumps(player_details, indent=4))
             else:
                 print(f"No player found with the name '{player_name}'.")
         elif first_innings_data == 4:
             player_name = input("\nEnter player name: ")
             player_details = next(
                 (player for player in data_source['results']['live_details']['scorecard'][0]['bowling'] if
                  player['player_name'].lower() == player_name.lower()), None)
             if player_details:
                 print("\nPlayer Details:")
                 print(json.dumps(player_details, indent=4))
             else:
                 print(f"No player found with the name '{player_name}'.")

         else:
             print("Invaild entry")
    elif Innings_details == 2:
        print("You have Chosen the second_innings")
        second_innings = pd.json_normalize(data_source['results']['live_details']['scorecard'][1])
        # print(second_innings)
        second_innings_data = int(input("Press 1 for batting. 2 for bowling, 3 for batting player, 4 for bowling player :"))
        print(second_innings_data)
        if second_innings_data == 1:
            batting_data = pd.json_normalize(data_source['results']['live_details']['scorecard'][1]['batting'])
            second_innings_batting_data = batting_data.drop('minutes', axis=1)
            print(second_innings_batting_data)
        elif second_innings_data == 2:
            second_bowling_data = pd.json_normalize(data_source['results']['live_details']['scorecard'][1]['bowling'])
            print(second_bowling_data)
        elif second_innings_data == 3:
            player_name = input("\nEnter player name: ")
            player_details = next(
                (player for player in data_source['results']['live_details']['scorecard'][1]['batting'] if
                 player['player_name'].lower() == player_name.lower()), None)
            if player_details:
                print("\nPlayer Details:")
                print(json.dumps(player_details, indent=4))
            else:
                print(f"No player found with the name '{player_name}'.")
        elif second_innings_data == 4:
            player_name = input("\nEnter player name: ")
            player_details = next(
                (player for player in data_source['results']['live_details']['scorecard'][1]['bowling'] if
                 player['player_name'].lower() == player_name.lower()), None)
            if player_details:
                print("\nPlayer Details:")
                print(json.dumps(player_details, indent=4))
            else:
                print(f"No player found with the name '{player_name}'.")
    else:
        print("You Entered the Wrong input.Please enter the Given_Number")