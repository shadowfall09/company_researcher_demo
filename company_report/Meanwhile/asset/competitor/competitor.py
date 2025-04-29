import os
import csv

# 假设 tavily_market 变量中保存了搜索整合后的市场分析内容
tavily_market = """
1. 主要竞争对手分析

Meanwhile作为全球首创的比特币计价终身寿险公司，目前市场上暂无完全同类型的直接竞争对手。主要竞争对手来自以下几类：

- 传统保险公司加密保险产品：多数保险巨头如Chubb、Allianz等涉足数字资产安全和交易所保险，但未提供以比特币计价的寿险产品。其产品多以法币计价，缺乏Meanwhile所具备的资产升值及税务优化优势。
- 数字资产保险创业公司：如Everest Re、Beazley等公司专注于数字资产托管和加密资产安全保障，但不涉及终身寿险领域，且缺乏AI驱动的承保和理赔数字化流程。
- 创新型金融科技公司：部分尝试将加密资产与传统金融产品结合，但多为结构化投资或理财产品，未涵盖保险保障功能。

综上，Meanwhile凭借独特的比特币计价保险产品及先进的数字化和AI技术应用，保持了市场先发优势和显著差异化竞争力。
"""

# 1. 检查是否有竞争对手信息
if "暂无完全同类型的直接竞争对手" in tavily_market and "主要竞争对手" in tavily_market:
    competitors = []
    # 分类下的公司名提取
    competitor_map = {
        "传统保险公司加密保险产品": {
            "公司": ["Chubb", "Allianz"],
            "主要业务/产品": "涉足数字资产安全和交易所保险，产品多以法币计价，未提供比特币计价寿险。",
            "备注": "传统保险巨头，未覆盖比特币寿险领域。"
        },
        "数字资产保险创业公司": {
            "公司": ["Everest Re", "Beazley"],
            "主要业务/产品": "专注于数字资产托管及加密资产安全保障，但未提供终身寿险。",
            "备注": "不涉及寿险且缺乏AI数字化流程。"
        },
        "创新型金融科技公司": {
            "公司": [],
            "主要业务/产品": "将加密资产与传统金融产品结合，多为结构化投资或理财，未涵盖保险保障功能。",
            "备注": "主要为金融/理财创新，未涉及保险保障。"
        }
    }

    for key, val in competitor_map.items():
        for name in val["公司"]:
            competitors.append({
                "公司名": name,
                "主要业务/产品": val["主要业务/产品"],
                "备注": val["备注"]
            })
        # 某些类别可能没有具体公司
        if not val["公司"]:
            competitors.append({
                "公司名": "无明确公司",
                "主要业务/产品": val["主要业务/产品"],
                "备注": val["备注"]
            })

    # 2. 构建保存路径
    output_dir = "company_report/Meanwhile/asset/competitor"
    os.makedirs(output_dir, exist_ok=True)

    # 3. 写入CSV
    csv_path = os.path.join(output_dir, "competitors.csv")
    with open(csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["公司名", "主要业务/产品", "备注"])
        writer.writeheader()
        for row in competitors:
            writer.writerow(row)
else:
    print("没有竞争对手")