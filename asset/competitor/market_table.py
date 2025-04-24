import pandas as pd

# 假设tavily_market是一个包含竞争对手数据的字典列表
tavily_market = [
    {'公司名': 'Semantic Kernel', '主要业务/产品': '多语言支持和自动编排AI插件', '备注': '适合需要跨语言开发的团队'},
    {'公司名': 'AutoChain', '主要业务/产品': '轻量级和可扩展的快速应用开发', '备注': '结构简洁，功能不及LangChain丰富'},
    {'公司名': 'HuggingFace Transformers', '主要业务/产品': '预训练模型和活跃社区', '备注': '不及LangChain在链式调用和集成方面'},
    {'公司名': 'Flowise AI', '主要业务/产品': '低代码平台', '备注': '适合非技术人员快速搭建'}
    # 添加其他竞争对手数据...
]

# 创建DataFrame
df = pd.DataFrame(tavily_market)

# 保存为CSV文件
df.to_csv('asset/competitor/competitors.csv', index=False, encoding='utf-8-sig')