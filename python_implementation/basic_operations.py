import cx_Oracle


def fixup_fields(fields):
    if len(fields) == 1:
        fields = '({})'.format(fields[0])
    else:
        fields = str(fields).replace('\'', '')
    return fields


def fixup_values(values):
    if len(values) == 1:
        values = '(\'{}\')'.format(values[0])
    return values


def create_template(table, fields, values):
    fields = fixup_fields(fields)
    values = fixup_values(values)

    query = "INSERT INTO {} {} VALUES {}".format(table, fields, values)
    print(query)
    cursor.execute(query)


def select_template(table):
    query = 'SELECT * FROM {}'.format(table)
    cursor.execute(query)
    for result in cursor:
        print result


connection = cx_Oracle.connect('NAME/q@localhost:1521')
cursor = connection.cursor()

create_template('REQUISITE', ('REQUISITENAME', 'REQUISITEPRICE'), ('brains', '1000'))
select_template('REQUISITE')

print('===================================================')

create_template('SERVICE', ('SERVICENAME',), ('stage', ))
select_template('SERVICE')

# connection.commit()
cursor.close()
connection.close()
