import pandas as pd
from random import randint

pick = randint(1, 200000)


Round = 2
Category = 3
Value = 4
Question = 5
Answer = 6

df = pd.read_csv("F:\AI\JEOPARDY.csv")
game_round = df.iloc[pick, Round]
category = df.iloc[pick, Category]
value = df.iloc[pick, Value]
question = df.iloc[pick, Question] # you can also use df['column_name']
answer = df.iloc[pick, Answer]

#              df.loc[row_indexer,column_indexer]

print(game_round)
print(category)
print(value)
print(question)
print(answer)
