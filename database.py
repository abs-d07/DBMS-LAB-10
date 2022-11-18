import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lab_10"
)
c = mydb.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS train(Train_number text,Train_name TEXT,Train_type TEXT, Train_source TEXT, Train_destination TEXT,Train_availability text)')

def add_data(Train_number, Train_name, Train_type, Train_source, Train_destination, Train_availability):
    c.execute('INSERT INTO train(Train_number, Train_name, Train_type, Train_source, Train_destination, Train_availability) VALUES (%s,%s,%s,%s,%s,%s)',(Train_number, Train_name, Train_type, Train_source, Train_destination, Train_availability))
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM train')
    data = c.fetchall()
    return data


def get_train(Train_number):
    c.execute('SELECT * FROM train WHERE Train_number="{}"'.format(Train_number))
    data = c.fetchall()
    return data

def edit_train_data(new_train_number, new_train_name, new_train_type, new_train_source, new_train_destination,new_train_availability, Train_number, Train_name, Train_type, Train_source, Train_destination, Train_availability):
    c.execute("UPDATE train SET Train_number=%s, Train_name=%s, Train_type=%s, Train_source=%s, Train_destination=%s , Train_availability=%s WHERE Train_number=%s and Train_name=%s and Train_type=%s and Train_source=%s and Train_destination=%s and Train_availability=%s", (new_train_number, new_train_name, new_train_type, new_train_source, new_train_destination, new_train_availability , Train_number, Train_name, Train_type, Train_source, Train_destination , Train_availability))
    mydb.commit()
    return view_all_data()

    # return data

def delete_data(Train_number):
    c.execute('DELETE FROM train WHERE Train_number="{}"'.format(Train_number))
    mydb.commit()

# def view_only_dealer_names():
#     pass

def view_only_train_numbers():
    c.execute("SELECT Train_number FROM train")
    data=c.fetchall()
    return data
