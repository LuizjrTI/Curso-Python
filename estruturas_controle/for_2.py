palavra = 'paralelepípedo'

for letra in palavra:
    #print(letra, end='\n')
    print(letra, end=',')


aprovados = ['Rafaela','Pedro','Renato','Maria']

for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1}) ', nome) 