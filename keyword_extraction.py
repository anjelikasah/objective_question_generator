#Source of text:
#https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents

Text = "Compatibility of systems of linear constraints over the set of natural numbers. \
Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and \
nonstrict inequations are considered. \
Upper bounds for components of a minimal set of solutions and \
algorithms of construction of minimal generating sets of solutions for all \
types of systems are given. \
These criteria and the corresponding algorithms for constructing \
a minimal supporting set of solutions can be used in solving all the \
considered types of systems and systems of mixed types."

import nltk
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer


#nltk.download('punkt')

# def clean(text):
#     text = text.lower()
#     printable = set(string.printable)
#     text = filter(lambda x: x in printable, text) #filter funny characters, if any.
#     return text

# Cleaned_text = clean(Text)

text = word_tokenize(Text)

POS_tag = nltk.pos_tag(text)

wordnet_lemmatizer = WordNetLemmatizer()

adjective_tags = ['JJ','JJR','JJS']

lemmatized_text = []

for word in POS_tag:
    if word[1] in adjective_tags:
        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
    else:
        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0]))) #default POS = noun
        
print ("Text tokens after lemmatization of adjectives and nouns: \n")
print (lemmatized_text)