import os
import matplotlib.pyplot as plt
import numpy as np

# 创建文件夹
save_dir = 'company_report/LangChain/asset/traffic'
os.makedirs(save_dir, exist_ok=True)

plt.rcParams.update({'font.size': 20})

# ========== MAU：无单一月活数据，故省略 ==========

# ========== 关键词（柱状图） ==========
keywords = ['langchain', 'langgraph', 'langsmith', 'langchain js', 'langraph']
search_volume = [314780, 102560, 59270, 11870, 12110]

fig, ax = plt.subplots(figsize=(10,6))
bars = ax.bar(keywords, search_volume, color='#729ECE')
ax.set_ylabel('Search Volume', fontsize=20)
ax.set_title('Top Keywords by Search Volume', fontsize=20)
ax.tick_params(axis='x', labelrotation=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'keywords_bar.png'))
plt.close()

# ========== 主要访问国家（饼图） ==========
country_labels = ['United States', 'China', 'India', 'South Korea', 'Hong Kong']
country_perc = [19.31, 16.80, 11.76, 5.13, 4.92]  # total > 95%，剩余不单独列

# 其它
others = 100 - sum(country_perc)
if others > 0:
    country_labels.append('Others')
    country_perc.append(others)

def autopct_func(pct):
    return ('%.1f%%' % pct) if pct >= 5 else ''

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(country_perc, labels=country_labels, autopct=autopct_func,
                                  startangle=140, colors=['#729ECE', '#8AD6CC', '#FFB878', '#E06767', '#A38F7C', '#B4B4B4'])
for autot in autotexts:
    autot.set_fontsize(20)
for txt in texts:
    txt.set_fontsize(20)
ax.set_title('Visitor Country Distribution', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'country_pie.png'))
plt.close()

# ========== 流量来源（饼图） ==========
source_labels = ['Organic Search', 'Direct', 'Referral', 'Social', 'Paid Search', 'Mail', 'Ads']
source_perc = [51.91, 40.98, 6.16, 0.80, 0.008, 0.04, 0.10]

# 合并小于5%的为Others
filtered_labels, filtered_perc = [], []
others_source = 0

for l, v in zip(source_labels, source_perc):
    if v >= 5:
        filtered_labels.append(l)
        filtered_perc.append(v)
    else:
        others_source += v

if others_source > 0:
    filtered_labels.append('Others')
    filtered_perc.append(others_source)

fig, ax = plt.subplots(figsize=(10,8))
wedges, texts, autotexts = ax.pie(filtered_perc, labels=filtered_labels, autopct=autopct_func,
                                  startangle=80, colors=['#729ECE','#8AD6CC','#FFB878','#E06767','#B4B4B4'])
for autot in autotexts:
    autot.set_fontsize(20)
for txt in texts:
    txt.set_fontsize(20)
ax.set_title('Traffic Sources Breakdown', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'traffic_source_pie.png'))
plt.close()

# ========== 社交媒体来源（柱状图） ==========
social_labels = ['Reddit', 'YouTube', 'Linkedin', 'X', 'Facebook']
social_perc = [35.26, 30.47, 11.82, 11.68, 3.13]

fig, ax = plt.subplots(figsize=(10,6))
bars = ax.bar(social_labels, social_perc, color='#8AD6CC')
ax.set_ylabel('Visitor %', fontsize=20)
ax.set_title('Social Media Sources', fontsize=20)
ax.set_ylim([0, max(social_perc) + 5])
for i, v in enumerate(social_perc):
    if v > 5:
        ax.text(i, v + 1, f'{v:.1f}%', ha='center', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'social_source_bar.png'))
plt.close()

# ========== 竞争对手（柱状图-对数Y轴） ==========
competitor_domains = ['github.com', 'stackoverflow.com', 'claude.ai', 'ollama.com', 'pypi.org', 'langchain-ai.github.io']
competitor_visits = [521149929, 112795947, 101105053, 7814190, 5752103, 1072934]

fig, ax = plt.subplots(figsize=(14,7))
bars = ax.bar(competitor_domains, competitor_visits, color='#FFB878')
ax.set_ylabel('Visits (log scale)', fontsize=20)
ax.set_yscale('log')
ax.set_title('Top Competitor Total Visits', fontsize=20)
plt.xticks(rotation=15, fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'competitors_bar.png'))
plt.close()

# ========== 年龄段分布（柱状图） ==========
age_labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
age_perc = [20.84, 44.08, 17.55, 10.52, 4.47, 2.54]

fig, ax = plt.subplots(figsize=(12,7))
bars = ax.bar(age_labels, age_perc, color='#E06767')
ax.set_ylabel('User %', fontsize=20)
ax.set_title('User Age Distribution', fontsize=20)
for i, v in enumerate(age_perc):
    if v > 5:
        ax.text(i, v + 1, f'{v:.1f}%', ha='center', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'age_bar.png'))
plt.close()