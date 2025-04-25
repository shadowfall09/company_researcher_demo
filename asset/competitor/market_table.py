import pandas as pd
import os

# 示例：tavily_market基础数据结构（实际应从Tavily搜索结果中获取）
tavily_market = [
    {
        "company": "Meta (Oculus)",
        "business": "增强现实（AR）与虚拟现实（VR）产品；推出多款智能眼镜，强调互动和元宇宙体验。",
        "remark": "依托社交平台及技术生态，财力雄厚，拥有广泛用户基础。"
    },
    {
        "company": "Snap Inc. (Spectacles)",
        "business": "主打社交与娱乐功能的智能眼镜，设计时尚，面向年轻用户。",
        "remark": "注重轻便和即时分享体验，品牌影响力强于年轻群体。"
    },
    {
        "company": "Google (Google Glass Enterprise Edition)",
        "business": "面向企业和专业领域的AR眼镜，强调工业、医疗等场景的工作辅助。",
        "remark": "产品稳定性高，实用性强，在B端市场有较好口碑。"
    },
    {
        "company": "Vuzix",
        "business": "聚焦工业级AR眼镜，广泛应用于制造、仓储、物流等行业。",
        "remark": "专注B端市场，客户基础成熟，技术迭代快。"
    }
]

# 转换为DataFrame
df = pd.DataFrame(tavily_market, columns=["company", "business", "remark"])

# 保存路径
output_dir = "asset/competitor"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "competitors.csv")

# 保存为csv，utf-8编码，带列名
df.to_csv(output_file, index=False, encoding="utf-8")