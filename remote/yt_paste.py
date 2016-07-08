#!/home/jonkman666/bin/python
import MySQLdb
import re
import os
import sys
global PATH 
PATH = "YR PATH"
def insert_item(vid_post,db,cur):
	all_vids = os.listdir(PATH + "/videos/")
	desc_file = ""
	title = ""
	channel = ""
	
	for x in all_vids:
		split_file = x.split("&&&")
		if split_file[0]==vid_post:
			vid_file = x.replace(".description","")
			desc_file = x
			title = split_file[1]
			channel = split_file[2]
			break
	f = file(PATH + "/videos/"+desc_file,"r")#open file
	desc = f.read()#read the shit
	try:
		cur.execute("INSERT INTO videos(title,post,description,channel,date_copied,file_path) VALUES(%s,%s,%s,%s,CURRENT_TIMESTAMP,%s);",(title,vid_post,desc,channel,vid_file))
		db.commit()
		cur.close()
		db.close()
		print 'FUCK YA'
		exit()
	except MySQLdb.Error as e:
		print "Error %d: %s" % (e.args[0],e.args[1])
		return "Error %d: %s" % (e.args[0],e.args[1])





if len(sys.argv) < 2:
        print "there's nothing here"
        exit()
else:
	vid = sys.argv[1]
	if "youtube.com/watch?" in vid:
		vid_post = vid.strip("https://www.youtube.com/watch?v=")
	elif "youtu.be/" in formattedStr:
		vid_post = vid.strip("http://youtu.be/")
	try:
		db = MySQLdb.connect(host=rm_mysql_host,user=rm_mysql_usr,passwd=rm_mysql_pw,db=rm_mysql_db)
		cur = db.cursor()
		cur.execute("SELECT count(id) FROM videos WHERE post=%s;",(vid_post,))
		row =int(cur.fetchone()[0])
		print row
		print "that was row"
		if row != 0:
			print "this one exists"
		else:
			print "doesn't exist"
			insert_item(vid_post, db, cur)
		cur.close()
		db.close()
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0],e.args[1])

