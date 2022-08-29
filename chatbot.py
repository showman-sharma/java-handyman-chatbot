from sklearn import preprocessing
import numpy as np
import pickle
from tensorflow import keras



class chatbot:
    def __init__(self):

        #Loading a Model 
        self.loaded_model = keras.models.load_model("chatbot_model");

        #Print Model Summary
        # self.loaded_model.summary()

        #Convert input into IF-IDF vector using the same vectorizer model
        self.vectorizer = pickle.load( open( "bot_vectorizer.p", "rb" ) );

        self.encoder = preprocessing.LabelEncoder();
        self.encoder.classes_ = np.load('bot_label_encoder.npy',allow_pickle=True);


        self.start_state = 'start_convo'
        self.end_state = 'end_convo'

        #Loading Bot Replies
        bot_reply_classes = [self.start_state]+list(self.encoder.classes_) 
        self.bot_replies = {}
        for reply_class in bot_reply_classes:
            with open('bot_replies/'+reply_class+'.txt') as f:
                self.bot_replies[reply_class] = f.readlines()

    def respond(self,user_reply):
        if user_reply==None or len(user_reply)<=3:
            state = self.start_state
            print("\n\n")
        else:
            predict_tfidf=self.vectorizer.transform([user_reply]).toarray();
            prediction=np.argmax( self.loaded_model.predict(predict_tfidf), axis=1 );  
            state = self.encoder.inverse_transform(prediction)[0]
        convo = True
        if state == self.end_state:
            convo = False
                
        return self.bot_replies[state], convo      





# state = start_state
# while state!=end_state:
#     for line in bot_replies[state]:
#         print('Handy: '+line.strip())
        
#     user_reply = input('user: ')
    
#     predict_tfidf=vectorizer.transform([user_reply]).toarray();
#     prediction=np.argmax( loaded_model.predict(predict_tfidf), axis=1 );
    
#     state = encoder.inverse_transform(prediction)[0]
# for line in bot_replies[state]:
#     print('Handy: '+line.strip())