import mysql.connector
from datetime import datetime

#Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='transportadora'
)

#CORES:
vm = '\033[1:31m'
vd = '\033[1;32m'
am = '\033[1;33m'
az = '\033[1;34m'
mg = '\033[1;35m'
cy = '\033[1;36m'
cz_cl =	'\033[1;37m'
Cz_es =	'\033[1;90m'
vm_cl =	'\033[1;91m'
vd_cl =	'\033[1;92m'
am_cl =	'\033[1;93m'
az_cl =	'\033[1;94m'
mg_cl =	'\033[1;95m'
cy_cl =	'\033[1;96m'
br = '\033[1;97m'
fc = '\033[m'


def decorar():
    print(f'{vd_cl}={fc}'*98)
def divisor():
    print(f'{vd_cl}-{fc}'*98)
def pularL():
    print('\n')


decorar()
print(' '*33,f'{br}SISTEMA PORTARIA TRANSPORTADORA{fc}')
decorar()

try:
    while True:
        pularL()
        divisor()
        opcao = int(input(f"""
{br}SELECIONE UMA OPCÃO:{fc}
    
{am}(1){fc} - {br}CADASTRO DE MOTORISTA{fc}
{am}(2){fc} - {br}CADASTRO DE TERCEIROS{fc}
{am}(3){fc} - {br}CONSULTA DE FROTA{fc}
{am}(4){fc} - {br}CONSULTA DE TERCEIROS{fc}
{am}(5){fc} - {br}SAIR{fc}
    
{br}O QUE DESEJA FAZER:{fc} """))
        if opcao == 1:
            pularL()
            divisor()
            id = int()
            motorista = str(input(f'{br}INFORME O NOME DO MOTORISTA{fc}: ').upper().lstrip())
            divisor()
            placa = str(input(f'{br}INFORME A PLACA DO VEÍCULO{fc}: ').upper().lstrip())
            divisor()
            km = int(input(f'{br}INFORME A QUILOMETRAGEM{fc}: ').upper().lstrip())
            divisor()
            controle = int(input(f'{br}DIGITE {am}(1){fc} {br}PARA{fc} {vd}ENTRADA{fc} {br}OU{fc} {am}(2){fc} {br}PARA{fc} {vd}SAÍDA:{fc} ').upper().lstrip())
            if controle == 1:
                controle = 'ENTRADA'
            elif controle == 2:
                controle = 'SAíDA'
            else:
                print(f'{vm}ERRO! Opção inválida.{fc}')
            divisor()
            observacao = int(input(f'{br}ALGUMA OBSERVAÇÃO? {fc}{am}(1-SIM/2-NÃO){fc}: ').upper().lstrip())
            if observacao == 1:
                observacaoNovo = str(input(f'{br}DIGITE A OBSERVAÇÃO:{fc} ').upper().lstrip())
            else:
                observacaoNovo = str('')
            data_atual = datetime.now()
            formatar = data_atual.strftime('%d/%m/%Y %H:%M')
            pularL()
            divisor()
            print(f'''{am}Informações do cadastro:{fc}
            {br}Nome do Motorista:{fc} {cy_cl}{motorista}{fc}
            {br}Placa do Veículo:{fc} {cy_cl}{placa}{fc}
            {br}Quilometragem:{fc} {cy_cl}{km}{fc}
            {br}Controle:{fc} {cy_cl}{controle}{fc}
            {br}Observação:{fc} {cy_cl}{observacaoNovo}{fc}
            {br}Data:{fc} {cy_cl}{formatar}{fc}''')
            pularL()
            confirmacao = int(input(f'{br}CONFIRMAR CADASTRO {am}(1)SIM{fc} e {am}(2)NÃO{fc}:'))
            pularL()
            if confirmacao == 1:
                comando = '''INSERT INTO FROTA (ID_FROTA, MOTORISTA, PLACA, KM, CONTROLE, 
                OBSERVACAO, DATA) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
                cursor = conexao.cursor()
                dados = (id,motorista,placa,km,controle,observacaoNovo,data_atual)
                cursor.execute(comando,dados)
                conexao.commit()
                divisor()
                print(f'{vd}DADOS CADASTRADOS COM SUCESSO.{fc}')
                divisor()
            else:
                divisor()
                print(f'{vm}ERRO AO EFETUAR O CADASTRO.{fc}')
                divisor()
        elif opcao == 2:
            pularL()
            divisor()
            id = int()
            nome = str(input(f'{br}INFORME O NOME{fc}: ').upper().lstrip())
            documento = int(input(f'{br}INFORME O DOCUMENTO: {fc}'))
            finalidade = int(input(f'{br}DIGITE{fc} {am}(1)ENVIO (2)RETIRADA (3)OUTROS{fc}:'))
            if finalidade == 1:
                finalidadeN = 'ENVIO'
            elif finalidade == 2:
                finalidadeN = 'RETIRADA'
            elif finalidade == 3:
                finalidadeN = 'OUTROS'
            else:
                print(f'{vm}OPÇÃO INVÁLIDA{fc}')
            observacao = int(input(f'{br}Alguma observação{fc}{am}(1-SIM/2-NÃO){fc}:').upper().lstrip())
            if observacao == 1:
                observacaoNovo = str(input('').upper().lstrip())
            else:
                observacaoNovo = str('')
            controle = int(input(f'{br}DIGITE {am}(1){fc} {br}PARA{fc} {vd}ENTRADA{fc} {br}OU{fc} {am}(2){fc} {br}PARA{fc} {vd}SAÍDA:{fc}').upper().lstrip())
            if controle == 1:
                controleN = 'ENTRADA'
            elif controle == 2:
                controleN = 'SAíDA'
            else:
                print(f'{vm}ERRO! Opção inválida.{fc}')
            responsavel = str(input(f'{br}INFORME O RESPONSÁVEL:{fc} ').upper().lstrip())
            data_atual = datetime.now()
            formatar = data_atual.strftime('%d/%m/%Y %H:%M')
            pularL()
            divisor()
            print(f'''{am}Informações do cadastro:{fc}
            {br}Nome:{fc} {cy_cl}{nome}{fc}
            {br}Documento:{fc} {cy_cl}{documento}{fc}
            {br}Finalidade:{fc} {cy_cl}{finalidadeN}{fc}
            {br}Observação:{fc} {cy_cl}{observacaoNovo}{fc}
            {br}Controle:{fc} {cy_cl}{controleN}{fc}
            {br}Responsável{fc} {cy_cl}{responsavel}{fc}
            {br}Data:{fc} {cy_cl}{formatar}{fc}''')
            pularL()
            confirmacao = int(input(f'{br}CONFIRMAR CADASTRO {am}(1)SIM{fc} e {am}(2)NÃO{fc}:'))
            pularL()
            if confirmacao == 1:
                comando = '''INSERT INTO TERCEIROS (ID_TERCEIROS, NOME, DOCUMENTO, FINALIDADE, OBSERVACAO, 
                CONTROLE, RESPONSAVEL, DATA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
                cursor = conexao.cursor()
                dados = (id,nome,documento,finalidadeN,observacaoNovo,controle,responsavel,data_atual)
                cursor.execute(comando,dados)
                conexao.commit()
                divisor()
                print(f'{vd}DADOS CADASTRADOS COM SUCESSO.{fc}')
                divisor()
            else:
                divisor()
                print(f'{vm}ERRO AO EFETUAR O CADASTRO.{fc}')
                divisor()
        elif opcao == 3:
            pularL()
            divisor()
            cursor = conexao.cursor()
            comando_sql='SELECT * FROM FROTA'
            cursor.execute(comando_sql)
            valor = cursor.fetchall()
            print(f'{am}TABELA FROTA{fc}')
            divisor()
            for i in valor:
                print(f'{br}')
                print(i)
        elif opcao == 4:
            pularL()
            divisor()
            cursor = conexao.cursor()
            comando_sql='SELECT * FROM TERCEIROS'
            cursor.execute(comando_sql)
            valor = cursor.fetchall()
            print(f'{am}TABELA TERCEIROS{fc}')
            divisor
            for i in valor:
                print(f'{br}')
                print(i)
        elif opcao == 5:
            pularL()
            divisor()
            print(f'{vm}SESSÃO ENCERRADA.{fc}')
            divisor()
            break
        else:
            pularL()
            divisor()
            print(f'{vm}OPÇÃO INVÁLIDA.{fc}')
            divisor()
except:
    pularL()
    divisor()
    print(f'{vm}DADO INVÁLIDO.{fc}')
    divisor()

