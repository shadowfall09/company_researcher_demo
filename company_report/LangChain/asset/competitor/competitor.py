import os
import pandas as pd

# 假设 tavily_market 是一个包含前述内容的长文本变量
tavily_market = """
- **Semantic Kernel**  
  由微软支持的开源轻量级SDK，支持多语言编程，专注于模块化集成AI功能，特别适合微软生态系统客户。其高度模块化和多语言支持使其在企业级深度定制中具备优势。

- **AutoChain**  
  一款由Forethought AI推出的轻量且易用的AI框架，强调多模型协同和自动化流程，特别在智能客服和智能代理领域有较强竞争力。

- **IBM watsonx**  
  IBM推出的企业级AI平台，提供包含LLM定制、微调与数据集成能力，注重企业安全合规，覆盖广泛行业，是传统大型企业的首选。

- **Haystack**  
  开源NLP框架，主攻智能搜索和基于检索的生成（RAG），以高度定制化及模型无缝融合著称，适合科研和企业内部知识管理系统。

- **Flowise AI**  
  低代码/无代码平台，提供可视化设计界面，降低非开发者团队门槛，适合快速构建和部署大型语言模型应用。
"""

import re

def extract_competitors(text):
    pattern = r'- \*\*(.*?)\*\*[\s\S]+?(?=- \*\*|$)'
    matches = re.findall(pattern, text)
    competitors = []
    split_lines = text.split('\n')
    current_name = None
    desc = []
    for line in split_lines:
        # 判断公司名
        m = re.match(r'- \*\*(.*?)\*\*', line)
        if m:
            # 推入上一个
            if current_name:
                competitors.append({'公司名': current_name, '主要业务/产品': ''.join(desc).strip()})
            current_name = m.group(1)
            desc = []
        elif line.strip() and current_name:
            desc.append(line.strip())
    # 最后一个
    if current_name:
        competitors.append({'公司名': current_name, '主要业务/产品': ''.join(desc).strip()})
    
    # 增加备注，可以结合主要业务简单分析
    for comp in competitors:
        remark = ""
        if "微软" in comp['主要业务/产品']:
            remark = "微软官方，支持多语言，企业级定制优势"
        elif "Forethought" in comp['主要业务/产品']:
            remark = "智能客服、智能代理领域有较强竞争力"
        elif "IBM" in comp['主要业务/产品']:
            remark = "行业公认的企业级AI平台，合规与数据集成优势"
        elif "NLP" in comp['主要业务/产品'] or "检索" in comp['主要业务/产品']:
            remark = "专注智能搜索与RAG，适合知识管理"
        elif "低代码" in comp['主要业务/产品'] or "可视化" in comp['主要业务/产品']:
            remark = "低门槛，适合快速搭建"
        comp['备注'] = remark
    return competitors

competitors = extract_competitors(tavily_market)

df = pd.DataFrame(competitors, columns=['公司名', '主要业务/产品', '备注'])

save_dir = 'company_report/LangChain/asset/competitor'
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, 'competitors.csv')
df.to_csv(save_path, index=False, encoding='utf-8-sig')