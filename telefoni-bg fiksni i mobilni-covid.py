#! python3
import re, pyperclip
phoneRegex=re.compile(r'''
(\+\d{12}) | (\d{10}) | (\d{7}-\d{3}) | (\+\d{5} \s \d{4}-\d{3})
''', re.VERBOSE)

text=pyperclip.paste()
extractedPhone=phoneRegex.findall(text)
puza=[j for i in extractedPhone for j in i if j]
print('\n'.join(puza)+'\n')

#spisak sa adresama i telefonima: http://www.heritage.gov.rs/cirilica/Download/Spisak__sa__adresama__i__telefonima__COVID__ambulanti__u__Domovima__zdravlja__grad__Beograd.pdf
#spisak mail adresa: https://www.vzsbeograd.edu.rs/attachments/article/711/%D0%A1%D0%BF%D0%B8%D1%81%D0%B0%D0%BA%20%D0%B8%D0%BC%D0%B5%D1%98%D0%BB%20%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0%20%D0%BD%D0%B0%D1%81%D1%82%D0%B0%D0%B2%D0%BD%D0%BE%D0%B3%20%D0%BA%D0%B0%D0%B4%D1%80%D0%B0%20.pdf
