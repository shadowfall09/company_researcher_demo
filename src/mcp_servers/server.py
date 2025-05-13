import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# from mcp_servers.servers.linkedin import *
# from mcp_servers.servers.similarweb import *
# from mcp_servers.servers.twitter.twitter import *
# from mcp_servers.servers.reddit import *
from mcp_servers.servers.company_tools.company_info import *
from mcp_servers.servers.company_tools.linkedin import *
from mcp_servers.servers.company_tools.sns import *


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run()
