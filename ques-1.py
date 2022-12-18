import pandas as pd
a1=list(map(int,input().split()))
b2=list(map(int,input().split()))
a1_series=pd.Series(a1)
b2_series=pd.Series(b2)
print(a1_series,b2_series)
operator=input("please choose the operation:")
if operator=='*':
    print(a1_series*b2_series)
elif operator=='+':
    print(a1_series+b2_series)
elif operator=='-':
    print(a1_series/b2_series)
elif operator=='*':
    print(a1_series/b2_series)
else:
    print("choose correct operator")