import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# ✅ FIXED CSV read line
df = pd.read_csv("all_books.csv", encoding="utf-8-sig")

df["Price"] = df["Price"].replace(r"[^\d.]", "", regex=True).astype(float)


# Rating chart
rating_counts = Counter(df["Rating"])
plt.figure(figsize=(6,4))
plt.bar(rating_counts.keys(), rating_counts.values(), color="skyblue")
plt.title(" Book Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("ratings_chart.png")
plt.show()

# Top expensive books chart
top_expensive = df.sort_values("Price", ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.barh(top_expensive["Title"], top_expensive["Price"], color="salmon")
plt.title(" Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.savefig("expensive_books.png")
plt.show()
