import os
import matplotlib.pyplot as plt
import numpy as np

# Create directory for saving images
save_dir = 'company_report/Towns Protocol/asset/traffic'
os.makedirs(save_dir, exist_ok=True)

plt.rcParams.update({'font.size': 20, 'font.family': 'sans-serif'})

# ==== 1. MAU (simulate estimation if only total visits are known) ====
# Assume MAU (Monthly Active Users) for Jan, Feb, Mar are estimated as:
mau_months = ['Jan', 'Feb', 'Mar']
# Estimated from context: Visits per month divided by an average visits per user, e.g., 5
visits = [811324, 706571, 485421]
mau = [round(v/8) for v in visits]  # Use divisor for estimation

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(mau_months, mau, color='#729ECE', width=0.6)
ax.set_ylabel('Estimated MAU', fontsize=20)
ax.set_title('Estimated Monthly Active Users', fontsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
for i, v in enumerate(mau):
    ax.text(i, v+0.025*max(mau), f"{v:,}", ha='center', va='bottom')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'mau_bar.png'))
plt.close()

# ==== 2. Keywords ====
keywords = ['townsprotocol f', 'towns airdrop', 'towns', 'towns blokcchain', 'родіон єрошек']
search_volume = [40, 750, 18470, 20, 260]

fig, ax = plt.subplots(figsize=(14, 6))
bars = ax.bar(keywords, search_volume, color='#8FBC94', width=0.6)
ax.set_ylabel('Search Volume', fontsize=20)
ax.set_title('Main Keywords Search Volume', fontsize=20)
ax.set_xticklabels(keywords, rotation=25)
ax.tick_params(axis='x', labelsize=18)
ax.tick_params(axis='y', labelsize=20)
for i, v in enumerate(search_volume):
    ax.text(i, v+0.025*max(search_volume), f"{v:,}", ha='center', va='bottom')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'keyword_bar.png'))
plt.close()

# ==== 3. Main Countries ====
countries = ['Russia', 'Ukraine', 'Japan', 'USA', 'Netherlands']
country_share = [25.43, 11.82, 9.04, 7.24, 5.45]
# Hide text for wedges <5%
def pct_func(pct):
    return ('%.1f%%' % pct) if pct >= 5 else ''

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#A0CBE8', '#C6D685', '#FFB884', '#9D97CB', '#FFD2A6']
wedges, texts, autotexts = ax.pie(country_share, labels=countries, autopct=pct_func, colors=colors, textprops={'fontsize': 20})
ax.set_title('Main Visiting Countries', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'country_pie.png'))
plt.close()

# ==== 4. Traffic Sources ====
sources = ['Direct', 'Referrals', 'Organic Search', 'Social', 'Email', 'Ads']
source_share = [69.29, 6.44, 15.28, 8.37, 0.10, 0.52]
fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#82B0D2', '#8ADAC7', '#FFD880', '#E88572', '#B299E2', '#C4D6D3']
wedges, texts, autotexts = ax.pie(source_share, labels=sources, autopct=pct_func, colors=colors, textprops={'fontsize': 20})
ax.set_title('Traffic Sources', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'source_pie.png'))
plt.close()

# ==== 5. Social Media Sources ====
social_media = ['Twitter', 'YouTube', 'Discord', 'Telegram', 'VKontakte']
media_share = [44.93, 27.20, 18.51, 8.42, 0.89]
fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#9ACEEB', '#A2E8CB', '#FBC398', '#CCB8E2', '#A7D0CD']
wedges, texts, autotexts = ax.pie(media_share, labels=social_media, autopct=pct_func, colors=colors, textprops={'fontsize': 20})
ax.set_title('Social Media Sources', fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'social_media_pie.png'))
plt.close()

# ==== 6. Competitors ====
competitors = ['warpcast.com', 'opensea.io', 'debank.com', 'guild.xyz']
visit_share = [78.94, 10, 7, 4]  # Adjusted based on report context
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(competitors, visit_share, color='#E7ACD6', width=0.6)
ax.set_ylabel('Share (%)', fontsize=20)
ax.set_title('Top Competitors (Estimated Share)', fontsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
for i, v in enumerate(visit_share):
    if v > 5:
        ax.text(i, v+0.5, f"{v:.1f}%", ha='center', va='bottom')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'competitors_bar.png'))
plt.close()

# ==== 7. Age Groups ====
age_labels = ['25-34', '18-24', '35-44', '45-54', '55-64', '65+']
age_share = [72.56, 14.09, 10.00, 2.53, 0.50, 0.32]
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(age_labels, age_share, color='#A6CFD5', width=0.6)
ax.set_ylabel('Percentage (%)', fontsize=20)
ax.set_title('User Age Distribution', fontsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
for i, v in enumerate(age_share):
    if v > 2:
        ax.text(i, v+0.5, f"{v:.2f}%", ha='center', va='bottom')
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'age_bar.png'))
plt.close()