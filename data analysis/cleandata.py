import numpy as np

def cleaned_data(df):
    df = df.drop_duplicates().copy()
    df["Product"] = df["Product"].fillna("Unknown")
    df["Price"] = df["Price"].fillna(df["Price"].median())

    df["Total_Sales"] = df["Price"] * df["Quantity"]
    
    return df