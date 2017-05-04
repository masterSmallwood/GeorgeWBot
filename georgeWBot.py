import sys
from random import choice



#Split everything up into functions... make georgeWBot its own class??


class GeorgeWBot(object):

    def __init__(self):

        # Create list of words from corpus.
        textfile = open("Selected_Speeches_George_.txt", "r", encoding="utf8")
        text = textfile.read()
        words = text.split()
        #print("corpus has " + str(len(words)) + " words.")

        #Need to clean up the text file a little bit.
        #This gets rid of all occurences of "————" followed by the next line. Which is always a page number...I think.
        while True:
            try:
                index = words.index("————")
                del words[index]
                del words[index]
            except ValueError:
                break

        # Build the dictionary from list of words.
        d = {}
        for i, word in enumerate(words):
            if i + 2 < len(words):
                key = (words[i], words[i + 1])
                if key not in d:
                    d[key] = []
                d[key].append(words[i + 2])

        self.d = d




    def makeSentence(self, d):
        endChars = [".", "!", "?"]
        # Create a sentence using the dictionary we made above.
        # Find first key that is a number since its the bible
        # Key starts with a number, since bible verses start with numbers
        startingWords = [key for key in d.keys() if key[0][0].isupper() and key[0][-1] not in endChars]
        # Choose a random key to start from
        key = choice(startingWords)

        # List to store our sentence
        sentence = []
        first, second = key
        sentence.append(first)
        sentence.append(second)

        while True:

            third = choice(d[key])
            sentence.append(third)
            if third[-1] in endChars:
                break

            # Increment the key
            key = (second, third)
            if key not in d.keys():
                break

            first, second = key

        sentenceString = ' '.join(sentence)

        return sentenceString


    """
    Algorithm for creating a tweet:
    sentence = new sentence
    if len(sentence) is < 80
        sentence2 = new sentence
        tweet = sentence + sentence2
        while tweet > 120 and tweet < 95:
            sentence2 = new sentence
            tweet = sentence + sentence2

        return tweet
    """
    def makeTweetText(self):

        tweet = self.makeSentence(self.d)
        #print(len(tweet))

        if len(tweet) < 80:
            charsLeft = 120 - len(tweet)
            tweet2 = self.makeSentence(self.d)
            fullTweet = tweet + " " + tweet2
            while len(tweet2) >charsLeft or len(tweet2) < 10:
                tweet2 = self.makeSentence(self.d)
                fullTweet = tweet + " " + tweet2
            return fullTweet

        elif len(tweet) > 120:
            return self.makeTweetText()

        else:
            return tweet

        #print("Length of tweet is " + str(len(tweet)) + " characters.")
        #print("\n" + tweet)


    #This method determines hashtags and creates the final tweet
    #tweetText is the string generated from makeTweetText()
    def createTweet(self,tweetText):
        #TODO

        triggerWords = ["terror","God","nuclear","Iraq","soldiers","freedom","al Qaeda"]
        defaultHashtags = ["#America","#USA","#GodBlessAmerica","#Congress","#GeorgeBush"]
        hashtag = choice(defaultHashtags)

        #figure out what hashtags to use
        tweetTextWords = tweetText.split()
        for word in tweetTextWords:
            if word in triggerWords:
                hashtag = "#" + word

        tweet = hashtag + " " + tweetText

        return tweet



#***************************************
#TESTING
#***************************************
if __name__ == "__main__" :

    myBot = GeorgeWBot()
    myBotsTweetText = myBot.makeTweetText()
    print(myBotsTweetText)
    myTweet = myBot.createTweet(myBotsTweetText)
    print(myTweet)
    print("tweet length is " + str(len(myTweet)))