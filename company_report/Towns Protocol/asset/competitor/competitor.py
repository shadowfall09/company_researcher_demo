import os
import pandas as pd
import re

# 假设tavily_market内容已以字符串形式加载到tavily_market变量
tavily_market = """
1. 主要竞争对手详细介绍

- **Farcaster**  
  Farcaster是一个去中心化的社交协议，强调用户对身份和数据的自主控制。它由著名风险投资机构a16z支持，侧重于开放的身份和内容生态系统。与Towns Protocol相比，Farcaster更注重开放的身份认证机制和内容生态，而Towns则在实时通信和社区治理的“Spaces”功能上具备差异化优势。   
  来源：[TheBlockBeats 2025年3月20日](https://www.theblockbeats.info/en/news/35199)

- **Discord（潜在竞争对手）**  
  虽然Discord并非基于区块链的应用，但作为目前主流的实时通讯及社区管理平台，其庞大用户基础和成熟的运营模式对Towns构成潜在威胁。Discord在用户体验和社区构建上有显著优势，而Towns通过去中心化技术为用户提供更强的数据主权和隐私保护。  
  来源：[Gate.io 2025年2月28日](https://www.gate.io/learn/articles/a16z-leads-coinbase-follows-how-towns-is-reshaping-the-economic-model-of-web3-social/8352)

- **Houseparty**  
  Houseparty由Towns团队的创始成员开发，虽非直接竞争对手，但其技术积累和用户体验设计为Towns带来了重要的产品开发优势。Houseparty更多聚焦于即时通讯娱乐社交领域，Towns则强调去中心化和社区治理两大核心。  
  来源：[TechCrunch 2025年2月23日](https://techcrunch.com/2023/02/23/towns-protocol-app-ben-rubin)

- **其他Web3社交协议（如Status、Mastodon）**  
  这些协议也在推动去中心化社区和通信的发展，尤其注重用户数据所有权和社区自治。不过，Towns依托以太坊Layer 2智能合约和分布式流节点技术，在扩展性和实时通讯效率方面具备一定技术优势。  
  来源：[Panewslab 2025年3月15日](https://www.panewslab.com)
"""

def extract_competitors(text):
    competitor_list = []
    # 匹配条目
    pattern = re.compile(r"- \*\*(.+?)\*\*((.|\n)*?)(?:来源|$)")
    matches = pattern.finditer(text)
    for match in matches:
        full_name = match.group(1).strip()
        details = match.group(2).strip().replace('\n', '')
        # 提取名称和可能的备注
        name = full_name
        remark = ""
        if '（' in full_name and '）' in full_name:
            name = full_name.split('（')[0]
            remark = full_name.split('（')[1].split('）')[0]
        # 提取主要业务/产品
        product = ""
        for s in details.split('。'):
            if '协议' in s or '平台' in s or '应用' in s or '领域' in s or '生态系统' in s:
                product = s + '。'
                break
        # 补充备注
        if not remark:
            # 备注找带有“非直接竞争对手”或“也在推动”的描述
            if '虽非直接竞争对手' in details:
                remark = '非直接竞争对手'
            elif '也在推动' in details or '协议' in full_name:
                remark = '行业同类去中心化社交协议'
        competitor_list.append({
            '公司名': name,
            '主要业务或产品': product if product else details,
            '备注': remark
        })
    return competitor_list

competitors = extract_competitors(tavily_market)
df = pd.DataFrame(competitors)

os.makedirs('company_report/Towns Protocol/asset/competitor', exist_ok=True)
df.to_csv('company_report/Towns Protocol/asset/competitor/competitors.csv', index=False, encoding='utf-8-sig')