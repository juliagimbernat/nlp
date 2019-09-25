#sentiment analysis example

import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from  sklearn.metrics  import accuracy_score

#Code to create a csv file from raw data downloaded
""" 
folder = 'aclImdb'

labels = {'pos': 1, 'neg': 0}

df = pd.DataFrame()

for f in ('test', 'train'):    
    for l in ('pos', 'neg'):
        path = os.path.join(folder, f, l)
        for file in os.listdir(path):
            with open(os.path.join(path, file),'r', encoding='utf-8') as infile:
                txt = infile.read()
            df = df.append([[txt, labels[l]]],ignore_index=True)

df.columns = ['review', 'sentiment']

df.to_csv('movie_data.csv', index = False, encoding ='utf-8')

df.head()
"""

#Code accessing data directly from the created csv file

userdir = "/Users/juliagimbernat/Desktop/newname"
filename = "movie_data.csv"

df = pd.read_csv("{}/{}".format(userdir, filename), sep=',', header=0)
print(df.review[0])

reviews = df.review.str.cat(sep=' ')

#function to split text into word
tokens = word_tokenize(reviews)
vocabulary = set(tokens)

print(len(vocabulary))


#print(frequency_dist)

stop_words = set(stopwords.words('english'))
print(stop_words)
tokens = [w for w in tokens if not w in stop_words]

frequency_dist = nltk.FreqDist(tokens)

sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]

#Create WordCloud
wordcloud = WordCloud().generate_from_frequencies(frequency_dist)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


"""
#Building the Model
X_train = df.loc[:24999, 'review'].values
y_train = df.loc[:24999, 'sentiment'].values
X_test = df.loc[25000:, 'review'].values
y_test = df.loc[25000:, 'sentiment'].values

vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)
print(train_vectors.shape, test_vectors.shape)

clf = MultinomialNB().fit(train_vectors, y_train)

#Our Sentiment Analyzer is already trained
#Now let us test!

predicted = clf.predict(test_vectors)
print(accuracy_score(y_test,predicted))

"""