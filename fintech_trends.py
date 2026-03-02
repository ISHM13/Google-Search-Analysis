import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import time

Trending_topics = TrendReq(hl='en-US', tz=360)

# Creating a dataframe to store top 10 countries that search for the term "Fintech"
# Using build_payload to store the list of keywords to search
kw_list=["Fintech"]
Trending_topics.build_payload(kw_list, cat=0, timeframe='today 12-m')
time.sleep(5)

# Returns the historical indexed data forr when the 
# specified word was most searched: 
data = Trending_topics.interest_over_time()
data = data.sort_values(by="Fintech", ascending=False)
data = data.head(10)
print(data)

# Specified time periods (2026 Jan - Feb)
kw_list = ["Fintech"]
Trending_topics.build_payload(kw_list, cat=0, timeframe='2026-01-01 2026-02-01', geo='', gprop='')
data = Trending_topics.interest_over_time()
data = data.sort_values(by="Fintech", ascending = False)
data = data.head(10)
print(data)

# Performance of "Fintech" per region on a scale of 0 - 100
data = Trending_topics.interest_by_region()
data = data.sort_values(by="Fintech", ascending = False)
data = data.head(10)
print(data)

# Visualizing interest by region
plt.style.use('fivethirtyeight')
data.reset_index().plot(x='geoName', y='Fintech',
                        figsize=(10, 5), kind="bar")
plt.savefig('fintech_chart.png')
plt.close()
print("Chart saved as fintech_chart.png")

# Searching for related queries: 
try:
    Trending_topics.build_payload(kw_list=['Fintech'])
    related_queries = Trending_topics.related_queries()
    print("\n=== Related Queries ===")
    print(related_queries)
except (KeyError, IndexError):
    print("No related queries found for 'Fintech'")

# Keyword suggestions: 
keywords = Trending_topics.suggestions(keyword='Fintech')
df = pd.DataFrame(keywords)
df.drop(columns='mid')
print("\n === Keyword Suggestions ===")
print(df)