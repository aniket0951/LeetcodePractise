import pandas as pd 

arr = [1,2,3,4,5,6]
df = pd.DataFrame(arr)

a = pd.read_csv(".//aniket.csv")
# print(a)
# print(a.columns)
print(a.head())