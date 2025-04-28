import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import os

# Create output directory
output_dir = 'company_report/Towns Protocol/asset/traffic'
os.makedirs(output_dir, exist_ok=True)

plt.rcParams.update({'font.size': 20, 'font.family': 'sans-serif'})

# 1. Keywords
keywords = ['townsprotocol f', 'towns airdrop', 'towns', 'towns blokcchain', 'родіон єрошек']
search_volume = [40, 750, 18470, 20, 260]

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.bar(keywords, search_volume, color=cm.PuBu(np.linspace(0.2, 0.7, len(keywords))))
ax.set_ylabel('Search Volume')
ax.set_xlabel('Keyword')
ax.set_title('Top Keywords by Search Volume')
plt.xticks(rotation=25, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'keywords_bar.png'))
plt.close()

# 2. Top Countries
countries = ['Russia', 'Ukraine', 'Japan', 'United States', 'Netherlands']
country_shares = [25.43, 11.82, 9.04, 7.24, 5.45]

# Ignore countries with <5% in pie chart label
def autopct_gen(pct):
    return ('%.1f%%' % pct) if pct >= 5 else ''

fig, ax = plt.subplots(figsize=(10, 7))
colors = cm.PuBu(np.linspace(0.3, 0.7, len(countries)))
ax.pie(country_shares, labels=countries, autopct=autopct_gen, startangle=150, colors=colors)
ax.set_title('Top Countries by Traffic')
plt.savefig(os.path.join(output_dir, 'countries_pie.png'))
plt.close()

# 3. Traffic Sources
sources = ['Direct', 'Organic Search', 'Social', 'Referral', 'Ads', 'Mail']
source_shares = [69.29, 15.28, 8.37, 6.44, 0.52, 0.10]

fig, ax = plt.subplots(figsize=(10, 7))
colors = cm.Greens(np.linspace(0.4, 0.8, len(sources)))
ax.pie(source_shares, labels=sources, autopct=autopct_gen, startangle=90, colors=colors)
ax.set_title('Traffic Sources')
plt.savefig(os.path.join(output_dir, 'traffic_sources_pie.png'))
plt.close()

# 4. Social Media Sources
social_platforms = ['X-Twitter', 'Youtube', 'Discord', 'Telegram Webapp', 'VKontakte']
social_shares = [44.93, 27.20, 18.51, 8.42, 0.89]

fig, ax = plt.subplots(figsize=(10, 7))
colors = cm.Oranges(np.linspace(0.3, 0.8, len(social_platforms)))
ax.pie(social_shares, labels=social_platforms, autopct=autopct_gen, startangle=110, colors=colors)
ax.set_title('Social Media Sources')
plt.savefig(os.path.join(output_dir, 'social_platforms_pie.png'))
plt.close()

# 5. Competitors - bar chart
competitors = [
    'warpcast.com', 
    'opensea.io', 
    'debank.com', 
    'guild.xyz',
    'intract.io'
]
competitor_traffic = [1091354, 5117500, 1683837, 622433, 831340]

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.bar(competitors, competitor_traffic, color=cm.cividis(np.linspace(0.2, 0.7, len(competitors))))
ax.set_ylabel('Visits')
ax.set_xlabel('Competitor')
ax.set_title('Competitor Traffic Comparison')
plt.xticks(rotation=25, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'competitors_bar.png'))
plt.close()

# 6. Age Groups
age_ranges = ['25-34', '18-24', '35-44', '45-54', '55-64', '65+']
age_ratios = [72.56, 14.09, 10.00, 2.53, 0.50, 0.32]

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.bar(age_ranges, age_ratios, color=cm.Blues(np.linspace(0.3, 0.9, len(age_ranges))))
ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.set_title('Audience Age Distribution')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'age_groups_bar.png'))
plt.close()