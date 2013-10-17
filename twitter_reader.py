# parses tweets
import httplib
conn = httplib.HTTPConnection("search.twitter.com")
conn.connect()
conn.request("GET","/search.json?q=justinbieber")
r1 = conn.getresponse()
print(r1.read())
tweets=r1.read()
f1 = open("tweets.txt",'w')
for tweet in tweets:
  if (tweet =='results'):
    for result in tweet:
      for variable in result:
        if (variable=='text'):
          print result[variable]
          
f1.close()
conn.close()
