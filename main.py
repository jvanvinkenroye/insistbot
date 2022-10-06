import tweepy
import random

# authentifikations daten
bearer_token = "AAAAAAAAAAAAAAAAAAAAALymhQEAAAAAXNnHi2IZWb7GlbqLzRS2pYrVjjo%3Dpxv61uF5GQM4Y6LRqJIyrziO7CT1DMn2vFE1WLQFvCqDQYOMby"
consumer_key = "CvoDQM2t1WMLyVIPkZN2BTPLK"
consumer_secret = "HKveYnYqp7vCYYrQ3C2OFOAWZ4xvXp9Vwyzho6wIJGCf9CjYL2"
access_token = "1573406533697896448-DyYL6sxOFv8adtQHR7E0qZrnG7RHq7"
access_token_secret = "VlHIyh2oxQAwXWvX8X2KE7wgolumf2kn0ymTV6bzdC3zv"

# client initialisieren
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# nur tweets eines speziellen users retweeten
user_id = 1573406533697896448

# funktion zum auslesen der id des letzten tweets
def get_last_tweet(file):
    f = open(file, 'r')
    lastId = int(f.read().strip())
    f.close()
    return lastId

# funktion zum speichern der id des letzten tweets
def put_last_tweet(file, Id):
    f = open(file, 'w')
    f.write(str(Id))
    f.close()
    return


def reply(file='tweet_ID.txt'):
    response = client.get_users_tweets(user_id)
    for tweet in response.data:
        lastId = get_last_tweet(file)
        print("lastId")
        print(lastId)
        print("tweet.id")
        print(tweet.id)
        if tweet.id != lastId:
            print("jetzt würde ich twittern")
            tweet_text = random.choice(list(open('file.txt')))
            client.create_tweet(in_reply_to_tweet_id=tweet.id, text=tweet_text, exclude_reply_user_ids=['1573406533697896448'])
            print("tweet.id")
            print(tweet.id)
            put_last_tweet(file, tweet.id)
        else:
            print("ich mach dann mal nix")


if __name__ == "__main__":
    reply()

