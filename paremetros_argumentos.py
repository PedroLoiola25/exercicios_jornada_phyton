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

# def registrar_gol (jogador: str, time: str, minuto: int) -> None:
#     print(f"{jogador} marcou para o {time} aos {minuto} minutos.")

# registrar_gol(time="Brasil", minuto=34, jogador="Vini Jr")

# Exercício 5 – Parâmetro com valor padrão

# def criar_partida (time_a: str, time_b: str, estadio="Estádio Nacional") -> None:
#     print(f"A final será entre {time_a} X {time_b} no {estadio}")

# criar_partida ("Flamengo", "Estudiantes")
# criar_partida ("Flamengo", "Estudiantes", "Maracanã")

# Crie uma função chamada registrar_jogador com os seguintes parâmetros:
# def registrar_jogador(nome,
#     posicao="Não informada",
#     titular=False) -> None:
#     print(f"Jogadora: {nome}\nPosição: {posicao}\nÉ titular? {titular}")

# registrar_jogador("Marta",)
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)
# registrar_jogador("Marta", "Atacante", "Sempre ela")

# Exercício 7 – Alterando apenas um valor padrão

# def configurar_camisa(
#         nome: str, 
#         numero: int, 
#         tamanho="M", 
#         cor="amarela") -> None:
#     print (f"Jogadora: {nome}")
#     print (f"Número da camisa: {numero}")
#     print (f"Tamanho da camisa: {tamanho}")
#     print (f"Cor: {cor}")

# configurar_camisa("Marta", 10, cor="azul")

# Exercício 8 – Recebendo vários argumentos com *args

# def listar_jogadores(*jogadores):
#     print(f"{jogadores}")


# listar_jogadores("Marta")
# listar_jogadores("Marta","Vini Jr","Alisson")

# Exercício 9 – Trabalhando com os valores de *args

# def somar_gols(*valores) -> float:
#     return sum(valores)

# total=somar_gols(2, 1, 3, 2)
# print(total)

# Exercício 10 – Parâmetro normal e *args

# def convocar_selecao(pais, *jogadores) -> None:
#     print(f"País: {pais}\nConvocados: {jogadores}")

# convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")

# Exercício 11 – Recebendo argumentos nomeados com **kwargs
