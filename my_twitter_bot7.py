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
MEDIA_FILE = [
              'It takes being average for a while to become great',
              'Growth is an endlessly iterative process. Keep improving',
              'Love the hand that fate deals you and play it as your own, for what could be more fitting?',
              'The greater the difficulty of a task, the more the glory in surmounting it',
              'Get comfortable with frequent small failures on the way to learning',
              'Do not cry about the unfairness of life ... exploit it. Life is a video game, and all games can be hacked',
              'You cannot afford to live on potential for the rest of your life; at some point, you have to unleash the potential and make your move',
              "It is not about perfection. It’s about effort. And when you bring that effort every single day, that’s where transformation happens. That is how change occurs",
              'Only he who attempts the absurd is capable of achieving the impossible',
              'Character cannot be developed in ease and quiet. Only through experience of trial and suffering can the soul be strengthened, ambition inspired, and success achieved',
              'Output will tend to be greater when everyone strives for a level of achievement beyond immediate grasp… Such goal-setting is extremely important if what you want is peak performance',
              'Captain Yami said Surpass Your Limits',
              'Real generosity towards the future lies in giving all to the present',
              'The more immediate pleasure you get from an action, the more strongly you should question whether it aligns with your long-term goals',
              'When nothing seems to help, I go & look at a stonecutter hammering away at his rock -a hundred times without a crack showing in it. Yet at the hundred & first blow it will split in two, & I know it was not that last blow that did it—but all that had gone before',
              'When preparation becomes a form of procrastination, you need to change something. You don’t want to merely be planning. You want to be practising',
              'Start with repetition, not perfection. This is the first takeaway of the 3rd Law: you just need to get your reps in',
              'Missing one session is an accident. Missing two is the start of a new habit.',
              'Sluggish days and bad workouts maintain the compound gains you accrued from previous good days. Simply doing something— anything really —is huge. Don’t put up a zero. Don’t let losses eat into your compounding',
              'When you can’t win by being better, you can win by being different. A good player works hard to win the game everyone else is playing. A great player creates a new game that favours their strengths and avoids their weaknesses',
              'At some point it comes down to who can handle the boredom of training every day, doing the same lifts over and over and over.',
              '“Men desire novelty to such an extent that those who are doing well wish for a change as much as those who are doing badly.”'
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
        if ' #ineedmotivation' in mention.full_text.lower():
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





