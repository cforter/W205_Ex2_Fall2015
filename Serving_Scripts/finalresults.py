import psycopg2
conn = psycopg2.connect(database="Tcount", user="postgres", password="pass")
cur = conn.cursor()

print 'For which word would you like to see the count?'
which_word = str(raw_input())

cur.execute("SELECT count from tweetwordcount WHERE word = %s;", (which_word,))
records = cur.fetchall()

if len(records) > 0:
	print 'Total number of occurences of %s: %s' %(which_word, records[0][0])
else:
	cur.execute("SELECT word, count from tweetwordcount order by word asc;")
	records = cur.fetchall()
	print records






