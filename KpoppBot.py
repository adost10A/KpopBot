import praw, time
from KpopClass import *
u = 'kpoppbot'
p = '1216809a'
r = praw.Reddit(user_agent = '/r/KpopBot')
r.login(username = u, password = p)
checked = set()
fixcount = 0
count = 0
comments = praw.helpers.comment_stream(r,'kpoppbot', limit=None)
while True:
    try:
        for comment in comments:
            count+=1
            for Call in CallList:
                if (Call in str(comment))and (comment.id not in checked):
                    checked.add(comment.id)
                    if '!Members' in str(comment):
                        temp = Call
                        comment.reply('Members of ' + temp[1:] + ' are ' + Dic[Call])
                        timeset = time.strftime("%d/%m/%y %H:%M:%S")
                        print ("Just Posted A Message @ " + timeset)
                        print ("About " + Dic[Call] + ' in ' + comment.id)
                        print "\n\n"
                elif '!Help' in str(comment):
                        
                        comment.reply('Come check the wiki at /r/kpoppbot, any questions feel free to DM the creator /u/picflute')
                        timeset = time.strftime("%d/%m/%y %H:%M:%S")
                        print ("Just Posted A Message @ " + timeset)
                        print ("About " + Dic[Call] + ' in ' + comment.id)
                        print "\n\n"
                    
                else:
                    pass
    except Exception as e:
        print e
        
