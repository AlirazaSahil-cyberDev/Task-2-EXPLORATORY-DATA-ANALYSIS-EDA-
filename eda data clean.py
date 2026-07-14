# Price column clean karo (remove £ sign)
df['Price_Numeric'] = df['Price'].str.replace('£', '').astype(float)

# Ratings ko number mein convert karo
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Numeric'] = df['Rating'].map(rating_map)

# Duplicates check karo
duplicates = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates removed!")

print("\n✅ Data cleaned successfully!")