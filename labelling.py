import pandas as pd
import sklearn

keyword_list = open('keywords0.txt').read().splitlines()

print(keyword_list)

userdir = "/Users/juliagimbernat/Desktop/abstracts_data.csv"

df = pd.read_csv(userdir)

print(df.label1)


change_name = lambda row: 0\
		if 'experimental-studies' in row.label1\
		else 1
df['true_label1'] = df.apply(change_name, axis = 1)

print(df.true_label1)




"""
change_name = lambda row: '0'\
		if row == 'experimental-studies' 
df['']df.apply(change_name, axis = 1)

"""
"""addtolabelcol = lambda row: 1\
        if '0' in row.Classification\
        else 0
df['true_label0'] = df.apply(addtolabelcol, axis=1)

change_name = lambda row: 0\
		if row.label1 == 'experimental-studies'\
		else 1
df['label1_nums'] = df.apply(change_name, axis = 1)