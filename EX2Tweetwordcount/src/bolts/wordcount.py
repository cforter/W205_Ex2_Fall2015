from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
from collections import Counter
from streamparse.bolt import Bolt
#:conn = psycopg2.connect(database="Tcount", user="postgres", password="pass");

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1
	conn = psycopg2.connect(database="Tcount", user="postgres", password="pass");   
        cur = conn.cursor()
	cur.execute("SELECT word, count from tweetwordcount WHERE word = %s;", (word,))
	records = cur.fetchall()
	if len(records) > 0:
		cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s;", (self.counts[word], word))
		conn.commit()
	else:
		cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s);", (word, self.counts[word]))
		conn.commit()
        self.emit([word, self.counts[word]])
        self.log('%s: %d' % (word, self.counts[word]))
	conn.close()
