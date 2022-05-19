import re,pyperclip

phone_num = re.compile(r'''(
   (\d{3}|\(\d{3}\)?)
   (\s*|-|\.)
   (\d{3}?)
   (\s*|-|\.)
   (\d{4}?)
   (\s*ext|x|ext\.)(\s*\d{2,5}?)
)''', re.VERBOSE)

email_verify = re.complie(r'''
    ([^\s+])
    @
    (\w+)
    (\.\w+)
'''
, re.VERBOSE)