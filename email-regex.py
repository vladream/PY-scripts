import re, pyperclip
emailRegex=re.compile(r'''
#something.+_@something.com

[a-zA-z0-9_.+]+                 #name part
@                               #@ symbol
[a-zA-z0-9_.+]+                 #domain name part
''', re.VERBOSE)

text=pyperclip.paste()

extractedEmail=emailRegex.findall(text)

results='\n' + '\n'.join(extractedEmail)
print(results)
#pyperclip.copy(results)



#spisak sa adresama i telefonima: http://www.heritage.gov.rs/cirilica/Download/Spisak__sa__adresama__i__telefonima__COVID__ambulanti__u__Domovima__zdravlja__grad__Beograd.pdf
#spisak mail adresa: https://www.vzsbeograd.edu.rs/attachments/article/711/%D0%A1%D0%BF%D0%B8%D1%81%D0%B0%D0%BA%20%D0%B8%D0%BC%D0%B5%D1%98%D0%BB%20%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0%20%D0%BD%D0%B0%D1%81%D1%82%D0%B0%D0%B2%D0%BD%D0%BE%D
