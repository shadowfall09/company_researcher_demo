from agno.agent import Agent
from agno.models.openrouter import OpenRouter
import asyncio

from agno.agent import Agent
from agno.tools.mcp import MultiMCPTools
from src.mcp_servers.mcp_server_class import *
from utils import *
from agno_tasks import *
import time
import argparse

import logging
logger = logging.getLogger(__name__)

DEBUG = False
ADVANCED_MODEL = "gpt-4.1"
MODEL = "gpt-4.1-mini"

    
async def run_mcp_agent(task: AgnoTask):
    instructions = task.instructions
    if not task.context:
        context = ""
    else:
        context = []
        for atask in task.context:
            if isinstance(atask, dict):
                context.append(atask)
            else:
                context.append({atask.task_id: atask.response})
        context = " <context_spliter> ".join(str(item) for item in context)
    if task.MCP_tool:
        commands = []
        env = {}
        for mcp_tool in task.MCP_tool:
            commands.append(mcp_tool.command+" "+' '.join(mcp_tool.args))
            if hasattr(mcp_tool, "env"):
                env.update(mcp_tool.env)
        async with MultiMCPTools(commands = commands,env = env) as mcp_tools:
            agent = Agent(
                model=OpenRouter(MODEL if not task.advanced_response else ADVANCED_MODEL, max_tokens=4096),
                tools=[mcp_tools],
                instructions=instructions,
                markdown=True,
                show_tool_calls=True,
            )
            await agent.aprint_response(context,show_message=False)
            task.response = agent.run_response.content
    else:
        agent = Agent(
            model=OpenRouter(MODEL if not task.advanced_response else ADVANCED_MODEL, max_tokens=4096),
            instructions=instructions,
            markdown=True,
            show_tool_calls=True,
        )
        await agent.aprint_response(context,show_message=False)
        task.response = agent.run_response.content


def main(company_name: str, company_url: str):
    
    start_time = time.time()
    
    # 确保目录存在
    base_dir = "company_report/" + company_name
    traffic_folder = base_dir+"/asset/traffic"
    competitor_folder = base_dir+"/asset/competitor"
    ensure_dir(base_dir)
    empty_folder(traffic_folder)
    empty_folder(competitor_folder)
    
    info_json = {"company_name": company_name, "company_url": company_url}
    
    # 截图
    if not DEBUG:
        screenshot(base_dir, company_url)
    
    # 任务定义
    target_company = target_company_task(company_url, [GaorongvcMCP])
    if not DEBUG:
        traffic = traffic_task(company_url, company_name)
    same_name_company = same_name_company_task(company_name, [GaorongvcMCP], [target_company])
    linkedin = linkedin_task(company_url, company_name, [GaorongvcMCP], [target_company,info_json])
    sns = sns_task(company_name, [GaorongvcMCP], [target_company,same_name_company,info_json])
    hiring = hiring_task(company_url, [GaorongvcMCP, Apify_hiring], [target_company,same_name_company,info_json])
    tavily_financial = tavily_financial_task(company_url, [tavily], [target_company,same_name_company,info_json])
    financial_summary = financial_summary_task(company_name, [target_company, same_name_company, tavily_financial,info_json])
    tavily_market = tavily_market_task(company_name, [tavily], [target_company, same_name_company,info_json])
    tavily_news = tavily_news_task(company_name, [tavily], [target_company, same_name_company,info_json])
    news_summary = news_summary_task(company_name, [tavily_news,target_company,same_name_company,info_json])
    
    # 画图任务
    if not DEBUG:
        traffic_plot = traffic_plot_task(traffic, traffic_folder)
        market_table = competitor_table_task(tavily_market, competitor_folder)

    
    # 执行任务
    asyncio.run(run_mcp_agent(target_company))
    if not DEBUG:
        asyncio.run(run_mcp_agent(traffic))
    asyncio.run(run_mcp_agent(same_name_company))
    asyncio.run(run_mcp_agent(sns))
    asyncio.run(run_mcp_agent(linkedin))
    asyncio.run(run_mcp_agent(hiring))
    asyncio.run(run_mcp_agent(tavily_market))
    asyncio.run(run_mcp_agent(tavily_news))
    asyncio.run(run_mcp_agent(tavily_financial))
    asyncio.run(run_mcp_agent(news_summary))
    asyncio.run(run_mcp_agent(financial_summary))
    
    if not DEBUG:
        asyncio.run(run_mcp_agent(traffic_plot))
        asyncio.run(run_mcp_agent(market_table))

    # 保存结果
    with open(base_dir+"/report.txt", "w") as f:
        f.write(company_name)
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        f.write(remove_prefix(target_company.response))
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        f.write(remove_prefix(linkedin.response))
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        f.write(remove_prefix(sns.response))
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        if not DEBUG:
            f.write(remove_prefix(traffic.response))
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        f.write(remove_prefix(news_summary.response))
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        f.write(remove_prefix(financial_summary.response))
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        f.write(remove_prefix(tavily_market.response))
        f.write("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        f.write(remove_prefix(hiring.response))
    
    if not DEBUG:
        with open(traffic_folder+"/traffic_plot.py", "w") as f:
            f.write(remove_prefix(traffic_plot.response))
        try:
            exec(traffic_plot.response)
        except Exception as e:
            print("画图失败！")

        with open(competitor_folder+"/competitor.py", "w") as f:
            f.write(remove_prefix(market_table.response))
        try:
            exec(market_table.response)
        except Exception as e:
            print("创建竞争对手表格失败！")

    end_time = time.time()
    print(f"运行时间为：{(end_time - start_time)/60:.2f}分钟")


if __name__ == "__main__":
    # company_name = "LangChain"
    # company_url = "https://www.langchain.com/"

    # company_name = "halliday"
    # company_url = "https://hallidayglobal.com"

    # company_name = "blackbird"
    # company_url = "https://www.blackbird.xyz"
    
    # company_name = "TRAE"
    # company_url = "https://www.trae.ai"

    company_name = "Towns Protocol"
    company_url = "https://www.towns.com"

    # company_name = "Meanwhile"
    # company_url = "https://meanwhile.bm"
    
    if not DEBUG:
        parser = argparse.ArgumentParser(description='Generate company reports.')
        parser.add_argument('company_name', type=str, help='The name of the company')
        parser.add_argument('company_url', type=str, help='The URL of the company')

        args = parser.parse_args()

        company_name = args.company_name
        company_url = args.company_url

    main(company_name, company_url)
