import pandas as pd
# series的基本操作：
#               创建：1、直接创建；2、字典创建
#               查看的方式:通过索引，切片
#               增：
#               删：
#               改： 直接通过索引复制


# series竖起来的list,series有两列，index，数据行
#create
s1 = pd.Series([1,2,3,4])
print(s1)
s2 = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s2)

#字典形式创建
dic1 = {'name1':'jimmy','name2':'Tom','name3':'pepter'}
s4 = pd.Series(dic1)
# 更换/重置索引
s4.index = range(0,len(s4))
print('s4after:', s4)

# series的属性查看
print(s1.index)
print(s2.index)
print(s2.values)

# 操作series
# 通过index访问
print(s1[0])
print(s2['a':'d']) #元素切片
print(s2[['a','d']]) #按index来取值，只取index = 'a''d'的这连个元素

#增:不能直接append，一定要选存成series再append，最后一步一定要赋值
s3 = pd.Series(['tim'], index=['e'])
s2.append(s3)
print(s2)
s2= s2.append(s3)
print(s2)

#删除
s2 = s2.drop('a')
print(s2)
#判断一下某个值是否在Series里面
print('tim' != s2.values)

# 改，直接赋值,可以直接给多个元素赋值
s2['b','c'] = 'Tome'
print(s2)

# pandas DataFrame,相当于Excel表的表现形式，也是多个Series的集合
#        DataFrame的创建，列（column）名，index名的修改
#        增加一行数据
# df1 = pd.DataFrame({'name':['tim', 'tom', 'rose'],
#               'age':[10,11,12],
#               'income':[100,200,300]},index=['person1','person2','person3'])
#
# print(df1)

# 修改列名
# print(df1.columns)
# df1.columns = range(0,len(df1.columns))
# print(df1)
# #修改index名
# df1.index = range(0,len(df1.index))
# print(df1)
#
# #新增一条数据
# df1['pay'] = [100,200,300]
# print(df1)
#
# # 选定一行新增数据
# df1.insert(2,'gender',['M','F','F'])
#
# # 把其中一列换到指定位置
# df1.insert(1,'pay',df1.pop('pay'))
# print(df1)

# 按行来增加 行的index    要增加的列名
# df1.loc['person4',['name','age','income']] = ['rose',25,200]
# print(df1)

# 访问数据的方式,根据索引名来读取数据，index可以用index名和数字读取，column如果有名字，必须用名字读取
# 访问列与多列 df[[],[]]
# print(df1.age)
# print(df1[['age','name']])
# print(df1[[0,2]])

# 访问行
# print(df1[0:2])
# print(df1.loc[['person2','person3']])
# 读取某固定值
# print(df1.loc['person1','age'])

# 删除数据
# 删除一列并且在原数据上删除
# del df1['age']
# 删除一列数据，axis=1为row，=0为列，inplace=False表示不在源表上删除
# data = df1.drop('name',axis=1,inplace=False)
# print(df1)
# data = df1.drop('person1',axis=0,inplace=True)
# print(df1)

"""
loc()
iloc()
ix()
"""
import pandas as pd
import numpy as np
#生成指定日期,从'20180101'开始，向后+5天
datas = pd.date_range('20180101', periods=5)
#np.arange(30).reshape(5,6)总共30个数，形成5行6列的数据，列名为‘A’
df = pd.DataFrame(
        np.arange(30).reshape(5,6),index=datas,
        columns=['A','B','C','D','E','F'])

# print(df)

"""
三种方式本质上都是按照[x,y]轴取值，loc按照index名和column名来取值
三种方式本质上都是按照[x,y]轴取值，iloc按照index数字和column数字来取值
loc()方法
df.loc[x, y]
【标签索引】
"""
#打印某个值
print(df.loc['20180102','A'])
#打印某列值,表示x轴无取值，则用：代替
print(df.loc[:,'B'])
#打印某行值
print(df.loc['20180105',:])
#打印某些行
print(df.loc['20180104': , :])

"""
iloc()方法
位置索引
"""
#获取某个数据
df.iloc[0,1]
#获取某列
df.iloc[:,3]
#获取某几列
print(df.iloc[:,[0,2,3]])
#获取某行
#获取某些行
df.iloc[3:,:]


# dataFrame常用操作：排序，列值替换，列换顺序
dic = {'name': ['kiti', 'beta', 'peter', 'tom'],
          'age': [20, 18, 35, 21],
          'gender': ['f', 'f', 'm', 'm']}
df_new = pd.DataFrame(dic)
# 按照升序对表排序
df_new = df_new.sort_values(by = 'age')
# 按照降序对表排序
df_new = df_new.sort_values(by = 'age',ascending=False)
# print(df_new)

# 对列的值进行替换
df_new['gender'] = df_new['gender'].replace(['m','f'],['M','F'])

# 调换列值顺序
cols = ['name','gender','age']
# df_new = df_new.loc[:,cols]
# print(df_new)
