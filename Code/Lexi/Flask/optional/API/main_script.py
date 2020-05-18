
import config

from twython import Twython, TwythonError

# create a Twython object by passing the necessary secret passwords
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)