Setup Twitter keys
import twitter
import json
#api = twitter.Api(consumer_key='consumer_key',consumer_secret='consumer_secret',access_token_key='access_token',access_token_secret='access_token_secret')
api = twitter.Api(consumer_key='FxdIcqx2qgGO7irzTdabgRJm7',
                      consumer_secret='hCPIwHTVBm9Y5mkryL3dSRapY7b40E1P52ZJdfqyGSEK6aJlDk',
                      access_token_key='55901155-jic21fdO1KNrpqIr3nabIIuK3An2bm9P5rzX5CUlK',
                      access_token_secret='V17gMJDGSHfpyX266kwgUj3ReqUObMwbebpmxcxCagvQM')
print(api.VerifyCredentials())
{"created_at": "Sat Jul 11 19:01:38 +0000 2009", "default_profile": true, "default_profile_image": true, "followers_count": 7, "friends_count": 22, "id": 55901155, "id_str": "55901155", "lang": "en", "location": "New York, NY", "name": "Sanket Ninawe", "profile_background_color": "C0DEED", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png", "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png", "profile_link_color": "1DA1F2", "profile_sidebar_border_color": "C0DEED", "profile_sidebar_fill_color": "DDEEF6", "profile_text_color": "333333", "profile_use_background_image": true, "screen_name": "sanketninawe"}
#1 Streaming API with geolocation
f = open('./streamingData.json', 'w')
for tweet in api.GetStreamFilter(locations=["-122.75","36.8","-121.75","37.8"]):
    f.write(json.dumps(tweet))
    f.write('\n')
    
#2 Search API with geolocation
results = api.GetSearch(geocode="37.781157,-122.398720,1mi")
print(len(results))  # count the number of records returend by the query
print(results[0])    # print and see an example one tweet instance.
#3.1 load the json from file into memory     
data=[]
with open('./streamingData.json', 'r') as jsonFile:
    for line in jsonFile:
        data.append(json.loads(line))
print("Total number of tweets loaded: ", len(data))
Total number of tweets loaded:  22
tweets = []
for item in data:
    if "text" in item.keys():
        tweet = item["text"]
        tweets.append(tweet) 
print("total no of tweets extracted from json: ", len(tweets))
total no of tweets extracted from json:  22
So, there are no empty tweets in the data

#3.2 various keys for any one json object
print(data[0].keys())
dict_keys(['created_at', 'id', 'id_str', 'text', 'display_text_range', 'source', 'truncated', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'quote_count', 'reply_count', 'retweet_count', 'favorite_count', 'entities', 'favorited', 'retweeted', 'filter_level', 'lang', 'timestamp_ms'])
Some of the interesting attributes in this json object are coordinates, reply count, retweet count, retweeted, language, place, favorites, quote count, timestamp etc.
#3.3 extract the tweets alone from this json dataset.
print(data[2]["text"])
@realDUmbridge Marauder? You must be thinking of The Butcher of Benghazi and odummer? 1.7 Billion to Iran? https://t.co/1SZKwz01ne
print(data[20]["text"])
@seanhannity @bbodine18457 Maybe it https://t.co/4TTrNiaJn4 best, if he just stays home for the next meeting.
print(data[21]["text"])     
Mostly Russian bots. https://t.co/tosnO5qFng
