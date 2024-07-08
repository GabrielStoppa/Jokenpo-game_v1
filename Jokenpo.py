import random

print("Bem-vindo ao Jogo de Jokenpô!")
print("\n1 - Pedra\n2 - Papel\n3 - Tesoura")

# Usando uma lista para determinar as opções
jokenpo = ["Pedra", "Papel", "Tesoura"]
player = input("\nQual o seu nome? ")

# Inicializando os pontos
player_points = 0
computer_points = 0

# Loop até que alguém alcance 3 pontos
while player_points < 3 and computer_points < 3:
    user_choice = int(input("\nFaça a sua escolha (Apenas o Número): ")) - 1

    # Verifica se a escolha do usuário é válida
    if user_choice not in [0, 1, 2]:
        print("\nO jogador selecionou uma opção que não existe")
        continue

    computer_choice = random.choice(jokenpo)

    print(f"\n{player} : {jokenpo[user_choice]} VS Computador : {computer_choice}")

    if computer_choice == jokenpo[user_choice]:
        print("---------- O jogo deu Empate! ----------")
    elif (user_choice == 0 and computer_choice == "Tesoura") or \
        (user_choice == 1 and computer_choice == "Pedra") or \
        (user_choice == 2 and computer_choice == "Papel"):
        print("---------- O Jogador ganhou! ----------")
        player_points += 1
    else:
        print("---------- O Computador ganhou! ----------")
        computer_points += 1

    # Exibe a pontuação atual
    print(f"\nPontuação: {player} {player_points} - {computer_points} Computador")

# Verifica quem alcançou 3 pontos primeiro
if player_points == 3:
    print(f"\nParabéns, {player}! Você venceu o jogo!")
else:
    print("\nO Computador venceu o jogo! Tente novamente.")

print("\nObriagdo por jogar....Desligando")