import psycopg2
conn = psycopg2.connect(database="Tcount", user="postgres", password="pass")
cur = conn.cursor()
print 'Choose a lower limit for occurences of a word'
lower_limit = raw_input()
print 'Choose an upper limit for occurences of a word'
upper_limit = raw_input()

cur.execute("SELECT word, count from tweetwordcount WHERE count > %s::numeric and count < %s::numeric order by count desc;",(lower_limit, upper_limit))
records = cur.fetchall()

for i in records:
	print str(i[0]) + ": " + str(i[1])



