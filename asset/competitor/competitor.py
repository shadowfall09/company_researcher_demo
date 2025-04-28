import os
import csv

# 假设 tavily_market 是已存在的字典数据，结构如下:
tavily_market = {
    "competitors": [
        {
            "name": "Two Hat Security",
            "business": "利用机器学习技术进行在线内容过滤和社区管理，帮助社交平台及游戏社区维护健康网络环境。",
            "note": "专注内容审核，全球知名。"
        },
        {
            "name": "ActiveFence",
            "business": "采用人工智能和大数据提供在线威胁检测与虚假信息识别，防御网络恶意行为和虚假内容。",
            "note": "国际领先的内容安全服务商。"
        },
        {
            "name": "Cyabra",
            "business": "通过AI技术检测虚假信息、社交机器人和恶意操纵，保护品牌声誉，实时监测网络风险。",
            "note": "以深度舆情分析著称，服务全球知名品牌。"
        },
        {
            "name": "Graphika",
            "business": "专注社交媒体分析与可视化，帮助客户识别信息传播模式及网络威胁，提升风险管理能力。",
            "note": "在信息传播溯源与网络分析领域有突出表现。"
        },
        {
            "name": "Alethea Group",
            "business": "提供信息安全与虚假信息检测方案，为政府和企业客户提供风险评估和策略支持。",
            "note": "原名LCK Strategies，美政府等为其主要客户。"
        }
    ]
}

# 创建目标存储路径
save_dir = 'company_report/blackbird/asset/competitor'
os.makedirs(save_dir, exist_ok=True)
csv_path = os.path.join(save_dir, 'competitors.csv')

# 写入CSV
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['公司名', '主要业务/产品', '备注'])
    for comp in tavily_market['competitors']:
        writer.writerow([comp['name'], comp['business'], comp['note']])