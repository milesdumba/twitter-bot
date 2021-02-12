import tweepy
import time
import random
import os
from os import environ


print('this is my twitter bot')


CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True)

FILE_NAME = 'last_seen_id.txt'
MEDIA_FILE = ['The inability to resist temptation makes you a slave to those temptations, whilst the capacity to prioritise what must be done over what you desire to do frees you to reach your potential',
              'The stronger you get, both physically and mentally, the easier everything seems. The things people call unrealistic suddenly only seem difficult to you',
              'Suffering cannot be avoided, merely postponed. Get it over and done with',
              'You will doubt yourself a million times. It is only natural',
              'Bitter are the roots of study, but how sweet their fruits',
              'Iron rusts from disuse, stagnant water loses its purity, and in cold weather becomes frozen; even so does inaction sap the vigors of the mind',
              'It takes being average for a while to become great',
              'Growth is an endlessly iterative process. Keep improving',
              'Love the hand that fate deals you and play it as your own, for what could be more fitting?',
              'The greater the difficulty of a task, the more the glory in surmounting it',
              'Get comfortable with frequent small failures on the way to learning',
              'Set an ambitious hourly wage rate for yourself that determines how you value your time. If your rate does not feel absurdly high, it is not high enough. Is what you’re currently doing right now worth your time?',
              'Do not cry about the unfairness of life ... exploit it. Life is a video game, and all games can be hacked',
              "Isn’t life funny? You cannot succeed without failing at least once, but you can fail multiple times and never succeed. The more you fail and learn, the greater the probability of succeeding",
              'Everything is either an opportunity to grow or an obstacle to keep you from growing. You get to choose',
              'You cannot afford to live on potential for the rest of your life; at some point, you have to unleash the potential and make your move',
              'Hardships often prepares ordinary people for an extraordinary destiny',
              "It is not about perfection. It’s about effort. And when you bring that effort every single day, that’s where transformation happens. That is how change occurs",
              'Only he who attempts the absurd is capable of achieving the impossible',
              'Character cannot be developed in ease and quiet. Only through experience of trial and suffering can the soul be strengthened, ambition inspired, and success achieved',
              'Output will tend to be greater when everyone strives for a level of achievement beyond immediate grasp… Such goal-setting is extremely important if what you want is peak performance',
              'Growth: 100 uncomfortable hours > 1,000 comfortable hour',
              'Surpass Your Limits.Right here. Right now!',
              "Even if you think you might fail, you'll be fine aslong as you don't give up! Surpass your limits. Then a path will open up for you!",
              'Being weak is nothing to be ashamed of...Staying weak is!'
              ]


def RANDOM_MEDIA_LIST(x):
    b = MEDIA_FILE
    random.shuffle(b)
    return b



def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()     
    return last_seen_id

# retrieves& id of tweet mention so bot does not reply to same user infinite times

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
# stores id of tweet mention so bot does not reply to same user infinite times

def reply_to_tweets():
    print('retrieving &replying to tweets...')

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode = 'extended')

    # use 1345535556198035458 for testing 

    for mention in reversed(mentions):   #allows us to go through oldest tweet mentions first
        print(str(mention.id)+ '-' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#ineedmotivation' in mention.full_text.lower():
            RANDOM_MEDIA_FILE = RANDOM_MEDIA_LIST(MEDIA_FILE)
            RANDOM_MEDIA_FILE2 = (random.choice(RANDOM_MEDIA_FILE))
            print('found #ineedmotivation')
            print('responding back...')
            api.update_status(RANDOM_MEDIA_FILE2 + ' @' + mention.user.screen_name, mention.id) 
            #Add ',mention.id' to get bot to reply under tweet, ' @' + mention.user.screen_name
            #api.update_status('@' + mention.user.screen_name + ' ' + RANDOM_MEDIA_FILE2 , mention.id)

while True:
    reply_to_tweets()
    time.sleep(10)





