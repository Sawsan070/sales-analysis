import pandas as pd

data = {
    "product": ["koffie", "thee", "koffie", "sap", "thee"],
    "prijs": [3, 2, 3, 4, 2],
    "aantal": [10, 5, 8, 3, 7]
}

df = pd.DataFrame(data)
df["omzet"] = df["prijs"] * df["aantal"]

print(df.groupby("product")["omzet"].sum())
