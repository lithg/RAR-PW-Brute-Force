#coding: utf-8

import rarfile
from colorama import Fore, Back, Style
from datetime import datetime, timedelta
import time
from itertools import chain, product, combinations_with_replacement

wordlist_txt = 'pt_br_wordlist.txt'

def dict():
    global tempo
    passwd_testados = 0
    encontrou = False

    if rarfile.is_rarfile('rarf.rar'):
        with rarfile.RarFile('rarf.rar') as rf:
            wordlist = open(wordlist_txt, 'r')
            start = time.time()         # inicia contador de duracao
            for senha in wordlist:

                try:
                    rf.extractall(path='.', members=rf.namelist(), pwd=senha.strip())

                except:
                    print(Fore.RED + '[+] Testando: ' + senha.strip())

                else:
                    print(Fore.RED + '[+] Testando: ' + senha + '\n')
                    print(Fore.GREEN + '[*] SENHA ENCONTRADA: {}'.format(senha))
                    print(Fore.GREEN + '[*] TENTATIVAS: ' + str(passwd_testados))
                    end = time.time()  # finaliza contador
                    tempo = end - start
                    duracao()
                    encontrou = True
                    break

                passwd_testados += 1

            if not encontrou:
                print(Fore.LIGHTRED_EX + '[*] SENHA NÃO ENCONTRADA')

            else:

                for f in rf.infolist():
                    print(Fore.LIGHTBLUE_EX + 'Arquivo: ' + f.filename)
                    print(Fore.LIGHTBLUE_EX + 'Tamanho: ' + str(f.file_size) + ' KB\n')

    else:
        print('Arquivo inválido')

def gerador(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


def bruteforce():

    lista = list(gerador('0123456789', 4))
    global tempo
    passwd_testados = 0
    encontrou = False

    if rarfile.is_rarfile('rarf.rar'):
        with rarfile.RarFile('rarf.rar') as rf:
            start = time.time()         # inicia contador de duracao
            for senha in lista:
                senha = ''.join(senha)

                try:
                    rf.extractall(path='.', members=rf.namelist(), pwd=senha)

                except:
                    print(Fore.RED + '[+] Testando: ' + senha)

                else:
                    print(Fore.RED + '[+] Testando: ' + senha + '\n')
                    print(Fore.GREEN + '[*] SENHA ENCONTRADA: {}'.format(senha))
                    print(Fore.GREEN + '[*] TENTATIVAS: ' + str(passwd_testados))
                    end = time.time()  # finaliza contador
                    tempo = end - start
                    duracao()
                    encontrou = True
                    break

                passwd_testados += 1

            if not encontrou:
                print(Fore.LIGHTRED_EX + '[*] SENHA NÃO ENCONTRADA')

            else:

                for f in rf.infolist():
                    print(Fore.LIGHTBLUE_EX + 'Arquivo: ' + f.filename)
                    print(Fore.LIGHTBLUE_EX + 'Tamanho: ' + str(f.file_size) + ' KB\n')


def duracao():
    sec = timedelta(seconds=tempo)
    d = datetime(1,1,1) + sec

    print("Duração: %dd:%dh:%dm:%ds" % (d.day-1, d.hour, d.minute, d.second))
    print()




if __name__ == '__main__':
    bruteforce()
