import pandas as pd
import numpy as np
import random as rnd

train_df=pd.read_csv("titanic/train.csv")
test_df=pd.read_csv("titanic/test.csv")
combine=[train_df,test_df]
