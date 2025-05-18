import re

text = "Encuentra ba9, be7"
pattern = r'\bb[aeiouAEIOU]\d\b'
matches = re.findall(pattern, text)
print(matches)