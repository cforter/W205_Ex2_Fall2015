### Make Bar Chart of Top 20 Words ###

library(ggplot2)
tweets <- read.csv("tweet_output.csv", header=F, col.names=c("Words","Count"))
# Reorder data by count
tweets <- transform(tweets, 
                          Words = reorder(Words, Count))

ggplot(tweets, aes(x = factor(tweets$Words), y=tweets$Count)) + 
  geom_bar(stat='identity', fill="dodgerblue") +
  xlab("Count of Words") +
  ylab("Words") +
  theme(axis.line = element_line(colour = NA),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) 

