import re

text = input("Texto a analizar: ")

pattern = r"\d{2}/\d{2}/\d{4}"
bestpattern = r"\b(?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[0-2])/(?:17\d\d|18\d\d|19\d\d|20\d\d)\b"


date = re.findall(pattern, text)
bestdate = re.findall(bestpattern, text)

print("Fechas (Forma Simple): \n", date)
print("Fechas (controlando dias [01-31], meses [01-12]): \n", bestdate)

