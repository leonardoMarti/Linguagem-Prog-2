import psycopg2
from email_validator import validate_email, EmailNotValidError
from connection import Connection

class Operations():

    def validateName(self, nome):
        validName = True

        if len(nome) == 0 or len(nome) > 150:
            validName = False

        return validName

    def validateCpf(self, cpf):
        validCpf = True

        if len(cpf) == 0 or len(cpf) != 14:
            validCpf = False
        else:
            duplicateCpf = self.searchByCpf(cpf)
            if len(duplicateCpf) == 1:
                validCpf = False

        return validCpf

    def validateEmail(self, email):
        validEmail = True

        if len(email) > 400:
            validEmail = False

        try:
            valid = validate_email(email)
            valid.email

        except EmailNotValidError as e:
            validEmail = False

        return validEmail

    def save(self, nome, cpf, email):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = f"insert into pessoa (nome, cpf, email, isdelete) values ('{nome}', '{cpf}', '{email}', 'false');"
            cursor.execute(insert)
            connection.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def search(self, where, param):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT nome, cpf, email FROM pessoa WHERE {where}='{param}' AND isdelete='false'"
            cursor.execute(select)
            pessoa = cursor.fetchall()

            if len(pessoa):
                for row in pessoa:
                    print(f'Nome = {row[0]}')
                    print(f'CPF = {row[1]}')
                    print(f'E-mail = {row[2]}')
                    print('-------------------')
            else:
                print('Nenhum registro foi encontrado!')

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def searchByCpf(self, cpf):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT cpf FROM public.pessoa WHERE cpf='{cpf}'"
            cursor.execute(select)
            data = cursor.fetchall()
            return data

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def update(self, nome, cpf, email):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE pessoa SET nome='{nome}', email='{email}' WHERE cpf='{cpf}'"
            cursor.execute(update)
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def remove(self, cpf):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE pessoa SET isdelete='true' WHERE cpf='{cpf}'"
            cursor.execute(update)
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

