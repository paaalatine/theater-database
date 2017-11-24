import cx_Oracle
import sys
from collections import namedtuple

table = namedtuple('Name', 'name id_field fields')

Service     = table("service",      "serviceId",    ("serviceName",))
Post        = table("post",         "postId",       ("postName", "salary", "serviceId"))
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


def create(table, values):
    fields = fixup_fields(table.fields)
    values = fixup_values(values)
    try:
        query = "INSERT INTO {} {} VALUES {}".format(table.name, fields, values)
        cursor.execute(query)
        connection.commit()
    except cx_Oracle.DatabaseError:
        info_string = "Specify '{}' correctly to commit create operation for '{}' table".format(fields, table.name)
        print(info_string)


def read(table):
    query = 'SELECT * FROM {}'.format(table.name)
    cursor.execute(query)
    for result in cursor:
        print result


def update(table, values):
    query = "UPDATE {} SET {}={} WHERE {}={}".format(table.name, values[1], values[2], table.id_field ,values[0])
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
    except cx_Oracle.DatabaseError:
        info_string = "Specify '{}', field to update: {}, value correctly to commit update operation for '{}' table".format(table.id_field, table.fields, table.name)
        print(info_string)



def delete(table, value):
    value = value[0]
    query = 'DELETE FROM {} WHERE {}={}'.format(table.name, table.id_field, value)
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
    except cx_Oracle.DatabaseError:
        info_string = "Specify '{}' correctly to commit delete operation for '{}' table".format(table.id_field, table.name)
        print(info_string)


def process_operation(table, operation, fields_info):
    if operation == "create":
        create(table, fields_info)
    if operation == "read":
        read(table)
    if operation == "update":
        update(table, fields_info)
    if operation == "delete":
        delete(table, fields_info)


if __name__ == '__main__':
    for table in tables:
        if sys.argv[1] == table.name and sys.argv[2] in operations:
            process_operation(table, sys.argv[2], sys.argv[3:])
            exit(0)
    print("Specify table & operation correctly")

    cursor.close()
    connection.close()
