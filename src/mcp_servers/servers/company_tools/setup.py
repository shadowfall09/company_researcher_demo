from mcp_servers.servers.base import mcp
import time
from tavily import TavilyClient
from apify_client import ApifyClient
import requests
import os

apify = ApifyClient(os.getenv('APIFY_API_KEY'))
client = TavilyClient(os.getenv('TAVILY_API_KEY'))
brave_api_key = os.getenv('BRAVE_API_KEY')