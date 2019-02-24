import pandas as pd
import seaborn as sns

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

# Analysing the SalePrice column in the train dataset
train["SalePrice"].describe()

sns.distplot(train["SalePrice"])


