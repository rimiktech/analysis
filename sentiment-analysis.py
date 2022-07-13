'''
https://www.red-gate.com/simple-talk/development/data-science-development/sentiment-analysis-python/

We have some review data (which are given by manager for own team). 

Sample data is:
Period,Manager,Team,Response
2019-Q1,Mgr 1,Team 1,We're a fun team that works well together and is constantly learning together. We are small which allows us to move quickly and have a process with very little overhead.
2019-Q1,Mgr 1,Team 1,"we have a sound and collaborative team focused on delivery for the business under the current vision and scope for the product. As the vision and scope evolve, we will have the opportunity to expand on the value and capabilities of the product and ensure the proper process and discipline adapt accordingly"
2019-Q1,Mgr 1,Team 1,"we work well as a team, we have fun together, I think we are very healthy"
2019-Q1,Mgr 1,Team 1,I fell pretty good about the health of our team. My main concerns re a lack of vision into what our application's true purpose is and the future direction of our team.

Task List:
- Please create a new function which will identify the most high performed team based on sentiment analysis.

- Team's performance will be calculated with following calculation...
positive: compound score>=0.05
neutral: compound score between -0.05 and 0.05
negative: compound score<=-0.05

'''

import re
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def sentiment_analysis(dataset):
  dataset["rowid"] = df.index + 1
  df_subset = dataset[['rowid', 'Response']].copy()
  df_subset['Response'] = df_subset['Response'].str.replace("[^a-zA-Z#]", " ")
  df_subset['Response'] = df_subset['Response'].str.casefold()
  
  print('Processing sentiment analysis...')
  df_scores = pd.DataFrame(columns=["rowid", "sentiment_type", "score"])
  sid = SentimentIntensityAnalyzer()
  for index, row in df_subset.iterrows():
      scores = sid.polarity_scores(row[1])
      for key, value in scores.items():
        df_scores.loc[len(df_scores)] = [row[0], key, value]

  df_scores_cleaned = df_scores[df_scores.sentiment_type == 'compound']
  df_output = pd.merge(dataset, df_scores_cleaned, on='rowid', how='inner')
  return df_output.drop(columns = ["rowid"])


def get_high_performed_team(dataset):
  team_name = ""
  result = sentiment_analysis(dataset)
  result = result[["Team", "score"]]
  result = result.groupby("Team").mean().reset_index()
  result = result.sort_values(by="score", ascending=False)
  team_name = result.iloc[0]["Team"]
  return team_name

df = pd.read_csv(r'./data/Comments.csv')
team = get_high_performed_team(df)
print(team)



