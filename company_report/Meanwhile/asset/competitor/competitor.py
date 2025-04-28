import os
import pandas as pd

# 模拟 tavily_market 数据结构（实际应替换为你的实际数据变量）
tavily_market = [
    {
        '公司名': 'Uncommon',
        '主要业务/产品': '专注于数字资产保险，尤其是加密钱包和交易所保险，聚焦于数字资产保护和风险防范。',
        '备注': '尚未推出以比特币计价的寿险产品，在数字资产保险领域有一定影响力。'
    },
    {
        '公司名': 'Etherisc',
        '主要业务/产品': '基于区块链的去中心化保险平台，涵盖农业保险、航班延误保险等，利用智能合约自动理赔。',
        '备注': '暂未专注于寿险，但技术创新对行业有借鉴意义。'
    },
    {
        '公司名': 'New York Life',
        '主要业务/产品': '传统寿险巨头，业务涵盖寿险、财险、资产管理等，正在探索数字资产和加密货币相关保险应用。',
        '备注': '具备深厚资本和客户基础，未来可能进入比特币计价寿险领域。'
    },
    {
        '公司名': 'Block Green',
        '主要业务/产品': '专注比特币投资和流动性管理，为数字资产生态提供金融支持。',
        '备注': 'Meanwhile的合作伙伴，未来可能独立拓展数字资产保险市场。'
    }
]

# 保存路径
save_dir = 'company_report/Meanwhile/asset/competitor'
os.makedirs(save_dir, exist_ok=True)

# 转换为 DataFrame
df = pd.DataFrame(tavily_market, columns=['公司名', '主要业务/产品', '备注'])

# 保存为 csv 文件（编码为utf-8-sig以保证中文友好性）
csv_path = os.path.join(save_dir, 'competitors.csv')
df.to_csv(csv_path, index=False, encoding='utf-8-sig')

print(f'数据已保存到：{csv_path}')