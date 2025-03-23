import json
import pandas as pd
with open('./Cricket.json') as data:
     data_source = json.load(data)
     # print(data_source)
import pprint
# pprint.pprint(data_source)
first_innings = pd.json_normalize(data_source['results']['live_details']['scorecard'][0])
first_innings_batting= pd.json_normalize(data_source['results']['live_details']['scorecard'][0]['batting'])
first_innings_batting_df = pd.DataFrame(first_innings_batting)
first_innings_batting_drop= first_innings_batting.drop('minutes', axis= 1 )
first_innings_batting_details = first_innings_batting_drop.rename(columns={"player_name" : "Batsman Name","how_out":"Wicket"})
first_innings_bowling = pd.json_normalize(data_source['results']['live_details']['scorecard'][0]['bowling'])
first_innings_bowling_df = first_innings_bowling.rename(columns={"player_name":"Bowler Name",'runs_conceded':'Runs'})
first_innings_bowling_details = pd.DataFrame(first_innings_bowling_df)
second_innings = pd.json_normalize(data_source['results']['live_details']['scorecard'][1])
second_innings_batting =pd.json_normalize(data_source['results']['live_details']['scorecard'][1]['batting'])
second_innings_batting_df = pd.DataFrame(second_innings_batting)
second_innings_batting_drop= second_innings_batting.drop('minutes', axis= 1 )
second_innings_batting_details = second_innings_batting_drop.rename(columns={"player_name" : "Batsman Name","how_out":"Wicket"})
second_innings_bowling = pd.json_normalize(data_source['results']['live_details']['scorecard'][1]['bowling'])
second_innings_bowling_df = second_innings_bowling.rename(columns={"player_name":"Bowler Name",'runs_conceded':'Runs'})
second_innings_bowling_details = pd.DataFrame(second_innings_bowling_df)
while True:

    Innings_details = int(input("Press 1 for first_innings, 2 for second_innings : "))
    print(Innings_details)
    if Innings_details == 1:
         print("you have chosen the first_innings")
         first_innings = pd.json_normalize(data_source['results']['live_details']['scorecard'][0])
         print(first_innings)
         first_innings_data = int(input("Press 1 for batting. 2 for bowling, 3 for batting player, 4 for bowling player :"))
         print(first_innings_data)
         if first_innings_data == 1:
             print(first_innings_batting_details)
         elif first_innings_data == 2:
             print(first_innings_bowling_details)
         elif first_innings_data == 3:
             def to_get_Batsman_details(player_name):
                 player = first_innings_batting_details[first_innings_batting_details["Batsman Name"].str.lower() == player_name.lower()]
                 if not player.empty:
                     return player[['Batsman Name', 'Wicket', 'runs', 'balls']]
                 else:
                     print(f"No player name found with {player_name}")
             player_name = input('Enter the Batsman Name :')
             print(to_get_Batsman_details(player_name))
         elif first_innings_data == 4:
             def to_get_Bowler_details(bowler_name):
                 bowler = first_innings_bowling_details[first_innings_bowling_details["Bowler Name"].str.lower() == bowler_name.lower()]
                 if not bowler.empty:
                     return bowler[["Bowler Name", "wickets", "overs", "economy", "Runs"]].to_string(index=False)
                 else:
                     return f"No bowler found with the name '{bowler_name}'."
             bowler_name = input('Enter the Bowler Name :')
             print(to_get_Bowler_details(bowler_name))

         else:
             print("Invalid entry")
    elif Innings_details == 2:
         print("You have Chosen the second_innings")
         print(second_innings)
         second_innings_data = int(input("Press 1 for batting. 2 for bowling, 3 for batting player, 4 for bowling player :"))
         print(second_innings_data)
         if second_innings_data == 1:
             print(second_innings_batting_details)
         elif second_innings_data == 2:
             print(second_innings_bowling_details)
         elif second_innings_data == 3:
             def get_Batsman_details(player_name):
                 player = second_innings_batting_details[second_innings_batting_details["Batsman Name"].str.lower() == player_name.lower()]
                 if not player.empty:
                     return player[['Batsman Name', 'Wicket', 'runs', 'balls']]
                 else:
                     print(f"No player name found with {player_name}")
             player_name = input('Enter the Batsman Name :')
             print(get_Batsman_details(player_name))
         elif second_innings_data == 4:
             def Bowler_details(bowler_name):
                 bowler = second_innings_bowling_details[second_innings_bowling_details["Bowler Name"].str.lower() == bowler_name.lower()]
                 if not bowler.empty:
                     return bowler[["Bowler Name", "wickets", "overs", "economy", "Runs"]].to_string(index=False)
                 else:
                     return f"No bowler found with the name '{bowler_name}'."
             bowler_name = input('Enter the Bowler Name :')
             print(Bowler_details(bowler_name))
    else:
        print("You Entered the Wrong input.Please enter the Given_Number")
