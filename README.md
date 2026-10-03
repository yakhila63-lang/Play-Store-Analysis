# 📱 TASK 4 - Google Play Store Apps Analysis

> Exploratory Data Analysis of 10k+ Android apps from Google Play Store

### 🎯 Objective
Analyze Google Play Store data to help new developers understand market trends, user preferences & pricing strategies.

### 📊 Dataset
- `googleplaystore.csv` - App details (Category, Rating, Size, Installs, Price)
- `googleplaystore_user_reviews.csv` - User reviews & Sentiment

### 🛠️ Tech Stack
`Python` `Pandas` `Matplotlib` `Seaborn` `Plotly` `TextBlob`

### 🔧 What I Did

**1. Data Cleaning:**
- Cleaned `Installs`: "10,000+" -> 10000
- Cleaned `Price`: "$2.99" -> 2.99
- Removed duplicates & handled nulls

**2. Category Analysis:**
- **FAMILY** is most saturated (1972 apps - 20%)
- **MEDICAL / EVENTS** low competition = Opportunity!

**3. Rating vs Size/Price:**
- Avg Rating: 4.2
- Apps <30MB have higher installs & ratings

**4. Pricing Strategy:**
- Free Apps: 92.6%
- Paid Apps: 7.4%
- Sweet Spot: $0.99 - $4.99
- **Recommendation: Freemium model best**

**5. Sentiment Analysis:**
- Used TextBlob to classify reviews -> Positive / Negative / Neutral
- Positive 65%, Negative 22%, Neutral 13%
- Example: "This app is amazing, love it!" -> Positive (0.61)

### 📈 Key Insights for New Developer (Conclusion)

1.  **Niche Opportunity:** Don't go for FAMILY/GAME. Build in MEDICAL, EVENTS, BEAUTY - low competition, high demand.
2.  **Monetization:** Start FREE with In-App Purchases (Freemium). Don't put direct price.
3.  **App Size Matters:** Keep app size <30MB for maximum installs.
4.  **Focus on Reviews:** Positive sentiment = More installs. Fix negative feedback fast.

### ▶️ How to Run
```bash
pip install pandas matplotlib seaborn textblob plotly
python analysis.py
