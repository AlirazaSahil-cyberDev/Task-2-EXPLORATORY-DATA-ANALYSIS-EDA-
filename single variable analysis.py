# Single variable analysis

# 1. Price Distribution
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
df['Price_Numeric'].hist(bins=30, color='skyblue', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')

# 2. Rating Distribution
plt.subplot(1, 3, 2)
df['Rating'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')

# 3. Availability
plt.subplot(1, 3, 3)
df['Available'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Availability')

plt.tight_layout()
plt.savefig('univariate_analysis.png')
plt.show()

print("✅ Univariate analysis complete!")