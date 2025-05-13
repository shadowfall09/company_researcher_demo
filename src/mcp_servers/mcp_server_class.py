import os

EXA_API_KEY = os.getenv("EXA_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
APIFY_API_KEY = os.getenv("APIFY_API_KEY")
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")


class GaorongvcMCP:
    command = "uv"
    # args = ["--from", "git+ssh://git@github.com/gaorongvc/mcp_servers"]
    # args = ["--from", "/Users/zhangbin/workspace/grrepos/mcp_servers"]
    args = ["--directory", "/Users/user/Downloads/临时代码/mcp_servers/src/mcp_servers", "run", "server.py"]

# https://docs.exa.ai/examples/exa-mcp#exa-mcp
class EXA:
    command = "npx"
    args =  ["exa-mcp-server","--tools=company_research,web_search,twitter_search,crawling,competitor_finder"]
    env =  {"EXA_API_KEY": EXA_API_KEY}

# https://docs.tavily.com/documentation/mcp
class tavily:
    command = "npx"
    args = ["-y","tavily-mcp@0.1.4"]
    env = {"TAVILY_API_KEY": TAVILY_API_KEY}
    
class Time_MCP:
    command = "uvx"
    args = ["mcp-server-time"]
    
class python_code_executor:
    command='deno'
    args=[
        'run',
        '-N',
        '-R=node_modules',
        '-W=node_modules',
        '--node-modules-dir=auto',
        'jsr:@pydantic/mcp-run-python',
        'stdio',
    ]
    
actor_set = {
        "social_media": ["apify/instagram-scraper","apidojo/twitter-scraper-lite","trudax/reddit-scraper-lite","tri_angle/telegram-scraper"],
        "video": ["streamers/youtube-scraper","clockworks/free-tiktok-scraper"],
        "hiring": ["misceres/indeed-scraper"],# ,"bebity/linkedin-jobs-scraper"
        "e_commerce": ["junglee/amazon-crawler","apify/facebook-ads-scraper","silva95gustavo/google-ads-scraper","epctex/aliexpress-scraper"], # "dtrungtin/ebay-items-scraper"
        "search": ["apify/website-content-crawler","lukaskrivka/article-extractor-smart","apify/google-search-scraper"], # "apify/ai-web-agent",
        "SEO": ["tri_angle/similarweb-scraper"], # "emastra/google-trends-scraper"
    }  


class Sequential_thinking:
    command = "npx"
    args = ["-y","@modelcontextprotocol/server-sequential-thinking"]

            
class Apify_social_media:
    command = "npx"
    args = ["-y","@apify/actors-mcp-server",
            "--actors", ",".join(actor_set["social_media"])]
    env = {"APIFY_TOKEN": APIFY_API_KEY}
    
class Apify_video:
    command = "npx"
    args = ["-y","@apify/actors-mcp-server",
            "--actors", ",".join(actor_set["video"])]
    env = {"APIFY_TOKEN": APIFY_API_KEY}

class Apify_hiring:
    command = "npx"
    args = ["-y","@apify/actors-mcp-server",
            "--actors", ",".join(actor_set["hiring"])]
    env = {"APIFY_TOKEN": APIFY_API_KEY}
class Apify_e_commerce:
    command = "npx"
    args = ["-y","@apify/actors-mcp-server",
            "--actors", ",".join(actor_set["e_commerce"])]
    env = {"APIFY_TOKEN": APIFY_API_KEY}
class Apify_search:
    command = "npx"
    args = ["-y","@apify/actors-mcp-server",
            "--actors", ",".join(actor_set["search"])]
    env = {"APIFY_TOKEN": APIFY_API_KEY}
class Apify_SEO:
    command = "npx"
    args = ["-y","@apify/actors-mcp-server",
            "--actors", ",".join(actor_set["SEO"])]
    env = {"APIFY_TOKEN": APIFY_API_KEY}
    
class Brave_search:
    command = "npx"
    args = ["-y","@modelcontextprotocol/server-brave-search"]
    env = {"BRAVE_API_KEY": BRAVE_API_KEY}