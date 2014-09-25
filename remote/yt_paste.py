#remote python file binbash
import MySQLdb
import bs4
import sys
import getopt
import re
execfile('pass.py')
def insert_item(full_vid,vid_post):
	print full_vid
	print vid_post

if sys.argv[1]=="":
        print "there's nothing here"
        exit()
else:
	vid = sys.argv[1]
	vid_post = vid.strip("https://www.youtube.com/watch?v=")
	vid_post = re.sub('\&.*','',vid_post)
	full_vid = re.sub('\&.*','',vid)#remove extraneous details about the video like time to start and playlist
	try:
		db = MySQLdb.connect(host=rm_db_host,user=rm_usr,passwd=rm_db_pw,db=rm_db)
		cur = db.cursor()
		cur.execute("SELECT count(id) FROM videos WHERE post=%s;",(vid_post,))
		row =int(cur.fetchone()[0])
		if row != 0:
			print "this one exists"
		else:
			print "doesn't exist"
			insert_item(full_vid,vid_post)
		cur.close()
		db.close()
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0],e.args[1])

