# eda.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("📊 EDA Start Ho Raha Hai...")

# Data load karo (apne scraped data se)
df = pd.read_csv('books_data.csv')

# Basic info dekho
print("="*50)
print("DATASET INFORMATION")
print("="*50)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe(include='all'))