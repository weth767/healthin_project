import pandas as pandas
import re

data = pandas.read_excel('../files/acompanhamento_doencas.xlsx')
data_frame = pandas.DataFrame(data)
records = data_frame.to_records()

file = open('inserts_diseases.sql', 'a', encoding='utf8')
for record in records:
    if re.search('[a-zA-Z][0-9]+:', str(record[1])):
        name = str(record[1]).split(':')[1]
        cid = str(record[1]).split(':')[0]
        sql = "insert into Inlness (name, cid, status) values('%s', '%s', true)" % (
            name, cid)
        file.write(sql + '\n')
file.close()
