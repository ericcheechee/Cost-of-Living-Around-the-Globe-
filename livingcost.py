import pandas as pd
from sqlalchemy import create_engine

data = pd.read_csv("kaggle_income.csv") #encoding="latin1")

engine = create_engine('sqlite:///data/costofliving', echo = False)

data.to_sql('COL', con=engine)

#engine.execute("SELECT * FROM COL")

# print(engine.execute("SELECT * FROM COL").fetchall())




engine = create_engine('sqlite:///data/costofliving', echo = False)

costdata = engine.execute("SELECT id,County,City FROM COL").fetchall()
rowsdata = engine.execute("SELECT * FROM COL").fetchall()

print(type(costdata))
