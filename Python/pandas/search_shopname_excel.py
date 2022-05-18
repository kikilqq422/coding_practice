import numpy_prac as np
import pandas as pd
from pandas import Series,DataFrame

df_shop_id=pd.read_excel(r"F://峥呈//metabase数据11.11//5-二级商户号.xlsx")
df_data = pd.read_excel(r"F://峥呈//metabase数据11.11//重录汇总9.03.xlsx")
index_l = []
for id in df_shop_id["二级商户号"]:
    for index in df_data.index:
        if (df_data.iloc[index].isin([id])).any():
            index_l.append(index)
df_p = df_data.iloc[sorted(list(set(index_l)))]

df_p.to_excel(r'F://峥呈//metabase数据11.11//整理.xlsx')