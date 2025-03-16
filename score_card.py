import json
import pandas as pd

with open('D:/Github-Repos/cricket_score_card/Cricket.json') as f:
    data = json.load(f)
    print(data)

import pprint
pprint.pprint(data['results'])

batting_df = pd.json_normalize(data['results']['live_details']['scorecard'][0]['batting'])
print(batting_df)

