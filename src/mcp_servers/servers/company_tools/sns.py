from mcp_servers.servers.company_tools.setup import *
import json
import asyncio

def fetch_reddit_posts(company_summary: str):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": brave_api_key
    }
    params = {
        "q": "site:reddit.com "+company_summary,
        "count": 8
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    data = response.text
    json_data = json.loads(data)
    posts = []
    for item in json_data.get("web", {}).get("results", []):
        if "reddit.com" in item.get("url", ""):
            posts.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "description": item.get("description"),
                "published": item.get("page_age") or item.get("age")
            })

    return posts


def fetch_github_id(company_summary: str):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": brave_api_key
    }
    params = {
        "q": "github "+company_summary,
        "count": 2
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    data = response.text
    json_data = json.loads(data)
    results = json_data.get("web", {}).get("results", [])
    github_url = [item["url"] for item in results if "github.com" in item.get("url", "")]
    if not github_url:
        github_url = None
    return github_url


def fetch_youtube_videos(company_summary: str):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": brave_api_key
    }
    params = {
        "q": "site:youtube.com "+company_summary,
        "count": 5
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed, {response.text}")
    data = response.text
    json_data = json.loads(data)
    video_results = json_data.get("web", {}).get("results", [])
    parsed_videos = []

    for video in video_results:
        parsed = {
            "title": video.get("title", ""),
            "url": video.get("url", ""),
            "description": video.get("description", ""),
            "creator": video.get("video", {}).get("creator", "Unknown"),
            "views": video.get("video", {}).get("views", "Unknown"),
            "duration": video.get("video", {}).get("duration", "Unknown"),
            "thumbnail": video.get("thumbnail", {}).get("original", "")
        }
        parsed_videos.append(parsed)
    return parsed_videos
    
    
def fetch_readme(owner, repo):
    headers = {"Accept": "application/vnd.github.v3.raw"}
    base_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        return None
    else:
        return None

@mcp.tool()
async def get_company_social_media(company_name: str, company_summary: str, company_url: str) -> dict:
    """Get the social media info of the company, including twitter, github, reddit, youtube, all return in one call
    Args:
        company_name: the name of the company
        company_summary: 2 keywords of the company in English
        company_url: the url of the company
        """
    twitter = client.search(
        query=company_url,
        include_domains=["x.com"]
    )
    github_ids = fetch_github_id(company_summary+" "+company_name)
    github_detail = []
    if github_ids:
        for github_id in github_ids:
            await asyncio.sleep(1)
            owner,repo = github_id.split("/")[-2:]
            url = f"https://api.github.com/repos/{owner}/{repo}"
            headers = {'Accept': 'application/vnd.github.v3+json','Authorization': f'token '+os.getenv("GITHUB_TOKEN")}
            response = requests.get(url, headers=headers)
            await asyncio.sleep(1)
            readme = fetch_readme(owner, repo)
            if response.status_code == 200:
                data = response.json()
                github_detail.append({
                    'name': data['name'],
                    'description': data['description'],
                    'readme': readme,
                    'stars': data['stargazers_count'],
                    'forks': data['forks_count'],
                    'watchers': data['subscribers_count'],
                    'open_issues': data['open_issues_count'],
                    'topics': data.get('topics', []),
                    'language': data['language'],
                    'url': data['html_url'],
                    'star_history': 'https://api.star-history.com/svg?repos={owner}/{repo}&type=Date'.format(owner=owner, repo=repo),
                }) 
    await asyncio.sleep(1)   
    reddit_posts = fetch_reddit_posts(company_summary+" "+company_name)
    await asyncio.sleep(1)
    youtube = fetch_youtube_videos(company_summary+" "+company_name)
    return {"twitter": twitter["results"],  "github": github_detail, "reddit": reddit_posts, "youtube": youtube}


if __name__ == "__main__":
    import asyncio
    result = asyncio.run(get_company_social_media("halliday", "smart glasses AI", "https://hallidayglobal.com"))
    print(result)