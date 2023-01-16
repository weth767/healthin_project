import pandas as pandas
from datetime import datetime
import uuid

data = pandas.read_excel('../files/consulta_medicamento.xls')
data_frame = pandas.DataFrame(data)
records = data_frame.to_records()
laboratories = []


def generate_laboratories():
    file = open('inserts_laboratories.sql', 'a', encoding='utf8')
    for record in records:
        split = str(record[5]).split(' - ')
        laboratory = str.join(' - ', split[0: len(split) - 1]).strip()
        cnpj = split[-1].strip().replace('-', '').replace('/',
                                                          '').replace('.', '')
        uuid_local = str(uuid.uuid4()).upper()
        sql = "insert into Laboratory (id, name, cnpj) values ('%s', '%s', '%s');" % (
            uuid_local, laboratory, cnpj)
        already_inserted = list(
            filter(lambda lab: lab[2] == cnpj, laboratories))
        if (len(already_inserted) == 0):
            laboratories.append([uuid_local, laboratory, cnpj])
            file.write(sql + '\n')
    file.close()


def generate_medicines():
    file = open('inserts_medicines.sql', 'a', encoding='utf8')
    for record in records:
        date_time = None
        split = str(record[5]).split(' - ')
        cnpj = split[-1].strip().replace('-', '').replace('/',
                                                          '').replace('.', '')
        uuid_lab = list(filter(lambda lab: lab[2] == cnpj, laboratories))[0][0]
        if (str(record[7]).startswith('nan')):
            sql = "insert into Medicine (name, activePrinciple, register, laboratoryId, expiration) values ('%s', '%s', '%s', '%s', null);" % (
                record[1], record[2], record[3], uuid_lab)
            file.write(sql + '\n')
            continue
        if len(str(record[7]).strip()) > 5:
            date_time = datetime.strptime(str(record[7]).strip(), '%m/%Y')
        else:
            date_time = datetime.strptime(str(record[7]).strip(), '%m/%y')
        sql = "insert into Medicine (name, activePrinciple, register, laboratoryId, expiration) values ('%s', '%s', '%s', '%s', '%s');" % (
            record[1], record[2], record[3], uuid_lab, date_time)
        file.write(sql + '\n')
    file.close()


if __name__ == '__main__':
    generate_laboratories()
    generate_medicines()
