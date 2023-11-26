# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:37:17 2023

@author: ziegl
"""

# Calculate the average sentiment of "tweets" using word sentiment database
# Each word was rated on a scale from 1-9 with 9 being the most positive connotation

# Create ANEW Dictionary
ANEW = {}
# Open the file
with open('ANEW.tsv', 'r') as file:
    for line in file:
        # Assign variables and account for tab
        word, value = line.strip().split('\t')
        # parse information and make values floats
        ANEW[word] = float(value)
# Open tweet file
with open('tweets.txt', 'r') as file:
    # Read the lines and convert to string
    tweets = file.readlines()
for tweet in tweets:
    # Separate each tweet into a list of individual words
    words = tweet.strip().split()

    # Perform sentiment analysis for each word in the tweet if the word is contained in ANEW file
    values = [ANEW[word] for word in words if word in ANEW]

    # Calculate the average sentiment value for the tweet
    if values:
        # Divide the sum of sentiment values by the number of words in a tweet
        average = sum(values) / len(values)
        # If word is not in ANEW or has no value, set to average of 4.5 on a 1-9 scale
    else:
        average = 4.5

    # Print the average sentiment value and the tweet
    print(average)
    print(tweet)
    
    # Results:
    
   # 7.803999999999999
   # love sunshine and the happy laughter of children

   # 7.383333333333333
   # we had to adopt an adorable puppy

   # 2.8800000000000003
   # I am agonizing over this dreadful noise

   # 4.978
   # we saw an alien craft crash in the park
