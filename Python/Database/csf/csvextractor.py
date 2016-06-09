import pandas as pd

row = 5        # rowIndex:fifth row going down, ie:Index 5
column = 5     # columnIndex:fifth row going across, ie:Index 5

'''
df.iloc[row_indexer,column_indexer]
you can also use df['column_name']

!df.iloc does all the work!
gotta figure out how to call values by column name..
'''

# df = pd.read_csv("F:\AI\file.csv")     # Target File
df = pd.read_csv("F:\AI\JEOPARDY.csv")   # Example

with_var = df.iloc[row, column]           # Can use variables
with_int = df.iloc[1, 1]                  # or integers

print(with_var)
print(with_int)
