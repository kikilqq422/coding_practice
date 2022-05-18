import pandas as pd
import openpyxl
from openpyxl import load_workbook
import base64
import xlwings as xw
import warnings
import numpy as np

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

# data = df.iloc[0:5, 0:5]
# 转换数据格式
# data = data.astype(str)
# print(data)
# df1 = df1.astype(str)


# 读取两个表的数据，将表中所有列转换为str格式,会导致shop_id, index 自动为204.0等，为了避免此类问题，先将两列强转为int,后面在单独转为str:
# converters={'index':int}
# na_filter不检查空值，及不填充nan
df1 = pd.read_excel(r'shops0513.xlsx',dtype=str,na_values='',na_filter=False,converters={"shop_id":int});
df2 = pd.read_excel(r'bank0513.xlsx',dtype=str,na_values='',na_filter=False,converters={"index":int});

# 将'shop_id'强行处理为字符串
df1['shop_id']=df1['shop_id'].astype(str)
print(df1['shop_id'].head())
# print(df2.dtypes)
# print(df1.dtypes)
# 查看全部数据的类型，全部都是object，实际上已经转化为str了！！！

# 打印df2['index']值来确认是3还是3.0，再进行条件塞选：得力index=3
print(df2['index'].head())

# #在df2中，将得力的数据塞选出来，index=3,此处需要选打印
df3 = df2[df2['index']==3]

# 塞选出收银台商户中的必要列
df5 = df3[['sub_mer_id','account','mobile_phone','account_name','bank_name']]
# print(df5.head())

#内联的方式，将shops_messages的商户信息,以及收银台里面的固定列信息塞选出来
df4 = pd.merge(df1,df5,left_on='sub_mer_id',right_on='sub_mer_id')

#按时间戳进行BSE64编码，形成shop_key
area = df4.loc[:,'gmt51_modify']

# 测试一下就是df4['shops_key'][i]为空，才进行编码
# for i in range(len(df4)-5,len(df4)):
#     print("i",i)
#     if df4['shops_key'][i] == '':
#         print("null:", df4['shops_key'][i])

# for i in range(1192,len(df4)):

# 看一下最后几行的'shops_key'是否为空
print(df4['shops_key'].tail(5))

# 预判剩余几行，只对这几行进行编码：
for i in range(len(df4)-2,len(df4)):
    s = area.iloc[i]
    if df4['shops_key'][i] == '':
        print("",df4['shops_key'][i])
        df4['shops_key'].iloc[i]=str(base64.b64encode(s.encode('utf-8')),'utf-8')
        print(i,df4['shops_key'].iloc[i])
    i = i + 1

# 补齐shop_key的位数
df4['shops_key_final'] = "https://dlfp.cvillazc.com/smdd/banklogin?appid=1&param=" + df4['shops_key']
#补齐shop_id的位数
df4['shop_id']='00'+ df4['shop_id']

# 准备两个dataframe写入的一个新的Excel表中，data写入一张Excel的两个不同名的sheet中，解决pandas写入数据覆盖问题
writer = pd.ExcelWriter(r'内部整理0513.xlsx');

df4.to_excel(writer, sheet_name='商户',index=False,na_rep='');
df3.to_excel(writer, sheet_name='收银台',index=False,na_rep='');
df4.to_excel(writer, sheet_name='码牌表', index=False,na_rep='',columns=['province_address','market_address','shop_id','sub_mer_abbreviation','shops_fact_address','charge_phone','remark','sub_mer_abbreviation','sub_mer_id','charge_name','account','account_name','bank_name'],header=['省','市','码牌编号','商户名称','地址','联系电话(登录用户名)','门店标签','二级商户名','二级商户号','法人姓名','二级商户账号','收款户名','开户行名称'])

writer.save();

# 将码牌表单独制作,mode='a'表示追加，append数据,只能是在已有的Excel里面添加新的sheet，如果要在已有的sheet里面追加数据，需要把新旧数据concat
writer1 = pd.ExcelWriter(r'码牌表0513.xlsx',engine='openpyxl');
# data_old = pd.read_excel(r'码牌表0419.xlsx',index_col=None);
# print(data_old);
# data_old.to_excel(writer1, sheet_name='码牌表', index= False, header=None);


# 获取原Excel中数据的行数,（row_num , column_num）
row = df4.shape[0]
shape = df4.shape

print('row： ',row)
print('shape: ', shape)

df4.to_excel(writer1,sheet_name='码牌表',startrow=0,index=False,na_rep='',columns=['province_address','market_address','shop_id','sub_mer_abbreviation','shops_fact_address','charge_phone','remark','sub_mer_abbreviation','sub_mer_id','charge_name','account','account_name','bank_name'],header=['省','市','码牌编号','商户名称','地址','联系电话(登录用户名)','门店标签','二级商户名','二级商户号','法人姓名','二级商户账号','收款户名','开户行名称'])
# 从df4的全量商户表中，制作码牌表必要数据；单独打印码制作表出来
df4.to_csv(r'码牌表制作0513.csv',index=False, header= False, na_rep='',columns=['shop_id','sub_mer_abbreviation','shops_key_final','province_address','market_address'],encoding='gbk')
writer1.save()

# 试图追加数据失败
# 将码牌表单独制作,mode='a'表示追加，append数据,只能是在已有的Excel里面添加新的sheet，如果要在已有的sheet里面追加数据，需要把新旧数据concat
# writer1 = pd.ExcelWriter(r'码牌表0419.xlsx',engine='openpyxl',mode='w');
# 获取原Excel中数据的行数,（row_num , column_num）
# row = df4.shape[0]
# shape = df4.shape
# print('row： ',row)
# print('shape: ', shape)
# shape_new = df_new.shape
# print(shape_new)
# df4.to_excel(writer1,sheet_name='码牌表',startrow=row+1,index=False,na_rep='',columns=['province_address','market_address','shop_id','sub_mer_abbreviation','shops_fact_address','charge_phone','remark','sub_mer_abbreviation','sub_mer_id','charge_name','account','account_name','bank_name'],header=['省','市','码牌编号','商户名称','地址','联系电话(登录用户名)','门店标签','二级商户名','二级商户号','法人姓名','二级商户账号','收款户名','开户行名称'])
# 从df4的全量商户表中，制作码牌表必要数据；单独打印码制作表出来
