import psycopg2
conn = psycopg2.connect(database="Tcount", user="postgres", password="pass")
cur = conn.cursor()
cur.execute('''CREATE TABLE "tweetwordcount"
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()