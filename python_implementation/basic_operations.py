import cx_Oracle
from collections import namedtuple

table = namedtuple('Name', 'name id fields')

Service     = table("Service",      "serviceId",    ("serviceName",))
Post        = table("Post",         "postId",       ("postName", "salary", "serviceId", "fk_post"))
Staff       = table("Staff",        "StaffId",      ("name", "postId"))
Performance = table("Performance",  "PerformanceId",("performanseName", "performansePrice", "description"))
Role        = table("Role",         "RoleId",       ("roleName", "PerformanceId"))
Cast        = table("Cast",         "CastId",       ("roleId", "personId"))
Requisite   = table("Requisite",    "RequisiteId",  ("requisiteName", "requisitePrice"))
Decoration  = table("Decoration",   "DecorationId", ("performanceId", "requisiteId"))
Place       = table("Place",        "PlaceId",      ("placeType", "placePrice"))
Timetable   = table("Timetable",    "TimetableId",  ("eventType", "eventDate", "performanceId"))
Booking     = table("Booking",      "BookingId",    ("eventId", "placeId", "placeNo"))


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


def delete_template(table, field, value):
    query = 'DELETE FROM {} WHERE {}={}'.format(table, field, value)
    print(query)
    cursor.execute(query)


connection = cx_Oracle.connect('NAME/q@localhost:1521')
cursor = connection.cursor()

print('===================================================')
create_template(Requisite.name, Requisite.fields, ('brains', '1000'))
select_template(Requisite.name)

print('===================================================')
delete_template(Requisite.name, Requisite.id, 48)
select_template(Requisite.name)

print('===================================================')
create_template(Service.name, Service.fields, ('stage', ))
select_template(Service.name)

print('===================================================')
delete_template(Service.name, Service.id, 14)
select_template(Service.name)

# connection.commit()
cursor.close()
connection.close()
