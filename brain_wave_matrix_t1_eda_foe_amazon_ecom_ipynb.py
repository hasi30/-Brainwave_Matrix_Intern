# -*- coding: utf-8 -*-
"""brain wave matrix t1 EDA foe amazon ecom ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17k-qzjcEMJuZayoXauN9ePsXh6NA2rwc

Explorotary Data Analysis For an Amazon ecom products
"""

import pandas as pd

# Load the uploaded CSV file
file_path = "/content/amazon_sales_data 2025.csv"
df = pd.read_csv(file_path)

# Show basic info and first few rows
df_info = df.info()
df_head = df.head()
df_description = df.describe(include='all')

df_head, df_description

import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%y")

# Create new columns for month and year
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year

# Aggregate data
category_counts = df['Category'].value_counts()
payment_counts = df['Payment Method'].value_counts()
status_counts = df['Status'].value_counts()
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Total Sales'].sum()

# Plotting setup
sns.set(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(16, 12))

# Category distribution
sns.countplot(data=df, y='Category', order=category_counts.index, ax=axs[0, 0])
axs[0, 0].set_title("Product Category Distribution")

# Payment methods
sns.countplot(data=df, y='Payment Method', order=payment_counts.index, ax=axs[0, 1])
axs[0, 1].set_title("Payment Method Distribution")

# Order status
sns.countplot(data=df, x='Status', order=status_counts.index, ax=axs[1, 0])
axs[1, 0].set_title("Order Status Breakdown")

# Monthly sales trend
monthly_sales.plot(kind='line', marker='o', ax=axs[1, 1])
axs[1, 1].set_title("Monthly Sales Trend")
axs[1, 1].set_ylabel("Total Sales")
axs[1, 1].set_xlabel("Month")

plt.tight_layout()
plt.show()











