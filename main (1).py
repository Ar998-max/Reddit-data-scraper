import praw
import random
import time
import csv
from keep_Aliv import keep_alive
# from main2 import main2
from itertools import repeat
from threading import Thread
from time import sleep

username = "XXXXXX",

keep_alive()
# main2()
print('AAAAAAA')

reddit = praw.Reddit(client_id="XXXXXX",
                    client_secret="XXXXXXX",
                     user_agent="<XXXXXXX",
                     username=username,
                     password='XXXXXXXX')





subreddit = reddit.subreddit('teenagers')




class ptdata(Thread):
  
    def run(self):
      print('opening post_data csv')
      
      
      with open('post_data.csv', 'a') as f:
            headers = [
                'ID', 'Date_utc', 'Upvotes', 'Number of Comments', 'Subthread name', 'Post Author'
            ]
            writer = csv.DictWriter(f,
                                    fieldnames=headers,
                                    extrasaction='ignore',
                                    dialect='excel')
            writer.writeheader()
            for post in subreddit.stream.submissions():
                #print(post.title)
                
                data = {
                        "ID": post.id,
                        "Date_utc": post.created_utc,
                        "Upvotes": post.ups,
                        "Number of comments": post.num_comments,
                        "Subthread name": post.title,
                        "Post Author": post.author
                        }
                
                writer.writerow(data)
                print('writing post row')
                # print(data)










class ctdata(Thread):
  def run(self):

      

        with open('comment_data.csv', 'a') as a:
              headers = [
                  'ID', 'Date_utc', 'Upvotes', 'Comment Body', 'Comment Author'
              ]
              writer = csv.DictWriter(a,
                                      fieldnames=headers,
                                      extrasaction='ignore',
                                      dialect='excel')
              writer.writeheader()
              for comment in subreddit.stream.comments(skip_existing=True):
              #print(post.title)
              
                  data = {
                          "ID": comment.id,
                          "Date_utc": comment.created_utc,
                          "Upvotes": comment.ups,
                          "Comment Body": comment.body,
                          "Comment Author": comment.author
                         }
                  writer.writerow(data)
                  #print(data)
                  print('printing comment data rowl')














class htdata(Thread):
  def run(self):

        print('now opening hot_post_data csv')
        with open('hot_post_data.csv', 'a') as b:
            headers = [
                'ID', 'Date_utc', 'Upvotes', 'Number of Comments', 'Subthread name', 'post author']
              
            writer = csv.DictWriter(b,
                                    fieldnames=headers,
                                    extrasaction='ignore',
                                    dialect='excel')
            writer.writeheader()
            for post in subreddit.hot(limit=None):
                #print(post.title)
                
                data = {
                        "ID": post.id,
                        "Date_utc": post.created_utc,
                        "Upvotes": post.ups,
                        "Number of comments":post.num_comments,
                        "Subthread name": post.title,
                        "Author": post.author
                        }
                writer.writerow(data)
                # print(data)
                print('writing hot post data')


















class cotdata(Thread):
  def run(self):

      print('now opening controversial_post_data csv')

      with open('controversial_post_data.csv', 'a') as c:
          headers = [
              'ID', 'Date_utc', 'Upvotes', 'Number of Comments', 'Subthread name', 'Post Auther'
          ]
          writer = csv.DictWriter(c,
                                  fieldnames=headers,
                                  extrasaction='ignore',
                                  dialect='excel')
          writer.writeheader()
          for post in subreddit.controversial(limit=None):
              #print(post.title)
              
              data = {
                      "ID": post.id,
                      "Date_utc": post.created_utc,
                      "Upvotes": post.ups,
                      "Number of comments": post.num_comments,
                      "Subthread name": post.title,
                      "Post Author": post.author
                      }
              writer.writerow(data)
              # print(data)
              print('writing controversial data')

  















c1 = ptdata()
c2 = ctdata()
c3 = htdata()
c4 = cotdata()

c1.start()
sleep(0.2)
print('c1 done')

c2.start()
sleep(0.2)
print('c2 done')

c3.start()
sleep(0.2)
print('c3 done')

c4.start()
sleep(0.2)
print('c4 done')











