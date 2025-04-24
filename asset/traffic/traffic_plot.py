import matplotlib.pyplot as plt
import pandas as pd
import os

# Ensure the directory exists
os.makedirs('assets/traffic', exist_ok=True)

# Sample data from the context

# Data for "主要访问国家"
country_data = {
    "Country": ["United States", "China", "India", "Korea", "Hong Kong"],
    "Visit Share (%)": [19.31, 16.80, 11.76, 5.13, 4.92]
}

# Data for "关键词"
keyword_data = {
    "Keyword": ["langchain", "langgraph", "langsmith", "langchain js", "langraph"],
    "Monthly Search Volume": [314780, 102560, 59270, 11870, 12110]
}

# Data for "流量来源"
traffic_source_data = {
    "Source": ["Direct", "Organic Search", "Referral", "Social", "Paid Search"],
    "Share (%)": [40.98, 51.91, 6.16, 0.80, 0.01]
}

# Data for "社交媒体来源"
social_media_data = {
    "Platform": ["Reddit", "YouTube", "LinkedIn", "Twitter", "Facebook"],
    "Traffic Share (%)": [35.26, 30.47, 11.82, 11.68, 3.13]
}

# Plot function for pie chart
def plot_pie_chart(data, labels, title, filename):
    plt.figure(figsize=(10, 8))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854'])
    plt.title(title, fontsize=20)
    plt.axis('equal')
    plt.savefig(f'assets/traffic/{filename}.png', bbox_inches='tight')
    plt.close()

# Plot function for bar chart
def plot_bar_chart(categories, values, title, xlabel, ylabel, filename):
    plt.figure(figsize=(12, 8))
    plt.bar(categories, values, color=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854'])
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.xticks(rotation=45, ha="right", fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.savefig(f'assets/traffic/{filename}.png', bbox_inches='tight')
    plt.close()

# Create plots
# 1. Visiting countries as a pie chart
plot_pie_chart(country_data['Visit Share (%)'], country_data['Country'], 'Traffic by Country', 'traffic_by_country')

# 2. Keywords as a bar chart
plot_bar_chart(keyword_data['Keyword'], keyword_data['Monthly Search Volume'], 'Monthly Search Volume by Keyword', 'Keyword', 'Search Volume', 'search_volume_by_keyword')

# 3. Traffic sources as a pie chart
plot_pie_chart(traffic_source_data['Share (%)'], traffic_source_data['Source'], 'Traffic Source Share', 'traffic_source_share')

# 4. Social media sources as a pie chart
plot_pie_chart(social_media_data['Traffic Share (%)'], social_media_data['Platform'], 'Social Media Traffic Share', 'social_media_traffic_share')