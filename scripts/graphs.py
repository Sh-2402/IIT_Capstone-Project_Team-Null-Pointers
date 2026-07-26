import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/orders_clean.csv")  # relative to notebooks/ folder
df['order_time'] = pd.to_datetime(df['order_time'])
df['order_hour'] = df['order_time'].dt.hour

print(df.shape)
df.head()

## 3.1 Distribution of Delivery Time

plt.figure(figsize=(8, 5))
sns.histplot(df['delivery_minutes'], bins=30, kde=True)
plt.axvline(10, color='red', linestyle='--', label='10-min SLA')
plt.title("Distribution of Delivery Times")
plt.xlabel("Delivery time (minutes)")
plt.legend()

plt.show()

## 3.2 Delivery Time by Hour of Day
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='order_hour', y='delivery_minutes')
plt.axhline(10, color='red', linestyle='--')
plt.title("Delivery Time by Hour of Day")
plt.show()

## 3.3 Delivery Time by Store

plt.figure(figsize=(12, 6))
store_order = df.groupby('store_id')['delivery_minutes'].median().sort_values().index
sns.boxplot(data=df, x='store_id', y='delivery_minutes', order=store_order)
plt.axhline(10, color='red', linestyle='--')
plt.xticks(rotation=90)
plt.title("Delivery Time by Store (sorted by median)")
plt.show()

## 3.4 Delivery Time by Category
plt.figure(figsize=(10, 5))
cat_order = df.groupby('category')['delivery_minutes'].median().sort_values().index
sns.boxplot(data=df, x='category', y='delivery_minutes', order=cat_order)
plt.axhline(10, color='red', linestyle='--')
plt.xticks(rotation=45)
plt.title("Delivery Time by Category")
plt.show()

## 3.5 Summary — What Changes the Feature List

##- [e.g. "Store-level variation (3.3) is the strongest visual signal — 
##  justifies including store_id as a feature."]
##- [e.g. "Category showed minimal spread (3.4) — weak justification for 
##  including it, kept anyway for completeness / dropped."]
##- [e.g. "Hour shows moderate variation (3.2) but less dramatic than store 
 ## — justifies order_hour as a secondary feature."]