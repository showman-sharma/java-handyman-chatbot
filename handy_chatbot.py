
import chatbot
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

lemmatizer = WordNetLemmatizer()
def customtokenize(str):
    #Split string as tokens
    tokens=nltk.word_tokenize(str)
    #Filter for stopwords
    nostop = list(filter(lambda token: token not in stopwords.words('english'), tokens))
    #Perform lemmatization
    lemmatized=[lemmatizer.lemmatize(word) for word in nostop ]
    return lemmatized


import sys
if __name__ == '__main__':

    try:

        user_reply = " ".join(sys.argv[1:])
        print("User: "+user_reply)
    except:
        user_reply = None
    chatbot = chatbot.chatbot()
    bot_reply, convo = chatbot.respond(user_reply)
    print(convo)
    for line in bot_reply:
        print('Handy: '+line.strip())



