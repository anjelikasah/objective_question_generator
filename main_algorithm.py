from __future__ import absolute_import
from __future__ import print_function
import six
__author__ = 'a_medelyan'

import rake
import operator
import io
import nltk
from nltk.tokenize import sent_tokenize
import re

def objective_generator(mystring):
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

    defword = ['is called','was called','named as','developed in','lunched in','developed by',
    'invented in','invented by','presented in','presented by','viewed in','viewed by','called by','named by','written by','read by']

    sentence=sent_tokenize(mystring)
    for onesentence in sentence:
        for onedefword in defword:
            before_keyword, keyword, after_keyword = onesentence.partition(onedefword)
            # print(before_keyword, after_keyword)
            after=after_keyword.split()
            before=before_keyword.split()

            t=[]
            
            for afterword in after:
                tokenwordcount=0
                for beforeword in before:
                    if beforeword not in stopwords:
                        tokenwordcount=tokenwordcount+1
                if tokenwordcount>1:
                    if afterword in stopwords:
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
                            break
                        else:
                            t.append(afterword)


    print("\n")

    beforedefword = [' is ','was','will']
    for onesentence in sentence:
        for onedefword in beforedefword:
            before_keyword, keyword, after_keyword = onesentence.partition(onedefword)
            # print(before_keyword, after_keyword)
            after=after_keyword.split()
            before=before_keyword.split()
            t=[]
            numofstopinbefore=0
            tokenwordcount=0
            for afterword in after:
                if afterword not in stopwords:
                    tokenwordcount=tokenwordcount+1
            if tokenwordcount>1:
                    for beforeword in before:            
                        if beforeword.lower() in stopwords:
                            numofstopinbefore=numofstopinbefore+1
                        if numofstopinbefore==len(before):
                            break
                        else: 
                            t.append(beforeword)
                    if numofstopinbefore != len(before) and len(t)<4:
                        print("........",keyword,after_keyword)
                        print("option a:", ' '.join(t))
                        print("option b:", "something")

                        
