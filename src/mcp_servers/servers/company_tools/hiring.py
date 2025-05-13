from mcp_servers.servers.company_tools.setup import *
from exa_py import Exa
exa = Exa(api_key = os.getenv("EXA_API_KEY"))

@mcp.tool()
async def get_company_hiring(company_url: str) -> dict:
    """Get the hiring info of the company from its website"""
    positions = exa.get_contents(
    [company_url],
    text = True,
    summary =  {
        "query": "Describe the opening positions of the company. List the position name, location, and salary"
        }
    )
    positions2 = exa.search_and_contents(
        company_url+" Linkedin positions:",
        type = "keyword",
        text = True,
        livecrawl = "always"
    )
    return {"positions":positions.results,"positions2": positions2.results}