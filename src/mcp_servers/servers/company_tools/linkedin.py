from mcp_servers.servers.company_tools.setup import *

def filter(posts, threshold=0.4):
    """Filter the posts by score"""
    return [post for post in posts if post["score"] > threshold]

@mcp.tool()
async def get_company_linkedin(company_url: str,company_summary: str) -> dict:
    """Get the linkedin info of the company, including the company's linkedin page
    Args:
        company_url: the url of the company
        company_summary: the summary of the company, one short sentence (5 - 10 words) in English is enough"""
    result = client.search(
        query=company_url+"'s linkedin",
        max_results=3
    )
    result2 = client.search(
        query=company_summary + " Find "+company_url+"'s linkedin profile",
        max_results=3
    )
    return {"linkedin": filter(result["results"]+result2["results"])}


@mcp.tool()
async def get_company_linkedin_detail(company_linkedin: str) -> dict:
    """Get the linkedin info of the company, including the founder's linkedin page
    Args:
        company_linkedin: the linkedin url of the company, like https://www.linkedin.com/company/xxx"""
    response = client.extract(
        urls=[company_linkedin],
    )
    run_input = {
    "url": company_linkedin
    }
    run = apify.actor("dutBfLahHvTirBwyR").call(run_input=run_input)
    founders = next(apify.dataset(run["defaultDatasetId"]).iterate_items())["message"]["employees_data"]
    run_input = {
    "profileUrls": [founder["link"].replace("?trk=org-employees","") for founder in founders]
    }    
    run = apify.actor("2SyF0bVxmgGr8IVCZ").call(run_input=run_input)
    founders = list(apify.dataset(run["defaultDatasetId"]).iterate_items())
    return {"founders": founders, "detail": response["results"]}


if __name__ == "__main__":
    import asyncio
    result = asyncio.run(get_company_linkedin_detail("https://www.linkedin.com/company/traeai"))
    print(result)