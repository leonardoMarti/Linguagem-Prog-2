from pymongo import MongoClient

class Connection():

  def database(self):
    try:
      client = MongoClient('localhost', 27017)
      db = client.prova
      col = db.musica

    except Exception as err:
      print(err)

    finally:
      return col







