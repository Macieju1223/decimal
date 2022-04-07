import re

req = '([1-9]{3}\s[0-9]{3}\s[0-9]{3})'
num = 'asdawd12as131 123 231 asd asdawdaw awd12 we 12323 31212 dasda'
check = re.findall(req,num)
print(check)

req = '[1-9]{9}'
num = 'adqwqdw123123123adsdasd123123123adszs321123312asdad'
check = re.findall(req,num)
print(check)