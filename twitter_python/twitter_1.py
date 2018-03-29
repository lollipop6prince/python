# 导入tweepy
import tweepy

# 填写twitter提供的开发Key和secret
consumer_key = 'Qx7dQ3kvukoOMUWWAOg6D3GyE'
consumer_secret = 'Jdc2HlQ2r6YI5dWgo7qjMxd2oG3hv8WYds2mxim9LelOXXTd5i'
access_token = '285994030-Zxsxhy5eMUqIS43RKWu49ffmmaDc5Z6frk1m8ZNl'
access_token_secret = 'R0UwXSOcclld3dRPr1TzWmc9Lq4bG1K8KVhenv82es0o8'

# 提交你的Key和secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# 获取类似于内容句柄的东西
api = tweepy.API(auth)

# 打印其他用户主页上的时间轴里的内容
public_tweets = api.user_timeline('aka_seka')

#print (public_tweets)

for tweet in public_tweets:
    print (tweet.text)