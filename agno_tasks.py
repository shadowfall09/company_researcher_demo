from src.non_mcp_tools.similar_web import get_traffic_by_domain
from src.mcp_servers.servers.tavily_prompt_template import *
from typing import Any, List

class AgnoTask:
    def __init__(self, task_id: str, MCP_tool, instructions: str, advanced_response: bool = False, context: List["AgnoTask"] = None) -> None:
        self.task_id = task_id
        self.MCP_tool = MCP_tool
        self.instructions = instructions
        self.context = context
        self.response = None
        # 是否使用高级模型
        self.advanced_response = advanced_response

# Tasks
def target_company_task(company_url: str, MCP_tool: Any):
    target_company = AgnoTask(
        task_id = "target_company",
        instructions ="仅使用get_company_info（只需要调用一次）来搜索, " + company_url +
        "是一家什么样的公司？详细介绍一下。（不要加图片，markdown格式，标题：xx公司介绍。总分结构，重点部分请加粗）",
        MCP_tool=MCP_tool
    )
    return target_company


def same_name_company_task(company_name: str, MCP_tool: Any, context: List[AgnoTask]):
    same_name_company = AgnoTask(
        task_id = "same_name_company",
        instructions ="仅调用一次 get_company_same_name，搜索所有名为 "+company_name +
        " 的公司。请根据搜索结果合并公司（多个结果是一家公司在不同平台上的展示），列出合并后每家公司的名称及简短简介，并排除与 target_company 描述相符的公司。",
        MCP_tool=MCP_tool,
        context=context
    )
    return same_name_company


def traffic_task(company_url: str, company_name: str):
    traffic_data = get_traffic_by_domain(company_url)

    traffic = AgnoTask(
        task_id = "traffic",
        instructions="""根据 """ + company_name + """ 的网站数据(traffic_data)，请你进行详细分析：\
        ”基本信息“，”流量总体情况“，”MAU“，“关键词”，“主要访问国家”，“流量来源”，“社交媒体来源”，“竞争对手”，“年龄段”等分析（如果某一项没有数据就不用分析）。\
        （markdown格式，重点部分请加粗）""",
        MCP_tool=None,
        context=[{"traffic_data": traffic_data}]
    )
    return traffic


def linkedin_task(company_url: str, company_name: str, MCP_tool: Any, context: List[AgnoTask]):
    linkedin = AgnoTask(
        task_id = "linkedin",
        instructions="""Use get_company_linkedin to search for the relevant LinkedIn profile of """ + company_url + """. Based on the information found:
    1. Read `target_company` carefully. If `get_company_linkedin` tool returns norhing, reply ‘没有找到相关资料’ and end your reply. If `get_company_linkedin` tool result doesn't match `target_company`'s description or doesn't contain linkedin link, reply ‘没有找到相关资料’ and end your reply. Otherwise, proceed(no need to mention this step).
    2. If no info unavailable, ignore this step. Don't make up information! If else, provide the company's LinkedIn profile link and summarize the content. Don't mention Financing Information.
    3. If no info unavailable, ignore this step. Don't make up information! If else, Use get_company_linkedin_detail to supplement Step 2 with company details (e.g., founding year, headquarters, industry, size).
    4. If no info unavailable, ignore this step. Don't make up information! If else, also use get_company_linkedin_detail to retrieve multiple founders/CEO/employees information.
        •	If found, list LinkedIn links, current positions, past positions, and education history. Summarize the strengths of the founders/CEO/employees.
        •	If not found, state “没有搜到创始人信息”。
    (Search in English, answer in Chinese. Answer Title: """+company_name+""" LinkedIn资料。 Use Markdown, structured format, highlight key points in bold, and do not mention the tools used.)""",
        MCP_tool=MCP_tool,
        context=context
    )
    return linkedin


def sns_task(company_name: str, MCP_tool: Any, context: List[AgnoTask]):
    sns = AgnoTask(
        task_id = "social_media",
        MCP_tool=MCP_tool,
        instructions="""使用get_company_social_media来搜索 """+company_name + """公司的社交媒体信息。（搜索时用英语）\
        搜索后请判断get_company_social_media搜索结果是否与target company业务相关，忽略不相关的内容（尤其是和same_name_company中同名公司相关的内容）。
        1.请总结**相关的**twitter、reddit的帖子都关于什么（分别写一段话）。\
        2.如果有**本公司的**github账号，介绍一下账号的链接，数据，简介，展示star history图片。非本公司的不要（根据readme判断）。\
        3.罗列"""+company_name+""" 的每个社交媒体账号（twitter，youtube，reddit）和最近的几条动态（提供链接）。\
        （markdown格式，标题："""+company_name+""" 相关社交媒体。总分结构，重点部分请加粗，不用提及用了什么工具）""",
        context=context
    )
    return sns


