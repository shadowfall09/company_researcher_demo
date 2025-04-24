import matplotlib.pyplot as plt
import os

# 创建保存图片的目录
os.makedirs('asset/traffic', exist_ok=True)

# 数据
countries = ["US", "CN", "IN", "KR", "HK"]
country_shares = [19.31, 16.80, 11.76, 5.13, 4.92]

keywords = ["langchain", "langgraph", "langsmith", "langchain js", "langraph"]
keyword_values = [178179, 54018, 29765, 5288, 4897]

traffic_sources = ["Organic Search", "Direct Visits", "Referral Visits", "Social Networks", "Paid Search"]
traffic_shares = [51.91, 40.98, 6.16, 0.80, 0.008]

social_platforms = ["Reddit", "YouTube", "LinkedIn", "X", "Facebook"]
social_shares = [35.26, 30.47, 11.82, 11.68, 3.13]

# 设置字体大小
font_size = 20

# 绘制主要访问国家的饼图
plt.figure(figsize=(10, 6))
plt.pie(country_shares, labels=countries, autopct='%.2f%%', colors=['#4caf50', '#2196f3', '#ffeb3b', '#ff9800', '#f44336'])
plt.title('Main Visitor Countries', fontsize=font_size)
plt.axis('equal')
plt.savefig('asset/traffic/main_visitor_countries.png')
plt.close()

# 绘制关键词的柱状图
plt.figure(figsize=(12, 8))
plt.bar(keywords, keyword_values, color=['#4caf50', '#2196f3', '#ffeb3b', '#ff9800', '#f44336'])
plt.title('Keyword Analysis', fontsize=font_size)
plt.xlabel('Keywords', fontsize=font_size)
plt.ylabel('Estimated Traffic Value (USD)', fontsize=font_size)
plt.xticks(rotation=45, fontsize=font_size)
plt.yticks(fontsize=font_size)
plt.tight_layout()
plt.savefig('asset/traffic/keyword_analysis.png')
plt.close()

# 绘制流量来源的饼图
plt.figure(figsize=(10, 6))
plt.pie(traffic_shares, labels=traffic_sources, autopct='%.2f%%', colors=['#4caf50', '#2196f3', '#ffeb3b', '#ff9800', '#f44336'])
plt.title('Traffic Sources', fontsize=font_size)
plt.axis('equal')
plt.savefig('asset/traffic/traffic_sources.png')
plt.close()

# 绘制社交媒体来源的柱状图
plt.figure(figsize=(12, 8))
plt.bar(social_platforms, social_shares, color=['#4caf50', '#2196f3', '#ffeb3b', '#ff9800', '#f44336'])
plt.title('Social Media Sources', fontsize=font_size)
plt.xlabel('Social Platforms', fontsize=font_size)
plt.ylabel('Share of Social Traffic (%)', fontsize=font_size)
plt.xticks(rotation=45, fontsize=font_size)
plt.yticks(fontsize=font_size)
plt.tight_layout()
plt.savefig('asset/traffic/social_media_sources.png')
plt.close()