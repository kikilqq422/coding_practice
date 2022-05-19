import re
#
# num_define = re.compile(r'\d\,\d{3}')
# result = num_define.findall('42 1,234 6,368,745 12,34,567 1234')
# print(result)

# message = 'cell:556-896-5461, work: 459-986-7896'
# phonenum_regex = re.compile(r'((\d{3})-(\d{3}-\d{4}))') # group(), return tuple list
# mo = phonenum_regex.findall(message)
# print(mo)
# phonenum_regex = re.compile(r'(\d{3}-\d{3}-\d{4})') # group(), return tuple list
# mo = phonenum_regex.findall(message)
# print(mo)
#
# vowel_regex = re.compile(r'[aeiouAEIOU]')
# vowel_regex = re.compile(r'[^aeiouAEIOU]')

# nums = '''42
#           1,234
#           6,368,745
#           12,34,567
#           1234'''
# for num in nums.split():
    # print(num)
    # num_define = re.compile(r'^\d{1,3}(?:,\d{3})*$', re.DOTALL|re.VERBOSE)
    # result = re.search(num_define,num)
    # print(result.group())

# nums = '''42
#           1,234
#           6,368,745
#           12,34,567
#           1234'''
# for num in nums.split():
# num = '12,734,567'
# num_define = re.compile(r'''(?:\d{1,3}\,)
#                             (\d{3})*$)''', re.VERBOSE)
# result = re.findall(num_define,num)
# print(result)



# name = re.compile(r"^[A-Z][a-z]{1,}\s*Nakamoto", re.DOTALL)
# result = re.findall(name, 'Satoshi Nakamoto')
# print(result)

# name = re.compile(r"^[A-Z]\w+\s*Nakamoto", re.DOTALL)
# result = re.findall(name, 'Sata nakamoto')
# print(result)


# message = '''Alice throws baseballs.\
#           BOB EATS CATS.'''
# sentence = re.compile(r'(?:Alice|Bob|Carol)\s*(?:eats|pets|throws)\s*(?:apples|cats|baseballs).', re.I)
# result = re.findall(sentence, message)
# print(result)

'''日期检测：DD/MM/YEAR. day:(1,31),month:(01,12),year:(1000,2999),如果月份和天为单数，自动加0补齐两位'''
year_rex= '\d{4}'
month_rex = '\d{1,2}'
day_rex = '\d{1,2}'

# date_rex = re.compile(r'(0\d{1}|\d{2})\/(0\d{1}|\d{2})\/(\d{4})')
# date = '9/9/2010'
# result = re.findall(date_rex,date)
# print(result)
# year_num = int(input('please enter the year: '))
for year in range(1000,3000):
    if year % 4 == 0 and year % 400 == 0 and year % 100 != 0:
        print(year)
#     else:
#         date_rex = re.compile(year_rex)
#         year_result = re.findall(date_rex, year_num)
#     for month in range(1,13):
#         if month in (4,6,9,11):
#             day = range(30)
#         elif month == 2:
#             day = range(28)
#         else:
#             day = range(31)


'''7.18.1日期检测
编写一个正则表达式，可以检测 DD/MM/YYYY 格式的日期。假设日期的范围是01~31
月份的范围是01~12，年份的范围是1000~2999。请注意， 如果日期或月份是一位数字，会在 
前面自动加0。
该正则表达式不必检测每个月或闰年的正确日期;它将妾受不存在的日期，例如 31/02/2020或31/04/2021。
然后将这些字符串存储到名为 month、day和 year 的变量中，并编写其他代码以检测它是否为有效日期。
4月、6月、9月和11月有30天，2月有28天，其余月份为31天。闰年2月有29天。
闰年是能被4整除的年，能被100整除的年除外，除非它能被400整除这种计算使得用大小合理的正则表达式
来检测有效日期成为不可能的事，请注意原因'''

'''不区分闰年、平年来计算1000~2999的年份'''
year_rex = re.compile(r'[12][0-9]{3}')
result = re.findall(year_rex,'1900')
# print(result)



'''匹配日期与月份DD/MM，
   先匹配4月、6月、9月和11月有30天，
   2月有28天，其余月份为31天。
   闰年2月有29天'''
day_month_rex = re.compile(r'''(((0?[1-9]|[12][0-9]|30)-(0?[469]|11))   
                               |((0?[1-9]|[12][0-9]|3[01])-(0?[13578]|1[02]))
                               |((0?[0-9]|1[0-9]|2[0-8])-(0?2)))''', re.VERBOSE)

result = re.search(day_month_rex,'31-4').group()
# print('DD/MM:',result)

month_day_rex1 = re.compile(r'''(((0?[1-9]|[12][0-9]|30)/(0?[469]|11))   
                               |((0?[1-9]|[12][0-9]|3[01])/(0?[13578]|1[02]))
                               |((0?[0-9]|1[0-9]|2[0-9])/(0?2)))''', re.VERBOSE)

# result = re.search(day_month_rex,'29/2').group()
# print('DD/MM:',result)
#结合所有情况的月日匹配：
day_month_year_rex_final = re.compile(r'''
                                ((0[1-9]|[12][0-9]|3[01])-(0[469]|11))   
                               |((0[1-9]|[12][0-9]|30)-(0[123578]|1[02]))
                               |((0[1-9]|[1][0-9])-([2][0-8]))
                               |((0[1-9]|[1][0-9]-([2][0-9]))
                               -([12][0-9]{3}))
''', re.VERBOSE)

# result = re.search(day_month_year_rex_final,'9-9-1001').group()
# print(result)

# 强口令检测
# 写一个函数，使用正则表达式，确保传入的口令字符串是强口令
# 长度不少于8个字符，同时包含大小写，至少有1个数字
password = 'iupDpo2f'
'''检测长度：'''
len_rex = re.compile(r'.{8,}')
len_check = re.search(len_rex,password)
'''检测小写'''
alpha_rex = re.compile(r'[A-Z]+[a-z]+')
alpha_check = re.search(alpha_rex,password)
'''检测大写'''
num_rex = re.compile(r'\d+')
num_check = re.search(num_rex, password)
'''检测至少一个数字'''

if len_check:
    if not alpha_check or not num_check:
        print('at lease two alpha with lowercase and uppercase are needed')
        print('At lease one num is required')
    else:
        print('the password is strong')
else:
    print('the length is not enough')

git remote add origin https://github.com/liqq422/learning_git.git

$ ssh-keygen -t ed25519 -C "liqq422@hotmail.com"

#(r'(.*){5,}[A-Z]+[a-z]+[0-9]+')