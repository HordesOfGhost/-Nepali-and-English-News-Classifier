import numpy as np
import joblib
from backend.calculatetfidf import ProcessText,calc_tf_idf
from backend.nepali_preprocess import ProcessTextNepali
import ast
import pickle

model=joblib.load('final_model.pkl')
Category_class=['business', 'entertainment', 'politics', 'sport', 'tech']

#idf values
with open('backend/idf.txt') as f:
     idf_load=f.read()
idf=ast.literal_eval(idf_load)
with open('backend/nepali_idf.txt',encoding='utf-8') as f:
     idf_load_nep=f.read()
nepali_idf=ast.literal_eval(idf_load_nep)

def count_word(word):
    cnt=word.count(" ")+1
    return cnt

def Predict_news(news):
    txt=news
    if not news[0:20].isascii():
        txt=ProcessTextNepali(txt)
        tf_idf=calc_tf_idf(txt,nepali_idf)
    else:    
        text=ProcessText(txt)
        tf_idf=calc_tf_idf(text,idf) 
    if all(i <.05 for i in tf_idf) or count_word(news)<00:
        return("You cannot classify this text.")
    else:
        confidence=model.predict_proba([tf_idf])
        index=np.argmax(confidence)
        confidence=[np.around(x*100,2) for x in confidence]
        return(f"The provided news text is classified as '{Category_class[int(index)].upper()}'",confidence)




