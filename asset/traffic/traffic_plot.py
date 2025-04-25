import os
import matplotlib.pyplot as plt

# 示例结构化 traffic 数据（实际使用时请替换为API获取或文件读取后的真实数据）
traffic = {
    "mau_trend": {
        "dates": ["2023-10", "2023-11", "2023-12", "2024-01", "2024-02", "2024-03", "2024-04"],
        "maus": [87000, 94000, 96000, 99000, 101000, 104000, 106000]
    },
    "keywords": [
        {"keyword": "halliday", "volume": 17420},
        {"keyword": "halliday glasses", "volume": 12650},
        {"keyword": "halliday smart glasses", "volume": 2500},
        {"keyword": "movie recommendation app", "volume": 620},
        {"keyword": "haliday", "volume": 2610}
    ],
    "countries": [
        {"country": "US", "percent": 20.71},
        {"country": "GB", "percent": 5.83},
        {"country": "DE", "percent": 5.83},
        {"country": "FR", "percent": 5.40},
        {"country": "SG", "percent": 4.61}
    ],
    "sources": [
        {"source": "Direct", "percent": 31.88},
        {"source": "Search", "percent": 43.09},
        {"source": "Social", "percent": 11.72},
        {"source": "Referral", "percent": 11.07},
        {"source": "Ads", "percent": 2.00},
        {"source": "Mail", "percent": 0.15}
    ],
    "social_media": [
        {"platform": "YouTube", "percent": 82.55},
        {"platform": "Facebook", "percent": 12.55},
        {"platform": "X", "percent": 4.90}
    ]
}

os.makedirs('asset/traffic', exist_ok=True)
plt.rcParams.update({'font.size': 20, 'font.family': 'sans-serif'})

# 1. MAU趋势折线图
if "mau_trend" in traffic and traffic["mau_trend"]["dates"]:
    plt.figure(figsize=(12,8))
    plt.plot(traffic["mau_trend"]["dates"], traffic["mau_trend"]["maus"], marker='o', color='#5470c6')
    plt.title('MAU Trend (Past 6-12 Months)', fontsize=20)
    plt.xlabel('Month', fontsize=20)
    plt.ylabel('MAU', fontsize=20)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('asset/traffic/mau_trend.png')
    plt.close()

# 2. 关键词柱状图
if "keywords" in traffic and traffic["keywords"]:
    keywords = [kw["keyword"] for kw in traffic["keywords"]]
    volumes = [kw["volume"] for kw in traffic["keywords"]]
    plt.figure(figsize=(12,8))
    bars = plt.barh(keywords, volumes, color='#91cc75')
    plt.title('Top Keywords by Monthly Volume', fontsize=20)
    plt.xlabel('Monthly Search Volume', fontsize=20)
    plt.ylabel('Keyword', fontsize=20)
    for i, v in enumerate(volumes):
        plt.text(v + max(volumes)*0.01, i, str(v), va='center', fontsize=20)
    plt.tight_layout()
    plt.savefig('asset/traffic/keywords.png')
    plt.close()

# 3. 主要访问国家饼图
if "countries" in traffic and traffic["countries"]:
    countries = [c["country"] for c in traffic["countries"]]
    percents = [c["percent"] for c in traffic["countries"]]
    plt.figure(figsize=(10,10))
    patches, texts, autotexts = plt.pie(percents, labels=countries, autopct='%1.1f%%',
                                        colors=['#73c0de', '#fac858', '#ee6666', '#3ba272', '#fc8452'],
                                        startangle=140, textprops={'fontsize': 20})
    plt.title('Visitor Countries Distribution', fontsize=20)
    plt.tight_layout()
    plt.savefig('asset/traffic/countries.png')
    plt.close()

# 4. 流量来源饼图
if "sources" in traffic and traffic["sources"]:
    sources = [s["source"] for s in traffic["sources"]]
    perc_sou = [s["percent"] for s in traffic["sources"]]
    plt.figure(figsize=(10,10))
    patches, texts, autotexts = plt.pie(perc_sou, labels=sources, autopct='%1.1f%%',
                                        colors=['#91cc75', '#5470c6', '#73c0de', '#fac858', '#fc8452', '#ee6666'],
                                        startangle=120, textprops={'fontsize': 20})
    plt.title('Traffic Sources', fontsize=20)
    plt.tight_layout()
    plt.savefig('asset/traffic/traffic_sources.png')
    plt.close()

# 5. 社交媒体来源柱状图
if "social_media" in traffic and traffic["social_media"]:
    platforms = [s["platform"] for s in traffic["social_media"]]
    percents_social = [s["percent"] for s in traffic["social_media"]]
    plt.figure(figsize=(12,8))
    bars = plt.bar(platforms, percents_social, color='#fac858')
    plt.title('Social Media Traffic Sources', fontsize=20)
    plt.xlabel('Platform', fontsize=20)
    plt.ylabel('Percent (%)', fontsize=20)
    for i, v in enumerate(percents_social):
        plt.text(i, v + 1, f'{v:.1f}%', ha='center', fontsize=20)
    plt.tight_layout()
    plt.savefig('asset/traffic/social_media_sources.png')
    plt.close()