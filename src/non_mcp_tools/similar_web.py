from apify_client import ApifyClient
from curl_cffi import requests
import os


def get_traffic_by_domain(domain: str) -> str:
    print(f"Fetching Similarweb data for domain: {domain}")
    api_key = os.getenv('APIFY_API_KEY')
    if not api_key:
        return "Error: APIFY_API_KEY not found in .env file"
    client = ApifyClient(api_key)
    run_input = { "websites": [domain] }
    run = client.actor("tri_angle/similarweb-scraper").call(run_input=run_input)
    try:
        result = next(client.dataset(run["defaultDatasetId"]).iterate_items())
        keep_keys = ['name', 'description', 'categoryId', 'companyYearFounded', 'companyName', 'companyEmployeesMin', 'companyEmployeesMax',
            'companyAnnualRevenueMin', 'companyHeadquarterCountryCode', 'companyHeadquarterStateCode', 'companyHeadquarterCity',
            'avgVisitDuration', 'pagesPerVisit', 'bounceRate', 'totalVisits', 'trafficSources', 'topKeywords', 'socialNetworkDistribution', 
            'topCountries', 'topSimilarityCompetitors', 'topInterestedCategories', 'ageDistribution',  'scrapedAt', 'snapshotDate']
        keys_to_delete = [key for key in result if key not in keep_keys]
        for key in keys_to_delete:
            del result[key]
        url = "https://data.similarweb.com/api/v1/data"
        params = {
            'domain': domain,
        }
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
            'sec-fetch-dest': 'document',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
        try:
            response = requests.get(url, params=params, headers=headers, verify=False)
            traffic_data = response.json()['EstimatedMonthlyVisits']
            traffic_data_text = f'该域名的流量数据如下：{",".join([f"{k[:7]}为{v}" for k, v in traffic_data.items()])}'
            result['traffic_data'] = traffic_data_text
        except Exception as e:
            print(f"Error fetching traffic data: {str(e)}")
        # print(f"Fetched Similarweb data: {result}")
        return result
    except Exception as e:
        return f"Error fetching Similarweb data: {str(e)}"
    
