from TwitterAPI import TwitterAPI
from urllib import quote
import settings


def login():
	api = TwitterAPI(settings.consumer_key,
				settings.consumer_secret,
				settings.access_token_key,
				settings.access_token_secret)

	return api

def search(api, search_term):
	search_string = '#{} filter:links'.format(search_term)
	result = api.request('search/tweets', {'q': search_string})
	
	return result

def playlist(results):
	playlist = []

	for tweet in results:
		for url in tweet['entities']['urls']:
			playlist.append(url['expanded_url'])

	return playlist

if __name__ == "__main__":
	api = login()
	hashtag = raw_input('Enter your hashtag:')
	results = search(api, hashtag)
	playlist = playlist(results)
	print playlist