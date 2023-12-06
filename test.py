import re
import random
import string

txt = "gangsta rap! iu éééééeee"
x = re.sub('é', "e", txt)

y = 'Lynx'
aleaStr = ''
alpha = string.ascii_lowercase
print(alpha)

for i in range(5):
    alea = random.randint(0, 25)
    aleaStr += alpha[alea]

print(aleaStr)
print(y)
