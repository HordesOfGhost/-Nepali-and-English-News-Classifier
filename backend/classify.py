import numpy as np
import joblib
from backend.calculatetfidf import ProcessText,calc_tf_idf
import ast
model=joblib.load('model.pkl')
Category_class=['business', 'entertainment', 'politics', 'sport', 'tech']


with open('backend/idf.txt') as f:
     idf_load=f.read()
idf=ast.literal_eval(idf_load)

print(calc_tf_idf("abandon abandon abandon so abc abc   ability",idf)[0:5])

def count_word(word):
    cnt=word.count(" ")+1
    return cnt

def Predict_news(txt):
    text=ProcessText(txt)
    tf_idf=calc_tf_idf(txt,idf) 
    if all(i <.05 for i in tf_idf) or count_word(txt)<100:
        return("You cannot classify this text.")
    else:
        tf_idf_2=calc_tf_idf(" ",idf)
        tf_idf=np.append(tf_idf,tf_idf_2,axis=0)
        tf_idf=tf_idf.reshape(2,-1)
        #Predicting
        index=model.predict(tf_idf[0:1])
        return(f"The provided news text is classified as '{Category_class[int(index)].upper()}'")




