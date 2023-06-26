# Necessário a biblioteca pygame, instal: pip install pygame

from pygame import mixer, init, event
init()
mixer.music.load('SoundTTPN.mp3')
mixer.music.play()

print(
    f"""
    {20*'='} OLA!!! SEJA MUITO BEM VINDO AO TOPA TUDO POR NADA!!! {20*'='}
    {11*' '}Antes de darmos inicio eu preciso de algumas informações sobre você!!!
    """
)

print(f"""
     {32*'*'} Precione ENTER para começar {35*'*'}
"""
)

input(event.wait())



Name = input('Digete seu nome completo: ')
Name_s = Name.split()
age = int(input('Digite sua didade: '))

print(
    f"""
Beleza, {Name_s[0]} {Name_s[-1]}!!! VAMOS COMEÇAR!!
    """
)
print(F"{30*'='} OBRIGADO POR JOGAR! ATÉ A PRÓXIMA!! {30*'='}")
input(
    F"""
  


    {28*'='} PRECIONE ENTER PARA FINALIZAR {28*'='}
    """
)
event.wait()