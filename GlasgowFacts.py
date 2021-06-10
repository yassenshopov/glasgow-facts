import sys
sys.path.append('C:\PythonAnaconda\Lib\site-packages')
import tweepy
from tweepy import API
import unicodedata

counter_tweet = 2

#Run self-writing stub
content = []
with open(__file__,"r") as f:
    for line in f:
        content.append(line)

with open(__file__,"w") as f:
    counter_tweet = counter_tweet + 1
    content[6] = "counter_tweet = {n}\n".format(n = counter_tweet)
    for i in range(len(content)):
        f.write(content[i])

# Authenticate to Twitter

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")

auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")


# Create API object
api = tweepy.API(auth)

#To read from list (.txt file)
daily_tweet = 'Error'

file = open('list_tweets.txt','r')
file2 = list(file)

print('ORIGINAL:',file2[0])
encoded = file2[0].encode('cp1252')
final_text = encoded.decode('utf-8')
print('EDIT:',final_text)


status = 'Daily Glasgow Fact #' + str(counter_tweet) + ': ' + str(final_text)
api.update_status(status)

archive = []
archive.append(file2[0])
with open('archive.txt',"a+") as f:
    for index,i in enumerate(archive):
        f.write(status)
        f.write('------')
        f.write('\n')


file2.remove(file2[0])
file2.remove(file2[0])
file = open('list_tweets.txt','w+')
for line in file2:
    file.write(line)


input('Program executed. Press ENTER to exit. Cheers')
