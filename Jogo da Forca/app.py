from palavras import palavras
import random

def selecionar_palavra():
    palavra =random.choice(palavras)
    return palavra.upper()

def jogar(palavra):
    palavra_a_completar = "_" * len(palavra)
    adivinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6

    print("Vamos jogar!")
    print(exibir_forca(tentativas))
    print(f"Esta é a palavra: {palavra_a_completar}")

    while not adivinhou and tentativas > 0:

        tentativa = input("Digite uma letra ou a palavra para continuar: ").upper()

        print(tentativa)
        if len(tentativa) == 1 and tentativa.isalpha():
            if tentativa in letras_utilizadas:
                print(f"Você já utilizou esta letra antes: {tentativa}")
            elif tentativa not in palavra:
                print(f"A letra {tentativa} não está na palavra")
                tentativas -= 1
                letras_utilizadas.append(tentativa)
            else:
                print(f"Você acertou! A letra {tentativa} está na palavra.")
                letras_utilizadas.append(tentativa)
                palavra_lista = list(palavra_a_completar)

                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for indice in indices:
                    palavra_lista[indice] = tentativa
                palavra_a_completar = "".join(palavra_lista)
                if "_" not in palavra_a_completar:
                    adivinhou = True
        elif len(tentativa) == len(palavra) and tentativa.isalpha():
            if tentativa in palavras_utilizadas:
                print(f"Você já utilizou esta palavra {tentativa}")
            elif tentativa != palavra:
                print(f"A palavra {tentativa} esta incorreta!")
                tentativas -= 1
                palavras_utilizadas.append(tentativa)
            else:
                adivinhou = True
                palavra_a_completar = palavra

        else:
            print("Tentativa inválida, tente novamente!")

        print(exibir_forca(tentativas))
        print(palavra_a_completar)

    if adivinhou:
        print("Parabéns! Você acertou a palavra")
    else:
        print(f"Acabaram as tentativas, a palavra era: {palavra}")




def exibir_forca(tentativas):
  estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

  return estagios[tentativas]

def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)

    while input("Jogar novamente? (S/N) ").upper() == 'S':
        palavra = selecionar_palavra()
        jogar(palavra)

iniciar()