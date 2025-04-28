import os
import matplotlib.pyplot as plt

# 创建保存图片的目录
save_dir = 'company_report/Meanwhile/asset/traffic'
os.makedirs(save_dir, exist_ok=True)

plt.rcParams['font.size'] = 20

# 1. MAU（仅柱状图，若数据可视）
maus = [5140, 1078, 913]
months = ['2025-01', '2025-02', '2025-03']

plt.figure(figsize=(10, 6))
bars = plt.bar(months, maus, color='#6897bb', width=0.5)
plt.title('Monthly Active Users (MAU)')
plt.ylabel('MAU')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'mau_bar.png'))
plt.close()

# 2. 主要访问国家（假设只有美国有数据）
countries = ['United States', 'Others']
country_share = [99.9999, 0.0001]

def autopct_func(pct):
    return ('%.1f%%' % pct) if pct >= 5 else ''

colors = ['#b7c5d9', '#d2d7df']
plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(
    country_share, labels=countries, colors=colors,
    autopct=autopct_func, startangle=90
)
for autotext in autotexts:
    autotext.set_fontsize(20)
plt.title('Traffic by Country')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'traffic_country_pie.png'))
plt.close()

# 3. 流量来源
sources = ['Direct', 'Organic Search', 'Social', 'Referral', 'Ads', 'Mail']
source_share = [46.29, 27.02, 20.04, 5.72, 0.88, 0.038]
colors = ['#95afba', '#d6cec3', '#a2aab3', '#c8c6a7', '#b7babf', '#e1e5ea']

plt.figure(figsize=(10, 8))
patches, texts, autotexts = plt.pie(
    source_share, labels=sources, colors=colors,
    autopct=autopct_func, startangle=90
)
for autotext in autotexts:
    autotext.set_fontsize(20)
plt.title('Traffic Sources')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'traffic_source_pie.png'))
plt.close()

# 4. 社交媒体来源（暂无详细数据，故略）

# 5. 主要竞争对手对比（柱状图：Meanwhile/Evertas）
sites = ['Meanwhile', 'Evertas']
traffic = [1369, 3135]
bar_colors = ['#718ca1', '#b0b7c8']

plt.figure(figsize=(8,6))
bars = plt.bar(sites, traffic, color=bar_colors, width=0.5)
plt.title('Competitor Total Visits (Mar 2025)')
plt.ylabel('Total Visits')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'competitor_bar.png'))
plt.close()

# 6. 年龄段（暂无数据，略）