from textblob import TextBlob
import csv
import tweepy
import unidecode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#(OAuth)
f = open('auth.k','r')
ak = f.readlines()
f.close()
auth1 = tweepy.auth.OAuthHandler(ak[0].replace("\n",""),
ak[1].replace("\n",""))
auth1.set_access_token(ak[2].replace("\n",""),
ak[3].replace("\n",""))
api = tweepy.API(auth1)
target_num = int(raw_input())
query = raw_input()
hashtags=map(str,raw_input().split())
print hashtags
csvFile = open('results_social.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","authorid","created", "text",
"retwc", "hashtag", "followers",
"friends","polarity","subjectivity"])
counter = 0
for tweet in tweepy.Cursor(api.search, q = query, lang = "en",
count = target_num).items():
created = tweet.created_at
text = tweet.text
text = unidecode.unidecode(text)
retwc = tweet.retweet_count
try:
hashtag = tweet.entities[u'hashtags'][0][u'text']
print hashtag #hashtags used
except:
hashtag = "None"
username = tweet.author.name
authorid = tweet.author.id
followers = tweet.author.followers_count
friends = tweet.author.friends_count
text_blob = TextBlob(text)
polarity = text_blob.polarity
subjectivity = text_blob.subjectivity
for i in range(0, len(hashtags)):
if(hashtags[i] == hashtag):
csvWriter.writerow([username, authorid, created, text, retwc,
hashtag, followers, friends, polarity, subjectivity])
counter = counter + 1
if (counter == target_num):
break
csvFile.close()