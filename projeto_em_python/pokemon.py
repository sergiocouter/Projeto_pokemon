# Desafio Pokemon
# Criar um algoritmo que simule uma batalha entre dois pokemons
# O usuário deverá escolher entre 3 opções de personagem e enfrentar o Pokemom Boss
# Em cada rodada o usuário pode se curar ou atacar
# Boss só ataca no turno dele
# A batalha só acaba quando um dos pokemons morre

import time
import os


def linha():
    print("---------------------------------")


def limpar():
    os.system('cls') or None


def tempo():
    time.sleep(7)


def inicio_do_jogo():
    linha()
    print("Seja Bem-Vindo a batalha Pokémon")
    linha()
    tempo()
    jogador = str(input("Qual o seu nome jogador? "))
    linha()
    print("Ok!! {}, agora vou te passar as opções que tenho para você enfrentar o Mewtho".format(jogador))
    tempo()
    limpar()


inicio_do_jogo()


def pikachu(ataque_pikachu, vida_pikachu, cura_pikachu):
    ataque = ataque_pikachu
    vida = vida_pikachu
    cura = cura_pikachu
    print("PIKACHU")
    print("O ataque do Pikachu é: {} \nA vida do Pikachu é: {} \nA cura do Pikachu é: {}".format(
        ataque, vida, cura))
    linha()


pikachu(40, 400, 50)
tempo()


def bulbasaur(ataque_bulbasaur, vida_bulbasaur, cura_bulbasaur):
    ataque = ataque_bulbasaur
    vida = vida_bulbasaur
    cura = cura_bulbasaur
    print("BULBASAUR")
    print("O ataque do Bulbasaur é: {} \nA vida do Bulbasaur é: {} \nA cura do Bulbasaur é: {}".format(
        ataque, vida, cura))
    linha()


bulbasaur(30, 350, 60)
tempo()


def charmeleon(ataque_charmeleon, vida_charmeleon, cura_charmeleon):
    ataque = ataque_charmeleon
    vida = vida_charmeleon
    cura = cura_charmeleon
    print("CHARMELEON")
    print("O ataque do Charmeleon é: {} \nA vida do Charmeleon é: {} \nA cura do Charmeleon é: {}".format(
        ataque, vida, cura))
    linha()


charmeleon(50, 400, 40)
tempo()
limpar()

escolha_do_pokemon = int(input(
    "Informe o número do Pokémon escolhido? [ 1 - Pikachu] , [ 2 - Bulbasaur] , [ 3 - Charmeleon] => "))

if escolha_do_pokemon == 1:
    print("Você escolheu o Pikachu")
    pikachu(40, 400, 50)
elif escolha_do_pokemon == 2:
    print("Você escolheu o Bulbasaur")
    bulbasaur(30, 350, 60)
elif escolha_do_pokemon == 3:
    print("Você escolheu o Chameleon")
    charmeleon(50, 400, 40)
else:
    print(
        "Você digitou um valor incorreto. Por favor digite uma das opções [1] , [2] ou [3]")


