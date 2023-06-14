import re;

# https://blog.finxter.com/7-best-ways-to-remove-unicode-characters-in-python/
#https://stackoverflow.com/questions/3194516/replace-special-characters-with-ascii-equivalent

import re
def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]', '', text)
    

# print(remove_non_ascii(s))
#print(sent.encode("utf-8"))
#x = re.findall(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""", sent,re.A)
#print(x)sent

#

# string_unicode = sent
# string_encode = string_unicode.encode("ascii", "ignore")
# string_decode = string_encode.decode()
# print(string_decode)




#input string
#print(s.encode("ascii", "ignore").decode())


import unicodedata
sent = "Ángel Rodríguez"
s ="Familia de Medianoche, Season 01, Episode 104, Ramón, the Angel"
print(unicodedata.normalize('NFD', sent).encode('ascii', 'ignore').decode())
print(unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode())