import re
import pandas as pd
import nltk
from nltk import pos_tag
from nltk import RegexpParser, Tree

userdir = "/Users/juliagimbernat/Desktop/newname"
filename = "vci_1543_abs_tit_key_apr_1_2019_train.csv"

df = pd.read_csv("{}/{}".format(userdir, filename), sep='\t', header=0)

wordList = []
wordListTag = []
tokenized_words = []
combo = []
def exp_studies_regex2(abstract):
    #wordList = re.sub("[^\w]", " ", abstract).split()
    #print(wordList)
    #print('\n')
    #for word in abstract:
    tokenized_words.append(nltk.word_tokenize(abstract))
    print(tokenized_words)
    print('')
    for w in tokenized_words:
        wordListTag.append(pos_tag(w))
    print(wordListTag)
    
    chunk_grammar = "AN: {<JJ><NN>}"
    chunk_parser = RegexpParser(chunk_grammar)
    #for w in wordListTag:
    #combo.append(chunk_parser.parse(wordListTag).pos())	
    #combo = chunk_parser.parse(wordListTag).pos()
    print('\n')
    #print(combo)
    
    flag = 0
    for token in combo:
        if token[1] == 'AN':
            flag = 1
            break
    return flag

print(exp_studies_regex2(df.Abstract[0]))

#label3 = []

#for a in df.Abstract:
    #label3.append(exp_studies_regex2(a))

#print(exp_studies_regex2)

#find_abstracts = lambda abstract: re.findall(r'[0-9]*\-?[0-9]+\%', abstract)
#df['new_col_abstracts'] = df['Abstract'].apply(find_abstracts)

#print(df.new_col_abstracts)


