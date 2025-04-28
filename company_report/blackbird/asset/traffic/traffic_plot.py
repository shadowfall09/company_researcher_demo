import os
import matplotlib.pyplot as plt

# 确保保存目录存在
output_dir = 'company_report/blackbird/asset/traffic'
os.makedirs(output_dir, exist_ok=True)

plt.rcParams['font.size'] = 20

# 数据定义
# 1. MAU
mau = 30000  # 约3万

# 2. 关键词及搜索量
keyword_data = [
    {'Keyword': 'blackbird labs', 'Search Volume': 1390},
    {'Keyword': 'blackbird', 'Search Volume': 303910},
    {'Keyword': 'xyz', 'Search Volume': 141580},
    {'Keyword': 'blackbird crypto', 'Search Volume': 450},
    {'Keyword': 'blackbird loyalty', 'Search Volume': 260},
]
keywords = [item['Keyword'] for item in keyword_data]
keyword_volume = [item['Search Volume'] for item in keyword_data]

# 3. 主要访问国家
country_labels = ['USA', 'Indonesia', 'UK', 'India', 'Canada']
country_percents = [53.53, 6.99, 6.89, 5.63, 5.39]

# 4. 流量来源
source_labels = ['Direct', 'Organic Search', 'Referral', 'Social', 'Mail', 'Display Ads']
source_percents = [49.56, 35.05, 10.81, 3.53, 0.15, 0.83]

# 5. 社交媒体来源
social_labels = ['X(Twitter)', 'LinkedIn']
social_percents = [98.43, 1.57]

# 6. 竞争对手流量
competitor_labels = [
    'notboring.co',
    'warpcast.com',
    'dosh.com',
    'blockworks.co',
    'creditdonkey.com',
    'chase.com',
    'superrare.com'
]
competitor_traffic = [129766, 113320, 103627, 101244, 90568, 195273000, 153000]

# 7. 年龄段分布
age_labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
age_percents = [8.85, 34.35, 14.3, 18.3, 15.1, 9.1]

#------------------#
# 关键词 柱状图
plt.figure(figsize=(12,8))
plt.bar(keywords, keyword_volume, color='#6c8da2')
plt.xlabel('Keyword', fontsize=20)
plt.ylabel('Search Volume', fontsize=20)
plt.title('Top 5 Keywords Search Volume', fontsize=20)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'keywords_bar.png'), dpi=180)
plt.close()

# 主要访问国家 饼图
explode_countries = [0.07 if val == max(country_percents) else 0 for val in country_percents]
def autopct_countries(pct):
    return ('%1.1f%%' % pct) if pct >= 5 else ''
plt.figure(figsize=(8,8))
plt.pie(country_percents, labels=country_labels, autopct=autopct_countries,
        explode=explode_countries, startangle=120,
        colors=['#a7b6c2', '#bed3dd', '#e3e7eb', '#9da9b2', '#c8d3dc'])
plt.title('Top Visitor Countries', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'countries_pie.png'), dpi=180)
plt.close()

# 流量来源 饼图
explode_sources = [0.07 if val == max(source_percents) else 0 for val in source_percents]
def autopct_sources(pct):
    return ('%1.1f%%' % pct) if pct >= 5 else ''
plt.figure(figsize=(8,8))
plt.pie(source_percents, labels=source_labels, autopct=autopct_sources,
        explode=explode_sources, startangle=120,
        colors=['#b9b2a3', '#bfbbc9', '#e7e2db', '#dfdad7', '#dadbdc', '#bfc5ce'])
plt.title('Traffic Sources', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'sources_pie.png'), dpi=180)
plt.close()

# 社交媒体来源 饼图
explode_social = [0.07 if val == max(social_percents) else 0 for val in social_percents]
def autopct_social(pct):
    return ('%1.1f%%' % pct) if pct >= 5 else ''
plt.figure(figsize=(8,8))
plt.pie(social_percents, labels=social_labels, autopct=autopct_social,
        explode=explode_social, startangle=120,
        colors=['#cadcf3', '#b7bbc8'])
plt.title('Social Media Sources', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'social_pie.png'), dpi=180)
plt.close()

# 竞争对手流量 柱状图 (按流量大小排序，不显示极端巨大的chase.com影响观感)
top_comp_labels = ['notboring.co', 'warpcast.com', 'dosh.com', 'blockworks.co', 'creditdonkey.com', 'superrare.com']
top_comp_traffic = [129766, 113320, 103627, 101244, 90568, 153000]
plt.figure(figsize=(12,8))
plt.bar(top_comp_labels, top_comp_traffic, color='#9ebcbc')
plt.xlabel('Competitor', fontsize=20)
plt.ylabel('Traffic', fontsize=20)
plt.title('Competitor Traffic (Excluding Chase.com)', fontsize=20)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'competitor_bar.png'), dpi=180)
plt.close()

# 年龄段分布 饼图
explode_age = [0.07 if val == max(age_percents) else 0 for val in age_percents]
def autopct_age(pct):
    return ('%1.1f%%' % pct) if pct >= 5 else ''
plt.figure(figsize=(8,8))
plt.pie(age_percents, labels=age_labels, autopct=autopct_age,
        explode=explode_age, startangle=120,
        colors=['#90bfc3','#bfbfc5','#e3e1e8','#e8cbba','#cabfad','#a0abb7'])
plt.title('Visitor Age Distribution', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'age_pie.png'), dpi=180)
plt.close()