def hiring_task(company_url: str, MCP_tool: Any, context: List[AgnoTask]):
    hiring = AgnoTask(
        task_id = "hiring",
        instructions="""仅使用Apify_hiring和get_company_hiring（只需要调用一次）获取 """+company_url + """的招聘情况。\
        注意：首先请研读 target_company，判断Apify_hiring和get_company_hiring搜索出的职位是否与其主营业务相关，忽略非本公司的职位（尤其是和same_name_company中同名公司相关的职位）。
        如果有相关的岗位（没有就说暂无相关的），岗位职责分别是什么？待遇如何？提供来源链接（最多展示5个岗位）\
        （markdown格式，标题： xx公司招聘情况。总分结构，重点部分请加粗，不用提及用了什么工具）""",
        MCP_tool=MCP_tool,
        context=context
    )
    return hiring


def financial_task(company_url: str, MCP_tool: Any, context: List[AgnoTask]):
    financial = AgnoTask(
        task_id = "financial",
        instructions="仅使用get_company_financial（只需要调用一次）来搜索"+company_url + "的财务情况。\
        注意：首先请研读 target_company，判断get_company_financial搜索出的财务信息是否与其主营业务相关，忽略不相关的信息（尤其是和same_name_company中同名公司相关的财务信息）。\
        如果有相关信息就介绍一下公司的融资情况、财务报表等；没有的话就说没有；提供所有信息的来源链接",
        MCP_tool=MCP_tool,
        context=context
    )
    return financial


def tavily_financial_task(company_url: str, MCP_tool: Any, context: List[AgnoTask]):
    tavily_financial = AgnoTask(
        task_id = "tavily_financial",
        instructions=tavily_search_system_prompt.format(prompt=tavily_financial_prompt.format(
            company=company_url), company=company_url),
        MCP_tool=MCP_tool,
        context=context
    )
    return tavily_financial


def financial_summary_task(company_name: str, context: List[AgnoTask]):
    financial_summary = AgnoTask(
        task_id = "financial_summary",
        instructions="做详细的介绍， "+company_name + "的财务情况。包括融资情况，财务报表，未来计划等。（markdown格式，标题：" +
        company_name+" 财务情况。提供所有信息的来源链接，重点部分请加粗）"
        "注意：请研读 target_company，判断搜索出的财务信息是否与其主营业务相关，忽略不相关的信息（尤其是same_name_company中同名公司相关的财务信息）。",
        MCP_tool=None,
        context=context
    )
    return financial_summary


def tavily_market_task(company_name: str, MCP_tool: Any, context: List[AgnoTask]):
    tavily_market = AgnoTask(
        task_id = "tavily_market",
        instructions=tavily_search_system_prompt.format(prompt=tavily_market_prompt.format(
            company=company_name), company=company_name)+"（markdown格式，标题："+company_name+" 市场情况。提供所有信息的来源链接，重点部分请加粗）",
        MCP_tool=MCP_tool,
        context=context
    )
    return tavily_market


def tavily_news_task(company_name: str, MCP_tool: Any, context: List[AgnoTask]):
    tavily_news = AgnoTask(
        task_id = "tavily_news",
        instructions=tavily_search_system_prompt.format(prompt=tavily_news_prompt.format(
            company=company_name), company=company_name),
        MCP_tool=MCP_tool,
        context=context
    )
    return tavily_news


def news_summary_task(company_name: str, context: List[AgnoTask]):
    news_summary = AgnoTask(
        task_id = "news_summary",
        instructions=company_name + "最近有什么新闻和合作？详细介绍，标注时间，网页链接，过滤掉半年以前的新闻。（markdown格式，标题：" +
        company_name+" 近期新闻。每条新闻标题尽量中文，重点部分请加粗）"
        "注意：请研读 target_company，判断搜索出的新闻是否与其主营业务相关，忽略不相关的信息（尤其是same_name_company中同名公司相关的新闻）。",
        MCP_tool=None,
        context=context
    )
    return news_summary


# Plotting
def traffic_plot_task(traffic: str, traffic_folder: str):
    traffic_plot = AgnoTask(
        task_id = "traffic_plot",
        advanced_response=True,
        instructions="从traffic中提取”MAU“，“关键词”，“主要访问国家”，“流量来源”，“社交媒体来源”，“竞争对手”，“年龄段”等数据（若没有数据则忽略，不用画图），选择多种合适的图表形式（饼图、柱状图），利用matplotlib绘图（保存多个文件，不要用高饱和色调，饼图小于5%的不要显示文字；文字用英语，字号20），保存图片到'" +
        traffic_folder+"'。注意：只输出代码，不加```python```",
        MCP_tool=None,
        context=[traffic]
    )
    return traffic_plot


def competitor_table_task(tavily_market: str, competitor_folder: str):
    market_table = AgnoTask(
        task_id = "competitor_table",
        advanced_response=True,
        instructions="用python实现，从tavily_market中提取竞争对手数据，包含公司名，主要业务/产品，备注等,详细一些，中文为主，保存成competitors.csv到'" +
        competitor_folder+"'。如果没有竞争对手数据，就输出\"没有竞争对手\"，不用写代码。注意：只输出代码，不加```python```",
        MCP_tool=None,
        context=[tavily_market]
    )
    return market_table
