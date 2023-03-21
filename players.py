#import pickle

#aaron_judge = pickle.load( open( "aaron_judge.p", "rb" ) )
#jose_altuve = pickle.load( open( "jose_altuve.p", "rb" ) )
#david_ortiz = pickle.load( open( "david_ortiz.p", "rb" ) )

import pandas as pd

aaron_judge = pd.read_csv('aaron_judge.csv', index_col=0)
jose_altuve = pd.read_csv('jose_altuve.csv', index_col=0)
david_ortiz = pd.read_csv('david_ortiz.csv', index_col=0)