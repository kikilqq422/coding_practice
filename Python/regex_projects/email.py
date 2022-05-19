import re
email_verify = re.compile(r'''
    [a-zA-z0-9._%+-]+
    @
    [a-zA-z0-9.-]+
    (\.[a-zA-Z]{2,4})
'''
, re.VERBOSE)

a = email_verify.search('dwiopdjldjsldjlpdpl[sdfsdf350112370@qq.comfsfs')
print(a)