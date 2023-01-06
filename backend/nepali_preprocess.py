#from Nepali_nlp import Tokenizer

stop_words_file=open("backend/stopwords.txt","r",encoding="utf-8")
stop_words=stop_words_file.read()
stop_words=stop_words.split("\n")

nepali_num_file=open("backend/numbers.txt","r",encoding="utf-8")
nepali_num=nepali_num_file.read()
nepali_num=nepali_num.split(",")

nepali_suffix_file=open("backend/suffix.txt","r",encoding="utf-8")
nepali_suffix=nepali_suffix_file.read()
nepali_suffix=nepali_suffix.split("\n")

def count_word(word):
    cnt=word.count(" ")+1
    return cnt

def get_first_five_hundred_words(text):
    count=count_word(text)-1
    new_text=""
    for i in range(count):
        if i==50:
            break
        else:
            new_text += " "
            new_text += text.split(" ")[i]
    return new_text

def ProcessTextNepali(text):
    text=str(text)
    
    
    
    
    #removing \n and \ufeff
    remove=['\n','\ufeff']
    for i in remove:
        text.replace(i,'')
    
    #read stop words
    #Remove Stop Words
    #word_tokens = Tokenizer().word_tokenize(text)
    word_tokens = text.split(" ")
    filtered_list = [w for w in word_tokens if not w in stop_words]
    
    #Remove Nepali numbers
    num_filter=[]
    for i in range(0,len(filtered_list)):
        for j in range(0,len(nepali_num)):
            if nepali_num[j] in filtered_list[i]:
                num_filter.append(filtered_list[i])
                break
    for filter in num_filter:
        filtered_list.remove(filter)
    
    #Remove English numbers
    num=['0','1','2','3','4','5','6','7','8','9']
    num_filter=[]
    for i in range(0,len(filtered_list)):
        for j in range(0,len(num)):
            if num[j] in filtered_list[i]:
                num_filter.append(filtered_list[i])
                break
    for filter in num_filter:
        filtered_list.remove(filter)       
    
    #Stemming Manual
    
    
    
    stemmed_string=' '.join(filtered_list)
    
    #stemmed_string=' '.join(filtered_list)
    
    return stemmed_string