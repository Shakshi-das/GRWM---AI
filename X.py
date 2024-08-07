#import libraries

#essential libraries
import numpy as py
import pandas as pd
import datetime
import random

# Plots libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Stats
from scipy.stats import skew, norm
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax

# Ignore useless warnings
import warnings
warnings.filterwarnings(action="ignore")
pd.options.display.max_seq_items = 8000
pd.options.display.max_rows = 8000

# Visualizing the variables:
sns.pairplot(train)

Examining The Data:
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
train.head()
