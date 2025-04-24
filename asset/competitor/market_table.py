import pandas as pd

# 假设tavily_market是一个包含竞争对手数据的DataFrame
tavily_market = pd.DataFrame({
    '公司名': ['Vellum AI', 'LlamaIndex', 'Flowise AI', 'Humanloop', 'n8n'],
    '主要业务/产品': [
        '无需编码的聊天机器人构建',
        '24/7实时响应与用户参与',
        '内部流程优化与团队生产力提升',
        '结合人工反馈提升模型性能',
        '低代码自动化与数据集成支持'
    ],
    '备注': [
        '适合非技术用户，降低技术门槛',
        '增强用户体验与满意度',
        '适用于高效的组织管理',
        '高质量的模型迭代过程',
        '适用于复杂的AI工作流'
    ]
})

# 保存为CSV文件
tavily_market.to_csv('asset/competitor/competitors.csv', index=False, encoding='utf-8-sig')