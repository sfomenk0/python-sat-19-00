#ASCII
words = [[67, 114, 121, 112, 116, 111, 32 , 65, 71], [49, 57, 53, 50, 45, 50, 48, 49, 56]]
company = [] #Crypto AG
years = [] #'1952—2018'
field_activity = 'сфере'
for i in words:
    if i == words[0]:
        for x in words[0]:
            company.append(chr(x))
    if i == words[1]:
        for y in words[1]:
            years.append(chr(y))


print(''.join(company) + ' — швейцарская , существовавшая в ' + ''.join(years) + ' годах и специализировавшаяся на технологиях в ' + field_activity + ' коммуникаций и информационной безопасности.')






