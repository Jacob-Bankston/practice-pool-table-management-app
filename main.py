import json
import datetime
import decimal
from tableclass import PoolTable

pool_tables = []
dict_pool_tables = []
user_input = ""
today = str(datetime.datetime.now())[0:10]
todays_json = f"{today}.json"
todays_txt = f"{today}.txt"
file_to_email = []
file_to_email.append(f"Information on the Pool Table Usage From - {today}\n")

def new_day_table_creator():
    for index in range(12):
        pool_table = PoolTable(index + 1)
        pool_tables.append(pool_table)
    for table in pool_tables:
        dict_pool_tables.append(table.__dict__)
    with open(todays_json, "w") as file_object:
        json.dump(dict_pool_tables, file_object)

def send_tables_data_to_json():
    for table in pool_tables:
        dict_pool_tables.append(table.__dict__)
    with open(todays_json, "w") as file_object:
        json.dump(dict_pool_tables, file_object)

def tables_data_from_json():
    with open(todays_json) as file_object:
        dict_pool_tables = json.load(file_object)
    for dict_table in dict_pool_tables:
        pool_table = PoolTable.from_dictionary(dict_table)
        pool_tables.append(pool_table)

def table_file_addition(table):
    file_to_email.append(f"Pool Table #{table.number} - Start Time {refined_time(table.start_time)} End Time {refined_time(table.end_time)} Total Time {time_played_conversion(table.total_time)} Cost ${table.total_cost}\n")

def admin_view():
    print("\n\n----------------------- Administrator Pool Table List -----------------------\n")
    for table in pool_tables:
        if table.occupied:
                print(f"Pool Table #{table.number} - OCCUPIED - Start time: {refined_time(table.start_time)} - Time Played: {time_played_conversion(get_the_time() - table.start_time)}")
        else:
            print(f"Pool Table #{table.number} - NOT OCCUPIED")

def get_user_input():
    while True:
        try:
            user_input =  input("Select an option from below!\n  1 - Book a Table   2 - Close a Table   3 - Shut Down Application\n")
            int_user_input = int(user_input)
            if int_user_input < 1 and int_user_input > 3:
                print("ERROR: Please enter one of the available options!")
            else:
                return user_input
        except ValueError:
            print("ERROR: Please enter one of the available options!")
        except IndexError:
            print("ERROR: Please enter one of the available options!")

def book_the_table(table):
    if table.occupied == True:
        print(f"ERROR: Pool Table #{table.number} is OCCUPIED.")
        get_booking_input()
    else:
        table.start_time = get_the_time()
        table.occupied = True
        print("Table Booked Successfully!\n")

def get_booking_input():
    while True:
        try:
            booking_input =  input("Please select a table to book: ")
            int_booking_input = int(booking_input)
            if int_booking_input < 1 or int_booking_input > 12:
                print("ERROR: Please enter one of the available options!")
            else:
                return (int_booking_input - 1)
        except ValueError:
            print("ERROR: Please enter one of the available options!")
        except IndexError:
            print("ERROR: Please enter one of the available options!")

def close_the_table(table):
    if table.occupied == False:
        print(f"ERROR: Pool Table #{table.number} is NOT OCCUPIED.")
        get_closing_input()
    else:
        table.end_time = get_the_time()
        table.total_time = table.total_time + table.end_time - table.start_time
        calculate_cost(table)
        table.occupied = False
        send_tables_data_to_json()
        print("Table Closed Successfully!")

def get_closing_input():
    while True:
        try:
            closing_input =  input("Please select a table to book: ")
            int_closing_input = int(closing_input)
            if int_closing_input < 1 or int_closing_input > 12:
                print("ERROR: Please enter one of the available options!")
            else:
                return (int_closing_input - 1)
        except ValueError:
            print("ERROR: Please enter one of the available options!")
        except IndexError:
            print("ERROR: Please enter one of the available options!")

def shutdown_functions():
    for table in pool_tables:
        if table.occupied == True:
            table.end_time = get_the_time()
            table.total_time = table.total_time + table.end_time - table.start_time
            calculate_cost(table)
            table.occupied = False
            send_tables_data_to_json()
        table_file_addition(table)
    with open(todays_txt, "w") as file_object:
        for i in range(12):
            file_object.write(file_to_email[i])

def get_the_time(): #returns the time in seconds of the day, not in the hours or minutes
    hours_to_seconds = int(str(datetime.datetime.now())[11:13]) * 60 * 60
    minutes_to_seconds = int(str(datetime.datetime.now())[14:16]) * 60
    seconds = int(str(datetime.datetime.now())[17:19])
    time = hours_to_seconds + minutes_to_seconds + seconds
    return time

def time_played_conversion(time):
    hours = round(time / 3600)
    minutes = round(((time % 3600) / 60))
    if hours == 0:
        return str(f"{minutes} minutes")
    if hours == 1:
        return str(f"{hours} hour and {minutes}")
    else:
        return str(f"{hours} hours and {minutes}")

def refined_time(time):
    hours = round(time / 3600)
    minutes = round(((time % 3600) / 60))
    return str(f"{hours}:{minutes}")

def calculate_cost(table):
    total_seconds = decimal.Decimal(table.total_time)
    total_cost = round(decimal.Decimal(total_seconds / 120), 2)
    table.total_cost = int(total_cost)

if len(pool_tables) == 0:
    new_day_table_creator()

while user_input != "q":
    admin_view()
    user_input = get_user_input()
    if user_input == "1":
        table_booking = get_booking_input()
        book_the_table(pool_tables[table_booking])
    if user_input == "2":
        table_closing = get_closing_input()
        close_the_table(pool_tables[table_closing])
    if user_input == "3":
        shutdown_functions()
        print("\n\nBye!\n\n")
        user_input = "q"