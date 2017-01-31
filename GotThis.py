from twython import Twython
import pandas as pd

CONSUMER_KEY = '5BMZgF8vG3YutiEFD3aA98cBj'
CONSUMER_SECRET = 'UWEE40jntSXolOqqk1jlG1NJ8QAFU62LlPFANjc0hUKJhWyCsp'
ACCESS_KEY = '825068565107707904-2nSc0qf0NxlmiC1R7GhZvfbYXkqxp1T'
ACCESS_SECRET = '6TRFQDXZIPrUHJXWAsTLT1hwebUMskGkLOa5UMFoQVzvA'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

############################################################################
# Tandem Diabetes
############################################################################
comp   = []
Tweets = []
NumRt  = []
DateTw = []
NumFav = []
NumFol = []

lis = [804058701921447936] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="TandemDiabetes",
    count=200, include_retweets=False, max_id=lis[-1])

    for tweet in user_timeline:
        comp.append('Tandem')
        Tweets.append(tweet['text'])
        NumRt.append(tweet['retweet_count'])
        DateTw.append(tweet['created_at'])
        NumFav.append(tweet['user']['favourites_count'])
        NumFol.append(tweet['user']['followers_count'])
        lis.append(tweet['id']) ## append tweet id's

columnTitle = ['Company', 'Date of Tweet', 'Number of Retweets', 'Number of Favorites', 'Number of Followers', 'Tweet']
DF = {'Company':comp, 'Tweet:':Tweets, 'Date of Tweet':DateTw,'Number of Retweets':NumRt, 'Number of Favorites':NumFav, 'Number of Followers':NumFol}
df = pd.DataFrame(DF, columns=columnTitle)

df.to_csv(r'C:\Users\Ricky\Desktop\GlookaProblem\Tandem.txt', header=columnTitle, index=None, sep=' ')
#print df

##############################################################################
#Medtronic
##############################################################################
comp   = []
Tweets = []
NumRt  = []
DateTw = []
NumFav = []
NumFol = []

lis = [804100251913228288] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="MDT_Diabetes",
    count=200, include_retweets=False, max_id=lis[-1])

    for tweet in user_timeline:
        comp.append('Medtronic')
        Tweets.append(tweet['text'])
        NumRt.append(tweet['retweet_count'])
        DateTw.append(tweet['created_at'])
        NumFav.append(tweet['user']['favourites_count'])
        NumFol.append(tweet['user']['followers_count'])
        lis.append(tweet['id']) ## append tweet id's

DF = {'Company':comp, 'Date of Tweet':DateTw,'Number of Retweets':NumRt, 'Number of Favorites':NumFav, 'Number of Followers':NumFol, 'Tweet:':Tweets}
df1 = pd.DataFrame(DF, columns=columnTitle)

df1.to_csv(r'C:\Users\Ricky\Desktop\GlookaProblem\Medtronic.txt', header=columnTitle, index=None, sep=' ')

##############################################################################
#myomnipod
##############################################################################
comp   = []
Tweets = []
NumRt  = []
DateTw = []
NumFav = []
NumFol = []

lis = [804091504759361536] ## this is the latest starting tweet id
for i in range(0, 10): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="myomnipod",
    count=200, include_retweets=False, max_id=lis[-1])

    for tweet in user_timeline:
        comp.append('Omnipod')
        Tweets.append(tweet['text'])
        NumRt.append(tweet['retweet_count'])
        DateTw.append(tweet['created_at'])
        NumFav.append(tweet['user']['favourites_count'])
        NumFol.append(tweet['user']['followers_count'])
        lis.append(tweet['id']) ## append tweet id's

DF = {'Company':comp, 'Date of Tweet':DateTw,'Number of Retweets':NumRt, 'Number of Favorites':NumFav, 'Number of Followers':NumFol, 'Tweet:':Tweets}
df2 = pd.DataFrame(DF, columns=columnTitle)

df2.to_csv(r'C:\Users\Ricky\Desktop\GlookaProblem\Omnipod.txt', header=columnTitle, index=None, sep=' ')

##############################################################################
#OneTouch
##############################################################################
comp   = []
Tweets = []
NumRt  = []
DateTw = []
NumFav = []
NumFol = []

lis = [804047935763791872] ## this is the latest starting tweet id
for i in range(0, 12): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="OneTouch",
    count=200, include_retweets=False, max_id=lis[-1])

    for tweet in user_timeline:
        comp.append('OneTouch')
        Tweets.append(tweet['text'])
        NumRt.append(tweet['retweet_count'])
        DateTw.append(tweet['created_at'])
        NumFav.append(tweet['user']['favourites_count'])
        NumFol.append(tweet['user']['followers_count'])
        lis.append(tweet['id']) ## append tweet id's

DF = {'Company':comp, 'Date of Tweet':DateTw,'Number of Retweets':NumRt, 'Number of Favorites':NumFav, 'Number of Followers':NumFol, 'Tweet:':Tweets}
df3 = pd.DataFrame(DF, columns=columnTitle)

df3.to_csv(r'C:\Users\Ricky\Desktop\GlookaProblem\OneTouch.txt', header=columnTitle, index=None, sep=' ')

##############################################################################
#FreeStyleDiabet
##############################################################################
comp   = []
Tweets = []
NumRt  = []
DateTw = []
NumFav = []
NumFol = []

lis = [804116322690985984] ## this is the latest starting tweet id
for i in range(0, 12): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="FreeStyleDiabet",
    count=200, include_retweets=False, max_id=lis[-1])

    for tweet in user_timeline:
        comp.append('FreeStyleDiabet')
        Tweets.append(tweet['text'])
        NumRt.append(tweet['retweet_count'])
        DateTw.append(tweet['created_at'])
        NumFav.append(tweet['user']['favourites_count'])
        NumFol.append(tweet['user']['followers_count'])
        lis.append(tweet['id']) ## append tweet id's

DF = {'Company':comp, 'Date of Tweet':DateTw,'Number of Retweets':NumRt, 'Number of Favorites':NumFav, 'Number of Followers':NumFol, 'Tweet:':Tweets}
df4 = pd.DataFrame(DF, columns=columnTitle)

df4.to_csv(r'C:\Users\Ricky\Desktop\GlookaProblem\FreeStyleDiabet.txt', header=columnTitle, index=None, sep=' ')

##############################################################################
#AccuCheck
##############################################################################
comp   = []
Tweets = []
NumRt  = []
DateTw = []
NumFav = []
NumFol = []

lis = [803973205937549313] ## this is the latest starting tweet id
for i in range(0, 12): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="accuchek_us",
    count=200, include_retweets=False, max_id=lis[-1])

    for tweet in user_timeline:
        comp.append('accuchek_us')
        Tweets.append(tweet['text'])
        NumRt.append(tweet['retweet_count'])
        DateTw.append(tweet['created_at'])
        NumFav.append(tweet['user']['favourites_count'])
        NumFol.append(tweet['user']['followers_count'])
        lis.append(tweet['id']) ## append tweet id's

DF = {'Company':comp, 'Tweet:': Tweets, 'Date of Tweet':DateTw,'Number of Retweets':NumRt, 'Number of Favorites':NumFav, 'Number of Followers':NumFol}
df5 = pd.DataFrame(DF, columns=columnTitle)
df5.to_csv(r'C:\Users\Ricky\Desktop\GlookaProblem\accuchek_us.txt', header=columnTitle, index=None, sep=' ')