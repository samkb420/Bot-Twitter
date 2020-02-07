import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("pGBDoAaEpkliVKBOLwjtcmHGc", 
    "xF3g1wrP50b6BlZEd20u4oVfjgH1FGQcuWUzlQO5aUWOufvlhw")
auth.set_access_token("622518493-6VcLIPprbQbv9wkcBBPvCle8vsjU9fE85Dq9oStl", 
    "tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# import tweepy

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")


# import tweepy

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# # Create API object
# api = tweepy.API(auth, wait_on_rate_limit=True,
#     wait_on_rate_limit_notify=True)



# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

#api.update_status("Test tweet from Tweepy Python")



# user = api.get_user("MikezGarcia")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)


# tweets = api.home_timeline(count=1)
# tweet = tweets[0]
# print(f"Liking tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)



# for tweet in api.search(q="Python", lang="en", rpp=10):
#     print(f"{tweet.user.name}:{tweet.text}")



# trends_result = api.trends_place(1)
# for trend in trends_result[0]["trends"]:
#     print(trend["name"])
