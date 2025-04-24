import pandas as pd

# 创建竞争对手数据
competitors_data = [
    {"公司名": "SuperAGI", "主要业务/产品": "开源框架，专注于多代理自主AI系统", "备注": "适用于复杂AI工作流自动化"},
    {"公司名": "Flowise", "主要业务/产品": "可视化开发环境", "备注": "便于快速搭建AI代理"},
    {"公司名": "Langflow", "主要业务/产品": "可视化开发环境", "备注": "便于快速搭建AI代理"},
    {"公司名": "Rivet", "主要业务/产品": "TypeScript库", "备注": "桥接可视化编程与代码集成"},
    {"公司名": "Klu.ai", "主要业务/产品": "统一API接口", "备注": "管理多种大型语言模型"},
    {"公司名": "Humanloop", "主要业务/产品": "协作和评估平台", "备注": "促进LLM应用的性能优化"},
    {"公司名": "HoneyHive AI", "主要业务/产品": "监控和调试工具", "备注": "提升LLM应用的稳定性"},
    {"公司名": "Pipe Agents", "主要业务/产品": "API集成工具", "备注": "串联超过100个LLM"},
    {"公司名": "Braintrust", "主要业务/产品": "开发管理平台", "备注": "快速原型和实时监控支持"}
]

# 转换为DataFrame
df_competitors = pd.DataFrame(competitors_data)

# 保存为CSV文件
output_path = 'asset/competitor/competitors.csv'
df_competitors.to_csv(output_path, index=False, encoding='utf-8-sig')