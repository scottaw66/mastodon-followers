import json
import logging
import logging.config
import logging.handlers
import os
import sys

from datetime import datetime
from dotenv import load_dotenv
from mastodon import Mastodon

env_file = '.env'

# optionally load environment variables from .env.prod if some of them need changed for production environments. Simply pass a command line argument of 'prod' (without quotes) to the script.
for x in sys.argv[1:]:
    if 'prod' in x:
        env_file = '.env.prod'

load_dotenv(env_file)

mastodon_token = os.getenv("MASTODON_TOKEN")
mastodon_base_url = os.getenv("MASTODON_BASE_URL")
mastodon_username = os.getenv("MASTODON_USERNAME")
log_path = os.getenv("LOGFILE_PATH")

if not mastodon_token:
    sys.exit("Missing environment variable: MASTODON_TOKEN")
if not mastodon_base_url:
    sys.exit("Missing environment variable: MASTODON_BASE_URL")
if not mastodon_username:
    sys.exit("Missing environment variable: MASTODON_USERNAME")
if not log_path:
    sys.exit("Missing environment variable: LOGGING_DIR")

from logging_config import log_settings
log_settings["handlers"]["file"]["filename"] = log_path
logging.config.dictConfig(log_settings)

# create logger
logger = logging.getLogger('main')

mastodon = Mastodon(
    access_token=mastodon_token,
    api_base_url=mastodon_base_url,
)

me = mastodon.me()
my_id = me.id
account = mastodon.account(my_id)
followers = mastodon.account_followers(my_id)
#followers = mastodon.fetch_remaining(followers)
follower_count = len(followers)

timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
""" f = open(f'data/followers-{timestamp}', "w")
f.write("{") """
for follower in followers:
    logger.info(follower)
""" f.write("}")
f.close() """