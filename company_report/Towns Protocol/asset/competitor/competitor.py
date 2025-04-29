import pandas as pd
import os

# 假设 tavily_market 为列表，包含各竞争对手信息
tavily_market = [
    {
        "公司名": "Farcaster",
        "主要业务/产品": "去中心化社交网络协议，强调用户身份、数据自主权和抗审查，支持多客户端生态。",
        "备注": "开放性和可组合性强，吸引开发者扩展生态。"
    },
    {
        "公司名": "Bluesky",
        "主要业务/产品": "基于自主协议的去中心化社交项目，通过开放协议架构实现分布式数据存储与内容审核。",
        "备注": "由Twitter联合创始人Jack Dorsey支持，致力连接普通用户与Web3世界。"
    },
    {
        "公司名": "Status",
        "主要业务/产品": "融合去中心化通信、加密钱包和DApp入口，提供端到端加密即时通讯。",
        "备注": "服务区块链生态用户，定位去中心化多功能移动平台。"
    },
    {
        "公司名": "Lens Protocol",
        "主要业务/产品": "基于Polygon的去中心化社交图谱协议，用户可拥有内容和社交关系所有权。",
        "备注": "强调创作者经济和社区治理，推动链上内容货币化。"
    }
]

# 构建DataFrame
df = pd.DataFrame(tavily_market)

# 目录创建
output_dir = 'company_report/Towns Protocol/asset/competitor'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'competitors.csv')

# 保存为csv
df.to_csv(output_path, index=False, encoding='utf-8-sig')