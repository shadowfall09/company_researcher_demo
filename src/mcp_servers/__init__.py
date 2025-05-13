import argparse

from .server import mcp


def main():
    """MCP Servers: request private data."""
    parser = argparse.ArgumentParser(
        description="Gives you the ability to request private data."
    )
    parser.parse_args()
    mcp.run()


if __name__ == "__main__":
    main()
