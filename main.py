import re

str = 'piiig'
match = re.search(r'i+', str)

if match:
    print('wor:  ',match)
else:
    print('nope')

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0])  ## username
    print(tuple[1])  ## host

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

f = open('t.txt','r')
strings = re.findall(r'\w', f.read())
print('strings: ' , strings, ' type: ', type(strings))
print('\n-------------------------------\n')

em = 'student123@wp.com ala@kot.nl marciin kanarek rusland@wp.pl'
check = re.findall(r'\w+@\w+.\w+',em)
if check:
    print('true ', check)

print('----------------------------')

num = '^[1-9]([0-9]{8})'
check = '654654654'
result = re.match(num,check)
if result:
    print(result)


num = 'asd asda123aasdsa dasd'
check = re.search(r'\d*4',num)
print(check)
rek = 'Python main dot'
check = re.fullmatch(r'python',rek, flags = re.IGNORECASE)
print(check)

te = 'asdasdadasda Marcin Szwon asdasdasda'
req = '([A-Z][a-z]{3,}\s[A-Z][a-z]{3,})'
check = re.findall(req,te)
print(check)


