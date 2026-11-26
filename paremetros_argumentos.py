# Exercício 1 – Argumentos posicionais
# def apresentar_jogador (nome: str, posicao: str) -> None:
#     print(f"Jogador: {nome} | Posição: {posicao}")

# apresentar_jogador("Marta", "Atacante")

# Exercício 2 – A ordem dos argumentos
# def mostrar_partida( mandante:str, visitante:str) -> None:
#     print(f"{mandante} X {visitante}")

# mostrar_partida("Brasil", "Argentina")
# mostrar_partida("Argentina", "Brasil")

# Exercício 3 – Argumentos nomeados

# def cadastrar_jogador (nome: str, idade: int, posicao: str) -> None:
#     print(f"Jogador: {nome}\nIdade: {idade}\nPosição: {posicao}")

# cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)

# Exercício 4 – Posicionais e nomeados juntos

def registrar_gol (jogador: str, time: str, minuto: int) -> None:
    print(f"{jogador} marcou para o {time} aos {minuto} minutos.")

registrar_gol(time="Brasil", minuto=34, jogador="Vini Jr")
# Na chamada da função:

# Passe jogador por posição.
# Passe time por posição.
# Passe minuto pelo nome.