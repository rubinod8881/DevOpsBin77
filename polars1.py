import polars as pl
df=pl.DataFrame({"Name":["Binod Pasad","Rubi Prasad","Aayushman Prasad"],"Age":[44,37,16]})
prin(df)
print(df.filter(df["Age"]>25))
print(df.select("Name"))