import os
import matplotlib.pyplot as plt

# 创建目录
output_dir = 'company_report/Meanwhile/asset/traffic'
os.makedirs(output_dir, exist_ok=True)

plt.rcParams.update({'font.size': 20})

# 1. MAU数据（柱状图）
months = ['2025-01', '2025-02', '2025-03']
maus = [7709, 1617, 1369]
plt.figure(figsize=(10, 6))
bars = plt.bar(months, maus, color='#6B8EAB')
plt.ylabel('MAU')
plt.xlabel('Month')
plt.title('Monthly Active Users (MAU)')
plt.savefig(os.path.join(output_dir, 'mau_bar.png'), bbox_inches='tight')
plt.close()

# 2. 主要访问国家（饼图）
country_labels = ['United States']
country_sizes = [100]
plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(
    country_sizes, 
    labels=country_labels,
    autopct=lambda p: '{:.0f}%'.format(p) if p >= 5 else '',
    colors=['#9FB7B9']
)
for text in texts + autotexts:
    text.set_fontsize(20)
plt.title('Top Countries')
plt.savefig(os.path.join(output_dir, 'country_pie.png'), bbox_inches='tight')
plt.close()

# 3. 流量来源（饼图）
source_labels = [
    'Direct', 'Organic Search', 'Social',
    'Referral', 'Mail', 'Ads'
]
source_sizes = [
    46.29, 27.02, 20.04, 5.72, 0.04, 0.88
]
source_colors = ['#59778e', '#b1b9c6', '#8bb3af', '#baa29a', '#cce0df', '#e7c9a9']
plt.figure(figsize=(10, 10))
patches, texts, autotexts = plt.pie(
    source_sizes,
    labels=source_labels,
    autopct=lambda p: '{:.2f}%'.format(p) if p >= 5 else '',
    colors=source_colors
)
for text in texts + autotexts:
    text.set_fontsize(20)
plt.title('Traffic Sources')
plt.savefig(os.path.join(output_dir, 'source_pie.png'), bbox_inches='tight')
plt.close()

# 4. 竞争对手对比柱状图
competitor_labels = ['Meanwhile', 'evertas.com']
competitor_traffic = [1369, 3135]
plt.figure(figsize=(8, 6))
bars = plt.bar(competitor_labels, competitor_traffic, color=['#8bb3af', '#59778e'])
plt.ylabel('Estimated Traffic')
plt.xlabel('Website')
plt.title('Competitor Estimated Traffic (March 2025)')
plt.savefig(os.path.join(output_dir, 'competitor_bar.png'), bbox_inches='tight')
plt.close()