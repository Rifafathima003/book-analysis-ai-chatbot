import pandas as pd

df = pd.read_csv("data/raw_books.csv")
print(df.columns)
# Avoid pandas downcasting warning for fillna + astype
pd.set_option('future.no_silent_downcasting', True)

# Clean price
df['Price'] = df['Price'].str.replace('Â£', '', regex=False)
df['Price'] = df['Price'].astype(float)

# Convert rating
rating_map = {
    "One": 1, "Two": 2, "Three": 3,
    "Four": 4, "Five": 5
}
df["Rating"] = df["Rating"].map(rating_map)

# Clean availability (only number)
df["Availability"] = df["Availability"].str.extract(r'(\d+)').fillna(0).astype(int)
# optional safe future behavior for pandas downcasting warning
df["Availability"] = df["Availability"].astype('Int64')

df.to_csv("data/cleaned_books.csv", index=False)

print("✅ Cleaning done!")
