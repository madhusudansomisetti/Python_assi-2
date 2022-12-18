import pandas as pd
number=list(map(int,input().split()))
n_ser=pd.Series(number)

print(n_ser*n_ser)