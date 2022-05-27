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
    print("Seja Bem-Vindo a Batalha Pokémon ")
    linha()
    tempo()
    jogador = str(input("Qual o seu nome jogador? "))
    linha()
    print("Ok!! {}, agora vou te passar as opções que tenho para você enfrentar o Chefão Mewtho. -\/-".format(jogador))
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
    ataque_pikachu = 40
    vida_pikachu = 400
    cura_pikachu = 50
    ataque_mewtho = 60
    vida_mewtho = 500
    while(vida_pikachu > 0 and vida_mewtho > 0):
        print("Você tem {} de vida ".format(vida_pikachu))
        linha()
        tempo()
        escolha_turno = input("O que você quer fazer no seu turno? [ A - Atacar ] [ B - Curar ] => ")
        linha()
        tempo()
        if escolha_turno == "A":
            vida_mewtho = vida_mewtho - ataque_pikachu
            print("Você atacou o Mewtho e causou {} de dano ".format(ataque_pikachu))
            print("Mewtho agora tem {} de vida ".format(vida_mewtho))
            linha()
            tempo()
            limpar()
            print("Agora é o turno do Mewtho -\/- ")
            linha()
            tempo()
            vida_pikachu = vida_pikachu - ataque_mewtho
            print("O Mewtho te atacou!! ******** \nCausou {} de dano ".format(ataque_mewtho))
            tempo()
            limpar()

        elif escolha_turno == "B":
            vida_pikachu = vida_pikachu + cura_pikachu
            print("Você usou a cura :) ")
            linha()
            print("Você tem agora {} de vida ".format(vida_pikachu))
            linha()
            tempo()
            limpar()
            print("Agora é o turno do Mewtho -\/- ")
            linha()
            vida_pikachu = vida_pikachu - ataque_mewtho
            print("O Mewtho te atacou!! ****** ")
            print("Você agora tem {} de vida ".format(vida_pikachu))
            linha()
            tempo()
            limpar()
        else:
            print("Você digitou uma opção errada ")
            print("Agora o Mewtho vai te atacar como punição \nkkkkkkkkkkkkkkk ")
            linha()
            tempo()
            vida_pikachu = vida_pikachu - ataque_mewtho
            print("O mewtho te atacou! -\/- ")
            linha()
            print("Você tem {} de vida ".format(vida_pikachu))
            tempo()
            limpar()
    else:
        print("Fim de Jogo !!!")        

elif escolha_do_pokemon == 2:
    print("Você escolheu o Bulbasaur")
    ataque_bulbasaur = 30
    vida_bulbasaur = 350
    cura_bulbasaur = 60
    ataque_mewtho = 60
    vida_mewtho = 500
    while(vida_bulbasaur > 0 and vida_mewtho > 0):
        print("Você tem {} de vida ".format(vida_bulbasaur))
        linha()
        tempo()
        escolha_turno = input("O que você quer fazer no seu turno? [ A - Atacar ] [ B - Curar ] => ")
        linha()
        tempo()
        if escolha_turno == "A":
            vida_mewtho = vida_mewtho - ataque_bulbasaur
            print("Você atacou o Mewtho e causou {} de dano ".format(ataque_bulbasaur))
            print("Mewtho agora tem {} de vida ".format(vida_mewtho))
            linha()
            tempo()
            limpar()
            print("Agora é o turno do Mewtho -\/- ")
            linha()
            tempo()
            vida_bulbasaur = vida_bulbasaur - ataque_mewtho
            print("O Mewtho te atacou!! ******** \nCausou {} de dano ".format(ataque_mewtho))
            tempo()
            limpar()

        elif escolha_turno == "B":
            vida_bulbasaur = vida_bulbasaur + cura_bulbasaur
            print("Você usou a cura :) ")
            linha()
            print("Você tem agora {} de vida ".format(vida_bulbasaur))
            linha()
            tempo()
            limpar()
            print("Agora é o turno do Mewtho -\/- ")
            linha()
            vida_bulbasaur = vida_bulbasaur - ataque_mewtho
            print("O Mewtho te atacou!! ****** ")
            print("Você agora tem {} de vida ".format(vida_bulbasaur))
            linha()
            tempo()
            limpar()
        else:
            print("Você digitou uma opção errada ")
            print("Agora o Mewtho vai te atacar como punição \nkkkkkkkkkkkkkkk ")
            linha()
            tempo()
            vida_bulbasaur = vida_bulbasaur - ataque_mewtho
            print("O mewtho te atacou! -\/- ")
            linha()
            print("Você tem {} de vida ".format(vida_bulbasaur))
            tempo()
            limpar()
    else:
        print("Fim de Jogo !!!")

elif escolha_do_pokemon == 3:
    print("Você escolheu o Chameleon")
    ataque_charmeleon = 50
    vida_charmeleon = 400
    cura_charmeleon = 40
    ataque_mewtho = 60
    vida_mewtho = 500
    while(vida_charmeleon > 0 and vida_mewtho > 0):
        print("Você tem {} de vida ".format(vida_charmeleon))
        linha()
        tempo()
        escolha_turno = input("O que você quer fazer no seu turno? [ A - Atacar ] [ B - Curar ] => ")
        linha()
        tempo()
        if escolha_turno == "A":
            vida_mewtho = vida_mewtho - ataque_charmeleon
            print("Você atacou o Mewtho e causou {} de dano ".format(ataque_charmeleon))
            print("Mewtho agora tem {} de vida ".format(vida_mewtho))
            linha()
            tempo()
            limpar()
            print("Agora é o turno do Mewtho -\/- ")
            linha()
            tempo()
            vida_charmeleon = vida_charmeleon - ataque_mewtho
            print("O Mewtho te atacou!! ******** \nCausou {} de dano ".format(ataque_mewtho))
            tempo()
            limpar()

        elif escolha_turno == "B":
            vida_charmeleon = vida_charmeleon + cura_charmeleon
            print("Você usou a cura :) ")
            linha()
            print("Você tem agora {} de vida ".format(vida_charmeleon))
            linha()
            tempo()
            limpar()
            print("Agora é o turno do Mewtho -\/- ")
            linha()
            vida_charmeleon = vida_charmeleon - ataque_mewtho
            print("O Mewtho te atacou!! ****** ")
            print("Você agora tem {} de vida ".format(vida_charmeleon))
            linha()
            tempo()
            limpar()
        else:
            print("Você digitou uma opção errada ")
            print("Agora o Mewtho vai te atacar como punição \nkkkkkkkkkkkkkkk ")
            linha()
            tempo()
            vida_charmeleon = vida_charmeleon - ataque_mewtho
            print("O mewtho te atacou! -\/- ")
            linha()
            print("Você tem {} de vida ".format(vida_charmeleon))
            tempo()
            limpar()
    else:
        print("Fim de Jogo !!!")


print("Obrigado por jogar a Batalha Pokémon !! - _ - ")


