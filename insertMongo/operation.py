from connection import Connection

class Operations():

    def save(self, data):
        try:
            db = Connection()
            db.database().insert_many(data)
            print('Save')

        except Exception as err:
            print("We had a problem saving data")
            print(err)




