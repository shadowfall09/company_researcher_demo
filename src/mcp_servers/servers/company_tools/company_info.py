from mcp_servers.servers.company_tools.setup import *

@mcp.tool()
async def get_company_info(company_url: str) -> dict:
    """Get the website info of the company
    Args:
        company_url: the url of the company
    Note:
        Cached Anwer will be stored in `target_company`, so don't use this tool unless you're excuting the task `target_company`"""
    summary = client.search(
        query=company_url,
    )
    return {"summary": summary["results"]}


@mcp.tool()
async def get_company_same_name(company_name: str) -> dict:
    """Get the company with the same name
    Args:
        company_name: the name of the company"""
    same_name = client.search(
        query="company named "+company_name,
        max_results=6
    )
    return {"same_name": same_name["results"]}


if __name__ == "__main__":
    import asyncio
    result = asyncio.run(get_company_info("https://www.halliday.ai/"))
    print(result)