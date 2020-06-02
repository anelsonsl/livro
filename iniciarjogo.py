from random import randint

def linha():
    print('='*30)

def lancardado(d):
    dado=0
    for i in range(d):
        dado += randint(1,6)
    return dado

def magia_mostra():
    op=0
    linha()
    print('Lista dos feiticos:')
    for i in valor['magia']:
        op+=1
        print(f'{op} - {i[0]} ({i[1]})')
    
def escolher_feiticos():
    
    ainda=valor['mm'][1]
    for i in range(ainda):
        linha()
        print(f'Voce pode escolher {valor["mm"][1]} feiticos')
        magia_mostra()
        acres_magia=int(input('A sua opcao:'))
        valor['mm'][1]-=1
        valor['magia'][acres_magia-1][1]+=1
    print('Boa Sorte com as suas Opcoes')



valor={
    'hm':[0,0], #Minha Habilidae
    'em':[0,0], #Minha Energia
    'sm':[0,0], #Minha Sorte
    'mm':[0,0], #Minha Magia
    'ouro':0,   #Meu Ouro
    'magia':[['Copia de criatura',0],
            ['Percepcao extra sensorial',0],
            ['Fogo',0],
            ['Ouro dos Tolos',0],
            ['Ilusao',0],
            ['Levitacao',0],
            ['Sorte',0],
            ['Escudo',0],
            ['Habilidade',0],
            ['Energia',0],
            ['Forca',0],
            ['Fraquesa',0]
            ], #Meus feiticos existe 12  e depois quantos tenho de cada um
    'equipamneto':['espada','armadura de couro','lanterna','Mochila']#Meus material tipo texto
    }

linha()

continuar='s'

while continuar=='s':

    valor['hm'][0]=lancardado(1)+6
    valor['em'][0]=lancardado(2)+12
    valor['sm'][0]=lancardado(1)+6
    valor['mm'][0]=lancardado(2)+6
    print(f'Valor de Habilidae: {valor["hm"][0]} max 18') # nota hm com chaves duplas por causa da funcaO F UTILIZA chaves simplesc
    print(f'Valor de Energia: {valor["em"][0]} max 24')
    print(f'Valor de Sorte: {valor["sm"][0]} max 12')
    print(f'Valor de Magia: {valor["mm"][0]} max 18')
    continuar = input('Novos Valores? (s/n/c):')
if continuar=='c':
    valor['hm'][0]=18
    valor['em'][0]=24
    valor['sm'][0]=12
    valor['mm'][0]=18

valor['hm'][1]=valor['hm'][0]
valor['em'][1]=valor['em'][0]
valor['sm'][1]=valor['sm'][0]
valor['mm'][1]=valor['mm'][0]

linha()
print('Os seus Valores Iniciais:')
print(f'Valor de Habilidae: {valor["hm"][0]} max 18') # nota hm com chaves duplas por causa da funcaO F UTILIZA chaves simplesc
print(f'Valor de Energia: {valor["em"][0]} max 24')
print(f'Valor de Sorte: {valor["sm"][0]} max 12')
print(f'Valor de Magia: {valor["mm"][0]} max 18')

linha()
#Escolher os feiticos
escolher_feiticos()

#Agora gravar em ficheiro
