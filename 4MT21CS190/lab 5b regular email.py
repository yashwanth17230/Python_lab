import re
phone=re.compile(r'\+\d{12}')
email=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]{5}+\.[A-Z/a-z]{2,}')
with open("example.txt",'r')as f:
    for line in f:
        matches=phone.findall(line)
        for match in matches:
            print(match)
        matches=email.findall(line)
        for match in matches:
            print(match)
