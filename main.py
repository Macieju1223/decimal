import re

# req = '([1-9]{3}\s[0-9]{3}\s[0-9]{3})'
# num = 'asdawd12as131 123 231 asd asdawdaw awd12 we 12323 31212 dasda'
# check = re.findall(req,num)
# print(check)

# req = '[1-9]{9}'
# num = 'adqwqdw123123123adsdasd123123123adszs321123312asdad'
# check = re.findall(req,num)
# print(check)

tekst = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book with number 16755456532. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged
with mail student@pwsz.edu.pl. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
passages with PL12344, and more recently with desktop publishing software like Aldus PageMaker including versions 
of Lorem Ipsum on 64-100."""

# numer telefonu:
req = '[1-9]{9}'
check = re.findall(req,tekst)
print(check)

# adresy email w tekscie:
req = '\w+@\w+.\w+'
check = re.findall(req,tekst)
print(check)

# numer rejestracyjny:
req = '[A-Z]{2,3}\d+'
check = re.findall(req,tekst)
print(check)

# szukanie kodu tekstowego w kodzie:

req = '\d+-\d+'
check = re.findall(req,tekst)
print(check)