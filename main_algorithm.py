from __future__ import absolute_import
from __future__ import print_function
import six
__author__ = 'a_medelyan'

import rake
import operator
import io
import nltk
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

import random

import tkinter as algo
from tkinter import filedialog


def objective_generator(mystring):

    # text = word_tokenize(mystring)
    # POS_tag = nltk.pos_tag(text)

    # wordnet_lemmatizer = WordNetLemmatizer()
    # adjective_tags = ['JJ','JJR','JJS']
    # lemmatized_text = []

    # for word in POS_tag:
    #     if word[1] in adjective_tags:
    #         lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
    #     else:
    #         lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0]))) #default POS = noun
            
    # print ("Text tokens after lemmatization of adjectives and nouns: \n")
    # print (lemmatized_text)
    
    # for word in lemmatized_text:
    #     print (word+"-->"+WordNetLemmatizer().lemmatize(word,'v'))

    # front end
    Height=600
    Width=1200
    count=0

    resultwindow = algo.Tk()
    resultwindow.state('zoomed')

    canvas=algo.Canvas(resultwindow, bg='green', width=Width)

    scroll_y = algo.Scrollbar(resultwindow, orient="vertical", command=canvas.yview)

    resultwindow.title("Objective Questions")
    frame1=algo.Frame(canvas, bg='blue')
    frame1.place(relwidth=1, relheight=1)

    canvas.create_window(100, 100, anchor='nw', window=frame1, width=1350)

    T = algo.Text(frame1, font='Georgia', wrap=algo.WORD, padx=20, height=3) 
    T.pack(anchor='n')
    T.insert(algo.END,mystring) 


    print(mystring)
    
    stoppath = "data//stoplists//ourstopword.txt"
    rake_object = rake.Rake(stoppath, 5, 3, 4)
    sample_file = io.open("mcq.txt", 'r',encoding="iso-8859-1")
    text = sample_file.read()
    keywords = rake_object.run(text)
    # print(keywords)

    # following para is for stopword and arranging them in array
    with open('data//stoplists//ourstopword.txt', 'r') as file:
        stopword = file.read().replace('\n', ' ')
        stopwords=stopword.split()





    with open('mcq.txt', 'r') as file:
        string1 = file.read().replace('\n', '')
    # string1= open("mcq.txt",'r')
    splitstring= string1.split()
    list1=[]
    i=0
    for word in splitstring:
        if word == 'is':
            x=i-1
            # if splitstring[x-1] not in stopwords:
            list1.append(splitstring[x])        
        i=i+1
    # print(list1)



    # mystring =  '''Romeo and Juliet was written by William shakespeare. His name is Sandesh Sukubhattu. 
    # lines of code is called program.  That program is named as that statue. the program with two lines of codes is named as binary program. 
    # prime machine was developed in 1990s.'''

    # for question and .... (keyword)
    defword = ['is called','was called','named as','developed in','lunched in','developed by',
    'invented in','invented by','presented in','presented by','viewed in','viewed by','called by','named by','written by','read by']
    
    # for ....and question(keyword)
    beforedefword = [' is ','was','will']


    sentence=sent_tokenize(mystring)
    for onesentence in sentence:
        for onedefword in defword:
            before_keyword, keyword, after_keyword = onesentence.partition(onedefword)
            # print(before_keyword, after_keyword)
            after=after_keyword.split()
            before=before_keyword.split()

            t=[]
            option=[]
            
            for afterword in after:
                tokenwordcount=0
                for beforeword in before:

                    text = word_tokenize(beforeword)
                    POS_tag = nltk.pos_tag(text)

                    wordnet_lemmatizer = WordNetLemmatizer()
                    adjective_tags = ['JJ','JJR','JJS']
                    lemmatized_text = []

                    for word in POS_tag:
                        if word[1] in adjective_tags:
                            lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
                        else:
                            lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0]))) #default POS = noun
                            
                    # print ("Text tokens after lemmatization of adjectives and nouns: \n")
                    # print (lemmatized_text)
                    
                    for word in lemmatized_text:
                        beforeword_lem = WordNetLemmatizer().lemmatize(word,'v')
                    # print(beforeword_lem)

                    if beforeword_lem.lower() not in stopwords:
                        tokenwordcount=tokenwordcount+1
                if tokenwordcount>1:

                    #lemitization start
                    text = word_tokenize(afterword)
                    POS_tag = nltk.pos_tag(text)

                    wordnet_lemmatizer = WordNetLemmatizer()
                    adjective_tags = ['JJ','JJR','JJS']
                    lemmatized_text = []

                    for word in POS_tag:
                        if word[1] in adjective_tags:
                            lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
                        else:
                            lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0]))) #default POS = noun

                    for word in lemmatized_text:
                        afterword_lem = WordNetLemmatizer().lemmatize(word,'v')
                    #lemitization end

                    if afterword_lem.lower() in stopwords:
                        break
                    else:
                        x=re.search("[,]|[.]|[!]",afterword)
                        if x:
                            y=222
                            if re.search("[,]|[.]",afterword):
                                last=re.sub("[,]|[.]","",afterword,1,0)
                                if last not in stopwords:
                                    t.append(last)
                                    print("keyword:",' '.join(t))

                                    print (before_keyword, onedefword,"........")
                                    print("option a:", ' '.join(t))
                                    print("option b:", "something")

                                    option.append(' '.join(t))
                                    option.append('something1')
                                    option.append('something2')
                                    option.append('something3')

                                    random.shuffle(option)

                                    T = algo.Text(frame1, font='Georgia', wrap=algo.WORD, padx=20, height=3) 
                                    T.pack(anchor='n')
                                    T.insert(algo.END,'\n')
                                    T.insert(algo.END,before_keyword)
                                    T.insert(algo.END, onedefword) 
                                    T.insert (algo.END,'......')
                                        
                                    x=1    
                                    for options in option:  
                                          
                                        radiobutton= algo.Radiobutton(frame1, text=options, bg='white', borderwidth=3, activeforeground='blue', variable=count, value=x, selectcolor='white', tristatevalue=0)
                                        radiobutton.pack(anchor='w', side='top', ipadx=300)
                                        x=x+1

                                    count=count+1
                                    
                                    T.insert(algo.END, ' \n')

                            break
                        else:
                            t.append(afterword)


    # print("\n")    
    
        for onedefword in beforedefword:
            before_keyword, keyword, after_keyword = onesentence.partition(onedefword)
            # print(before_keyword, after_keyword)
            after=after_keyword.split()
            before=before_keyword.split()
            t=[]
            numofstopinbefore=0
            tokenwordcount=0
            option=[]
            for afterword in after:
                #lemitization start
                text = word_tokenize(afterword)
                POS_tag = nltk.pos_tag(text)

                wordnet_lemmatizer = WordNetLemmatizer()
                adjective_tags = ['JJ','JJR','JJS']
                lemmatized_text = []

                for word in POS_tag:
                    if word[1] in adjective_tags:
                        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
                    else:
                        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0]))) #default POS = noun

                for word in lemmatized_text:
                    afterword_lem = WordNetLemmatizer().lemmatize(word,'v')
                #lemitization end
                if afterword_lem.lower() not in stopwords:
                    tokenwordcount=tokenwordcount+1
            if tokenwordcount>1:
                    for beforeword in before:   
                        #lemitization start
                        text = word_tokenize(beforeword)
                        POS_tag = nltk.pos_tag(text)

                        wordnet_lemmatizer = WordNetLemmatizer()
                        adjective_tags = ['JJ','JJR','JJS']
                        lemmatized_text = []

                        for word in POS_tag:
                            if word[1] in adjective_tags:
                                lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
                            else:
                                lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0]))) #default POS = noun

                        for word in lemmatized_text:
                            beforeword_lem = WordNetLemmatizer().lemmatize(word,'v')
                        #lemitization end         
                        if beforeword_lem.lower() in stopwords:
                            numofstopinbefore=numofstopinbefore+1
                        if numofstopinbefore==len(before):
                            break
                        else: 
                            t.append(beforeword)
                    if numofstopinbefore != len(before) and len(t)<4:
                        print("........",keyword,after_keyword)
                        print("option a:", ' '.join(t))
                        print("option b:", "something")

                        r=' '.join(t)

                        option.append(' '.join(t))
                        option.append('something1')
                        option.append('something2')
                        option.append('something3')

                        random.shuffle(option)

                        T = algo.Text(frame1, font='Georgia', wrap=algo.WORD, padx=20, height=3) 
                        T.pack(anchor='n')
                        T.insert(algo.END,'\n')
                        T.insert (algo.END,'......')
                        T.insert(algo.END,keyword)
                        T.insert(algo.END, after_keyword) 
                        
                                        
                        x=1    
                        for options in option:    
                            radiobutton= algo.Radiobutton(frame1, text=options, bg='white', borderwidth=3, activeforeground='blue', variable=count, value=x, selectcolor='white', tristatevalue=0)
                            radiobutton.pack(anchor='w', side='top', ipadx=300)
                            x=x+1

                        count=count+1
                                    
                        T.insert(algo.END, ' \n')



    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'), 
                    yscrollcommand=scroll_y.set)
                    
    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')


    # resultwindow.mainloop()
if __name__=="__main__":
    objective_generator('''Romeo and Juliet was written by William shakespeare. Ram has gone to Kathmandu to manage better desks. His name is Sandesh Sukubhattu. lines of code is called program.  That program is named as that statue. the program with two lines of codes is named as binary program. prime machine was developed in 1990s.''')