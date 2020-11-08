from operation import Operations

op = Operations()

while True:
    print('-------------------')
    print('''[1]:Cadastrar
[2]:Editar
[3]:Remover
[4]:Consultar
[5]:Sair
''')
    print('-------------------')

    option = input(str('Escolha uma opção: '))

    if option == '1':
        print('---CADASTRO---')
        nome = cpf = email = ''
        while True:
            nome = str(input('nome: '))
            isValidName = op.validateName(nome)
            if isValidName:
                break
            print('Inválido, tente novamente!')

        while True:
            # Verificar letra dentro do cpf
            print('FORMATO: 000.000.000.00')
            cpf = str(input('cpf: '))
            isValidCpf = op.validateCpf(cpf)
            if isValidCpf:
                break
            print('Inválido, tente novamente!')

        while True:
            email = str(input('email: '))
            isValidEmail = op.validateEmail(email)
            if isValidEmail:
                break
            print('Inválido, tente novamente!')

        op.save(nome, cpf, email)

    if option == '2':
        print('---EDIÇÂO---')
        while True:
            print('FORMATO: 000.000.000.00')
            cpf = str(input('Pesquise um cpf para fazer a edição: '))
            haveCpf = op.searchByCpf(cpf)
            if haveCpf:
                nome = str(input('Novo nome: '))
                while True:
                    email = str(input('Novo email: '))
                    isValidEmail = op.validateEmail(email)
                    if isValidEmail:
                        break
                    print('Inválido, tente novamente!')
                op.update(nome, cpf, email)
                break
            print('Inválido, tente novamente!')



    if option == '3':
        print('---REMOÇÂO---')
        while True:
            print('FORMATO: 000.000.000.00')
            cpf = str(input('Digite um cpf para deleção: '))
            haveCpf = op.searchByCpf(cpf)
            if len(haveCpf):
                op.remove(cpf)
                print('Deleção realizada!')
                break
            print('Inválido, tente novamente!')

    if option == '4':
        print('---CONSULTAR POR---')
        print('''[1]:CPF
[2]:E-MAIL
-------------------
        ''')
        consulta = input(str('Digite o filtro de consulta: '))
        if consulta == '1':
            cpf = input(str('Pesquise pelo cpf: '))
            op.search('cpf', cpf)
        if consulta == '2':
            email = input(str('Pesquise pelo e-mail: '))
            op.search('email', email)

    if option == '5':
        print('---SAIR---')
        break

