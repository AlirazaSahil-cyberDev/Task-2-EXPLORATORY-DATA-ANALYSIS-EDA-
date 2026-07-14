# Outliers

def detect_outliers_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data < lower_bound) | (data > upper_bound)]

outliers = detect_outliers_iqr(df['Price_Numeric'])
print(f"\n💰 Price outliers: {len(outliers)}")
print(f"Outlier prices: {outliers.tolist()}")

# Box plot with outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Price_Numeric'])
plt.title('Price Distribution with Outliers')
plt.savefig('outliers.png')
plt.show()