import matplotlib.pyplot as plt
import os

# 确保保存图片的目录存在
os.makedirs('asset/traffic', exist_ok=True)

# 数据
countries = ['US', 'CN', 'IN', 'KR', 'HK']
country_shares = [19.31, 16.80, 11.76, 5.13, 4.92]

keywords = ['langchain', 'langgraph', 'langsmith', 'langchain js', 'langraph']
keyword_volumes = [314780, 102560, 59270, 11870, 12110]

traffic_sources = ['Direct Visits', 'Organic Searches', 'Referrals', 'Social Networks', 'Paid Searches', 'Mail Visits', 'Ads Visits']
traffic_shares = [40.98, 51.91, 6.16, 0.80, 0.008, 0.04, 0.10]

social_media_sources = ['Reddit', 'YouTube', 'LinkedIn', 'X (Twitter)', 'Facebook']
social_media_shares = [35.26, 30.47, 11.82, 11.68, 3.13]

# 绘制主要访问国家的饼图
plt.figure(figsize=(10, 7))
plt.pie(country_shares, labels=countries, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Major Visiting Countries', fontsize=20)
plt.savefig('asset/traffic/major_visiting_countries.png')
plt.close()

# 绘制不同比重的柱状图
plt.figure(figsize=(10, 7))
plt.bar(keywords, keyword_volumes, color=plt.cm.Paired.colors)
plt.xlabel('Keywords', fontsize=20)
plt.ylabel('Search Volume', fontsize=20)
plt.title('Search Volume of Keywords', fontsize=20)
plt.xticks(fontsize=20, rotation=45)
plt.yticks(fontsize=20)
plt.tight_layout()
plt.savefig('asset/traffic/keyword_search_volumes.png')
plt.close()

# 绘制流量来源的饼图
plt.figure(figsize=(10, 7))
plt.pie(traffic_shares, labels=traffic_sources, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Traffic Sources', fontsize=20)
plt.savefig('asset/traffic/traffic_sources.png')
plt.close()

# 绘制社交媒体来源的饼图
plt.figure(figsize=(10, 7))
plt.pie(social_media_shares, labels=social_media_sources, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Social Media Sources', fontsize=20)
plt.savefig('asset/traffic/social_media_sources.png')
plt.close()