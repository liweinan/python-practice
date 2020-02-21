import numpy as np
import pandas as pd

# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

print("\n-=- pd.Series([1, 3, 5, np.nan, 6, 8]) -=-\n")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)

print("\n-=- pd.DataFrame -=-\n")
df = pd.DataFrame({'A': 1.,
              'B': pd.Timestamp('20130102'),
              'C': pd.Series(1, index=list(range(4)), dtype='float32'),
              'D': np.array([3] * 4, dtype='int32'),
              'E': pd.Categorical(["test", "train", "test", "train"]),
              'F': 'foo'})

print(df)

print("\n-=- pd.DataFrame.dtypes -=-\n")
print(df.dtypes)

print("\n-=- pd.DataFrame.head -=-\n")
print(df.head)

print("\n-=- pd.DataFrame.T -=-\n")
print(df.T)
