from dotenv import load_dotenv
from atproto import Client as bsclient
import os
import tweepy
import json
import boto3

def main_func(tweet):
    post_x(tweet)
    post_bluesky(tweet)
    
    return {
      'statusCode': 200,
      'body': json.dumps('Hello from Lambda!')
    }
    
def post_x(message):
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_secret = os.getenv('ACCESS_SECRET')
    XAuth = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_secret)
    XAuth.create_tweet(text=message)

def post_bluesky(message):
    api = bsclient()
    api.login(os.getenv('BLUESKY_ID'), os.getenv('BLUESKY_PASSWORD'))
    api.send_post(message)

################################
# MAIN # デプロイ時にはlambda handlerの方のコメントを外してif __name__ == "__main__":をコメントアウトする
################################
def lambda_handler(event, context):
# if __name__ == "__main__":
    tweet = event['message']
    # tweet = 'Hello World!'
    load_dotenv()
    main_func(tweet)