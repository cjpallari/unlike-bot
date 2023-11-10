import tweepy


def authenticate_twitter():
    bearer_token = input("Enter your bearer token")
    consumer_key = input("Enter your consumer key:")
    consumer_secret = input("Enter your consumer secret:")
    access_token = input("Enter your access token:")
    access_token_secret = input("Enter your access_token_secret:")

    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client


def unlike_tweets(client, keywords):
    twitter_id = input("Enter your Twitter username (without @):")
    liked_tweets = client.get_liked_tweets(id=twitter_id)
    count = 0

    # print(f"Rate Limit Limit: {api.last_response.headers['x-rate-limit-limit']}")
    # print(f"Rate Limit Remaining: {api.last_response.headers['x-rate-limit-remaining']}")

    for tweet in liked_tweets:
        for keyword in keywords:
            if keyword.lower() in tweet.text.lower():
                client.unlike(tweet)
                count + 1
                print(f"Unliked tweet: {tweet.text}")
                print(f"Tweets deleted: {count}")
                break


if __name__ == "__main__":
    client = authenticate_twitter()

    # Enter keywords in the input section
    keywords_input = input("Enter key words (if multiple, separate by comma):")
    keywords = keywords_input.split(",")

    unlike_tweets(client, keywords)
