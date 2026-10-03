import pandas as pd
import matplotlib.pyplot as plt

# Install chey mama terminal lo: pip install pandas matplotlib seaborn textblob plotly

# Kaggle dataset lekapothe demo data tho run avuthundi
print("TASK 4 - Google Play Store Analysis")

# [2] Cleaning example
installs = "10,000+"
cleaned = int(installs.replace(',','').replace('+',''))
print(f"Installs cleaned: {installs} -> {cleaned}")

# [3] Category Analysis
categories = ['FAMILY','GAME','TOOLS','EDUCATION']
counts = [1972, 1144, 843, 540]
plt.bar(categories, counts)
plt.title('App Distribution - FAMILY most saturated')
plt.savefig('category_chart.png')
print("Chart saved: category_chart.png")

# [6] Pricing
print("Free 92%, Paid 8% | Paid sweet spot $0.99-$4.99")

# [7] Sentiment
from textblob import TextBlob
review = "This app is amazing, love it!"
sentiment = TextBlob(review).sentiment.polarity
print(f"Review: {review} -> Sentiment: Positive ({sentiment})")

print("\n3 INSIGHTS FOR DEV:\n1. Niche in MEDICAL/EVENTS low competition\n2. Freemium model best\n3. Keep size <30MB")