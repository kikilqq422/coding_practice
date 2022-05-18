import numpy_prac as np
import pandas as pd
from pandas import Series,DataFrame

df_shop_id=pd.read_excel(r"shopids.xlsx")
df_data = pd.read_excel(r"shop_messages.xlsx")
index_l = []
for id in df_shop_id["shop_name"]:
    for index in df_data.index:
        if (df_data.iloc[index].isin([id])).any():
            index_l.append(index)
df_p = df_data.iloc[sorted(list(set(index_l)))]

df_p.to_excel(r'result.xlsx')
