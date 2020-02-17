from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='2a90c4be59674387b8aafe9bd54fbc8c')

# /v2/top-headlines

def BBCTopTenHeadlines():
	BBCNews = ""
	top_headlines = newsapi.get_top_headlines(sources='bbc-news')
	x = (top_headlines)
	for i in range(len(x['articles'])):
		BBCNews += (x['articles'][i]['title']+". "+x['articles'][i]['description'])
	return BBCNews
BBCTopTenHeadlines()
