import cx_Oracle
import sys
from collections import namedtuple

table = namedtuple('Name', 'name id_field fields')

Service     = table("service",      "serviceId",    ("serviceName",))
Post        = table("post",         "postId",       ("postName", "salary", "serviceId", "fk_post"))
Staff       = table("staff",        "StaffId",      ("name", "postId"))
Performance = table("performance",  "PerformanceId",("performanseName", "performansePrice", "description"))
Role        = table("role",         "RoleId",       ("roleName", "PerformanceId"))
Cast        = table("cast",         "CastId",       ("roleId", "personId"))
Requisite   = table("requisite",    "RequisiteId",  ("requisiteName", "requisitePrice"))
Decoration  = table("decoration",   "DecorationId", ("performanceId", "requisiteId"))
Place       = table("place",        "PlaceId",      ("placeType", "placePrice"))
Timetable   = table("timetable",    "TimetableId",  ("eventType", "eventDate", "performanceId"))
Booking     = table("booking",      "BookingId",    ("eventId", "placeId", "placeNo"))

tables = (Service,
          Post,
          Staff,
          Performance,
          Role,
          Cast,
          Requisite,
          Decoration,
          Place,
          Timetable,
          Booking)

operations = ("create",
              "read",
              "update",
              "delete")

connection = cx_Oracle.connect('NAME/q@localhost:1521')
cursor = connection.cursor()


def fixup_fields(fields):
    if len(fields) == 1:
        fields = '({})'.format(fields[0])
    else:
        fields = str(fields).replace('\'', '')
    return fields


def fixup_values(values):
    values = str(values).replace("[", "(")
    values = values.replace("]", ")")
    if len(values) == 1:
        values = '(\'{}\')'.format(values[0])
    return values


def create(table, fields, values):
    fields = fixup_fields(fields)
    values = fixup_values(values)
    try:
        query = "INSERT INTO {} {} VALUES {}".format(table, fields, values)
        cursor.execute(query)
        connection.commit()
    except cx_Oracle.DatabaseError:
        info_string = "Specify '{}' correctly to commit create operation for '{}' table".format(fields, table)
        print(info_string)


def read(table):
    query = 'SELECT * FROM {}'.format(table)
    cursor.execute(query)
    for result in cursor:
        print result


def delete(table, field, value):
    value = value[0]
    query = 'DELETE FROM {} WHERE {}={}'.format(table, field, value)
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
    except cx_Oracle.DatabaseError:
        info_string = "Specify '{}' correctly to commit delete operation for '{}' table".format(field, table)
        print(info_string)


def process_operation(table, operation, fields_info):
    if operation == "create":
        create(table.name, table.fields, fields_info)
    if operation == "read":
        read(table.name)
    if operation == "delete":
        delete(table.name, table.id_field, fields_info)


if __name__ == '__main__':
    for table in tables:
        if sys.argv[1] == table.name and sys.argv[2] in operations:
            process_operation(table, sys.argv[2], sys.argv[3:])
            exit(0)
    print("Specify table & operation correctly")

    # print('===================================================')
    # create(Requisite.name, Requisite.fields, ('brains', '1000'))
    # read(Requisite.name)

    # print('===================================================')
    # create(Requisite.name, Requisite.fields, ('brains', '1000'))
    # read(Requisite.name)
    #
    # print('===================================================')
    # delete(Requisite.name, Requisite.id_field, 48)
    # read(Requisite.name)
    #
    # print('===================================================')
    # create(Service.name, Service.fields, ('stage',))
    # read(Service.name)
    #
    # print('===================================================')
    # delete(Service.name, Service.id_field, 14)
    # read(Service.name)

    # connection.commit()
    cursor.close()
    connection.close()