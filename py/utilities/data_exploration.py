import datetime
import pandas as pd

# Define a dictionary containing employee data
data = {
    'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32],
    'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
    'service_date': ['2020-01-20', '2020-02-23', '2021-03-24', '2022-01-05']
}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

print(df)

df_columns = list(df.columns)
for column in df_columns:
  print(df[column].iloc[0])
  if isinstance(df[column].iloc[0], datetime.datetime) or isinstance(
      df[column].iloc[0], datetime.date):
    print(f"{column} is of datetime type.")
  else:
    print(type(df[column].iloc[0]))

# pd.to_datetime(df[column].iloc[0])