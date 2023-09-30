import tweepy

class XAuth:
  def Auth_info(XAuth, BlueskyAuth):
      # X 認証情報
      api_key = '0NzyoX5MEXkcFtz3YPNHefnNp'
      api_secret = 'Ca6F6St5d4JAqKXgLoVyUBvVk2Qfl57Gv7gfUtRac2smw2KZ5e'
      access_token = '3546200300-WhHPQtx63CWiOk9b5Vjp5FtQgXzsLEOcAQOt0LM'
      access_secret = 'VzjijW8yUJrekeoUH4wMtRdkFsUbZRLtXwlIwApGMi6VB'
      XAuth = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_secret)

      # Bluesky 認証情報
      # api = Client()
      # BlueskyAuth = api.login('a2215rs@aiit.ac.jp', 'fdo4Cffp')

      return XAuth, BlueskyAuth



XAuth.send_post('Hello World')
# BlueskyAuth.create_tweet(text="あああああ")