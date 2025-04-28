import pandas as pd

# 假设 tavily_market 数据结构如下（示例数据，实际请替换成真实查询结果）
tavily_market = [
    {
        "公司名": "Meta（Ray-Ban Stories）",
        "主要业务或产品": "Ray-Ban智能眼镜，集成拍照、音频通话及智能助手，强调时尚与便携。",
        "备注": "与Ray-Ban合作，市场接受度高，功能基础但集成度高，聚焦C端用户。"
    },
    {
        "公司名": "Microsoft（HoloLens 系列）",
        "主要业务或产品": "HoloLens 混合现实头显，面向企业级应用，强调增强现实与空间交互。",
        "备注": "行业先行者，主要在工业、医疗和教育领域应用，设备较为笨重。"
    },
    {
        "公司名": "North（Focals 已被Google收购）",
        "主要业务或产品": "Focals 智能眼镜，利用全息显示技术，显示功能有限。",
        "备注": "2019年被Google收购，现已停产，曾专注轻便型智能眼镜方向。"
    },
    {
        "公司名": "Solos（AirGo Vision）",
        "主要业务或产品": "AirGo Vision 运动智能眼镜，专注于运动数据记录与语音交互。",
        "备注": "设计轻巧，主要面向运动健身爱好者，功能相对单一，定位垂直市场。"
    }
]

# 转为DataFrame
df = pd.DataFrame(tavily_market)

# 创建输出路径
import os
output_dir = 'asset/competitor'
os.makedirs(output_dir, exist_ok=True)

# 保存为CSV
df.to_csv(os.path.join(output_dir, 'competitors.csv'), index=False, encoding='utf-8-sig')