# Complete analysis report banao

def generate_report(df):
    print("="*60)
    print("📊 COMPLETE EDA REPORT")
    print("="*60)
    
    # Dataset Overview
    print("\n1. DATASET OVERVIEW")
    print("-"*40)
    print(f"Total Records: {len(df)}")
    print(f"Total Features: {len(df.columns)}")
    
    # Key Statistics
    print("\n2. KEY STATISTICS")
    print("-"*40)
    print(f"Average Price: £{df['Price_Numeric'].mean():.2f}")
    print(f"Most Common Rating: {df['Rating'].mode()[0]}")
    print(f"Books Available: {df['Available'].value_counts()['Yes']}")
    
    # Insights
    print("\n3. KEY INSIGHTS")
    print("-"*40)
    
    # Insight 1: Price range
    print(f"✅ Books range from £{df['Price_Numeric'].min()} to £{df['Price_Numeric'].max()}")
    
    # Insight 2: Rating distribution
    print(f"✅ Most books have {df['Rating'].mode()[0]} star rating")
    
    # Insight 3: Price vs Rating
    expensive_books = df[df['Price_Numeric'] > df['Price_Numeric'].mean()]
    expensive_avg_rating = expensive_books['Rating_Numeric'].mean()
    cheap_books = df[df['Price_Numeric'] <= df['Price_Numeric'].mean()]
    cheap_avg_rating = cheap_books['Rating_Numeric'].mean()
    
    if expensive_avg_rating > cheap_avg_rating:
        print("✅ Expensive books generally have better ratings")
    else:
        print("✅ Price doesn't guarantee better ratings")
    
    # Recommendations
    print("\n4. RECOMMENDATIONS")
    print("-"*40)
    print("📌 Focus on books with 4-5 star ratings")
    print("📌 Competitive pricing between £20-£35")
    print("📌 Ensure stock availability for popular ratings")

generate_report(df)