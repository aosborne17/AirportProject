import pyodbc
from create_connection import Database_OOP
from customerinformation import user_interaction_passengers

ob1 = Database_OOP()

# info = ["Mr.", "Andrew", "Osborne", "1999-02-15", "Male", "British", "Passport", 2345643]
passenger_info = user_interaction_passengers()
cursor = ob1.establish_connection()
query = """ INSERT INTO [Passengers](title, first_name, last_name, date_of_birth, gender, nationality,
                                       travel_documentation, travel_doc_number)
                                       VALUES
                                       (?, ?, ?, ?, ?, ?, ?, ?) """

values = (passenger_info[0], passenger_info[1], passenger_info[2], passenger_info[3], passenger_info[4], passenger_info[5], passenger_info[6], passenger_info[7])

cursor.execute(query, values)
cursor.commit()

passengers = cursor.execute("SELECT * FROM Passengers")
for row in passengers:
    print(row)


