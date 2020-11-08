import psycopg2
from connection import Connection

class Operations():

    def save(self, nome, autor, genero):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = f"insert into musica (nome, autor, genero) values ('{nome}', '{autor}', '{genero}');"
            cursor.execute(insert)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


    def search(self):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = "select * from musica"
            cursor.execute(select)
            musicas = cursor.fetchall()

            for row in musicas:
                print(f"Id = {row[0]}")
                print(f"nome = {row[1]}")
                print(f"autor = {row[2]}")
                print(f"genero =  {row[3]} \n")

        except (Exception, psycopg2.Error) as error:
            print("Error", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()