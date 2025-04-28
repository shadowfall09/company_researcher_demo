import os
import matplotlib.pyplot as plt

# 确保保存目录存在
save_dir = 'asset/traffic'
os.makedirs(save_dir, exist_ok=True)

# 示例流量数据（请将此处替换为实际traffic数据结构）
traffic = {
    'mau_trend': {
        '2023-11': 14000, '2023-12': 16000, '2024-01': 18000, '2024-02': 20000, '2024-03': 22500, '2024-04': 24946
    },
    'keywords': {
        'halliday': 17420,
        'halliday glasses': 12650,
        'movie recommendation app': 620,
        'halliday smart glasses': 2500,
        'haliday': 2610
    },
    'top_countries': {
        'United States': 20.7,
        'United Kingdom': 5.83,
        'Germany': 5.83,
        'France': 5.40,
        'Singapore': 4.61
    },
    'traffic_sources': {
        'Direct': 31.88,
        'Organic Search': 43.09,
        'Referral': 11.07,
        'Social': 11.72,
        'Paid Search': 0.05
    },
    'social_media_sources': {
        'Youtube': 82.55,
        'Facebook': 12.55,
        'X': 4.90
    }
}

plt.rcParams['font.size'] = 20

# MAU趋势（柱状图）
if 'mau_trend' in traffic and traffic['mau_trend']:
    months = list(traffic['mau_trend'].keys())
    mau_values = list(traffic['mau_trend'].values())
    plt.figure(figsize=(10,6))
    bars = plt.bar(months, mau_values, color='#6B8BA4')
    plt.xlabel('Month')
    plt.ylabel('MAU')
    plt.title('MAU Trend')
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, 'mau_trend.png'))
    plt.close()

# 关键词（柱状图）
if 'keywords' in traffic and traffic['keywords']:
    keyword_names = list(traffic['keywords'].keys())
    keyword_search = list(traffic['keywords'].values())
    plt.figure(figsize=(12,6))
    bars = plt.bar(keyword_names, keyword_search, color='#A5B2C2')
    plt.xlabel('Keyword')
    plt.ylabel('Monthly Search Vol.')
    plt.title('Top Keywords')
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, 'keywords.png'))
    plt.close()

# 主要访问国家（饼图）
if 'top_countries' in traffic and traffic['top_countries']:
    country_names = list(traffic['top_countries'].keys())
    country_percents = list(traffic['top_countries'].values())
    plt.figure(figsize=(8,8))
    plt.pie(
        country_percents, 
        labels=country_names, 
        autopct='%1.1f%%', 
        startangle=140,
        colors=['#84A5C0','#C7D3D9','#A3B9C6','#B7C7DB','#94ADC1']
    )
    plt.title('Top Countries')
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, 'top_countries.png'))
    plt.close()

# 流量来源（饼图）
if 'traffic_sources' in traffic and traffic['traffic_sources']:
    source_names = list(traffic['traffic_sources'].keys())
    source_percents = list(traffic['traffic_sources'].values())
    plt.figure(figsize=(8,8))
    plt.pie(
        source_percents, 
        labels=source_names,
        autopct='%1.1f%%', 
        startangle=140,
        colors=['#7B93A8','#BAC8D3','#CDD7E1','#A7B9C8','#DEE3E7']
    )
    plt.title('Traffic Sources')
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, 'traffic_sources.png'))
    plt.close()

# 社交媒体来源（柱状图）
if 'social_media_sources' in traffic and traffic['social_media_sources']:
    social_names = list(traffic['social_media_sources'].keys())
    social_percents = list(traffic['social_media_sources'].values())
    plt.figure(figsize=(8,6))
    bars = plt.bar(social_names, social_percents, color='#AFC3D3')
    plt.xlabel('Social Media')
    plt.ylabel('Percent')
    plt.title('Social Media Sources')
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, 'social_media_sources.png'))
    plt.close()