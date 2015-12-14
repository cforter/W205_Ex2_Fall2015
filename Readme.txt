Steps for running application on an AWS Linux Instance
1) Clone repo on linux server
2) Make sure you have Python 2.7, PostgreSQL, Tweepy, and Streamparse installed
3) Run the db_setup.sh file to create a database and user
4) Run db_setup.py to create a table for storing tweet results
5) Navigate to EX2Tweetwordcount and type sparse run
6) The table 'tweetwordcount' will be filled with results from the twitter stream
7) Navigate to Serving_Scripts
  a. run finalresults.py to see results of twitter stream
  b. run histogram.py to see different results of twitter stream 
8) The top 20 words in my twitter stream is viewable under Plots -> Plot.png, 
  along with the Rcode used to create it. This needs ggplot2 installed to run.