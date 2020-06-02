from random import randint
import pickle

def linha():
    print('='*30)

def lancardado(d):
    dado=0
    for i in range(d):
        dado += randint(1,6)
    return dado

# definir o jogo a abrir
nfic='teste.pkl'
linha()
print('ler ficheiro')
with open(nfic,'rb') as f:
    valor=pickle.load(f)

print(f'Os teus valores para combate sao:')
print(f'Habilidade: {valor["hm"][1]}')
print(f'Energia: {valor["em"][1]}')

ih=int(input('Habilidade do inimigo:'))
ie=int(input('Energia do inimigo:'))

mh=valor['hm'][1]
me=valor['em'][1]
print(mh)
print(me)
while me > 0 and ie > 0:
    fai=lancardado(2)+ih
    fam=lancardado(2)+mh
    if fai>fam:
        me-=2
        print('Perdes-te')
    if fai<fam:
        ie-=2
        print('Galhas-te')
    if fai==fam:
        print('Empate')


    