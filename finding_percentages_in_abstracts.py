import re
import pandas as pd

userdir = "/Users/juliagimbernat/Desktop/newname"
filename = "vci_1543_abs_tit_key_apr_1_2019_train.csv"

df = pd.read_csv("{}/{}".format(userdir, filename), sep='\t', header=0)

#print(df.Abstract)

find_abstracts = lambda abstract: re.findall(r'[0-9]*\-?[0-9]+\%', abstract)
df['new_col_abstracts'] = df['Abstract'].apply(find_abstracts)

print(df.new_col_abstracts)


#result = re.findall(r'[0-9]*\-?[0-9]+\%', df.Abstract)