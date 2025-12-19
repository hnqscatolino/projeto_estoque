# ============================
# "BANCO DE DADOS" (DICIONÁRIO)
# ============================
# Aqui ficam os produtos cadastrados.
# A CHAVE é o código (1, 2, 3...)
# O VALOR é outro dicionário com: Produto, Preço, Quantidade

sistema = {
    1: {"Produto": "Mouse", "Preço": 100.00, "Quantidade": 10},
    2: {"Produto": "Teclado", "Preço": 80.00, "Quantidade": 15},
    3: {"Produto": 'Monitor 24"', "Preço": 750.00, "Quantidade": 8},
    4: {"Produto": "Headset Gamer", "Preço": 199.90, "Quantidade": 12},
    5: {"Produto": "Mousepad Grande", "Preço": 45.00, "Quantidade": 25},
    6: {"Produto": "Cabo HDMI", "Preço": 29.90, "Quantidade": 30},
    7: {"Produto": "Webcam Full HD", "Preço": 150.00, "Quantidade": 7},
    8: {"Produto": "SSD 480GB", "Preço": 220.00, "Quantidade": 14},
    9: {"Produto": "HD 1TB", "Preço": 260.00, "Quantidade": 9},
    10: {"Produto": "Placa de Vídeo GTX 1650", "Preço": 1200.00, "Quantidade": 3},
    11: {"Produto": "Fonte 500W", "Preço": 180.00, "Quantidade": 11},
    12: {"Produto": "Gabinete Gamer", "Preço": 210.00, "Quantidade": 6},
    13: {"Produto": "Roteador Wi-Fi", "Preço": 130.00, "Quantidade": 20},
    14: {"Produto": "Teclado Mecânico", "Preço": 350.00, "Quantidade": 5},
    15: {"Produto": "Cadeira Gamer", "Preço": 890.00, "Quantidade": 2}
}


# ============================
# LOOP PRINCIPAL (MENU INFINITO)
# ============================
# O programa fica repetindo até o usuário escolher sair (opção 5)

while True:

    # ----------------------------
    # ENTRADA DO USUÁRIO (MENU)
    # ----------------------------
    opçao = int(input(
        "O que deseja fazer: \n"
        " 1 - adicionar produto \n"
        " 2 - consultar produto \n"
        " 3 - vender produto \n"
        " 4 - Relatório total \n"
        " 5 - sair\n"
        " : "
    ))


    # ============================
    # OPÇÃO 1: ADICIONAR PRODUTO
    # ============================
    if opçao == 1:

        # ---------
        # INPUTS
        # ---------
        novo_produto = input("Qual produto você quer adicionar: ")
        preço_np = float(input("Qual o preço desse produto: "))
        quantidade_np = int(input("Qual a quantidade desse produto: "))

        # -------------------------
        # LÓGICA: adicionar no dict
        # -------------------------
        sistema[len(sistema) + 1] = {
            "Produto": novo_produto,
            "Preço": preço_np,
            "Quantidade": quantidade_np
        }

        # -----------
        # SAÍDAS
        # -----------
        print(sistema[len(sistema)])
        print(f"O produto {novo_produto} foi adicionado")

        # -------------------------
        # PERGUNTA SE VAI SAIR
        # -------------------------
        op2 = input("Gostaria de continuar ou sair? (C/S): ")
        if op2.upper() == "S":
            print("Obrigado, volte sempre")
            break


    # ============================
    # OPÇÃO 2: CONSULTAR PRODUTO
    # ============================
    elif opçao == 2:

        # ---------
        # INPUT
        # ---------
        # Como a chave do dicionário é um CÓDIGO (número),
        # faz sentido consultar usando o código do produto.
        codigo = int(input("Qual produto deseja consultar? (use o código): "))

        # -------------------------
        # LÓGICA: consultar no dict
        # -------------------------
        if codigo in sistema:
            print(sistema[codigo])
        else:
            print("Produto não encontrado.")

        # -------------------------
        # PERGUNTA SE VAI SAIR
        # -------------------------
        op2 = input("Gostaria de continuar ou sair? (C/S): ")
        if op2.upper() == "S":
            print("Obrigado, volte sempre")
            break


    # ============================
    # OPÇÃO 3: VENDER PRODUTO
    # ============================
    elif opçao == 3:

        # ---------
        # INPUTS
        # ---------
        produto_vendido = int(input("Qual produto você quer vender? (use o código do produto): \n"))
        quantidade_vendida = int(input("Quantos produtos vão ser vendidos?: \n"))

        # -------------------------
        # VALIDAÇÃO: existe no sistema?
        # -------------------------
        if produto_vendido not in sistema:
            print("Código inválido.\n")
        else:
            # -------------------------
            # VALIDAÇÃO: tem estoque?
            # -------------------------
            if quantidade_vendida > sistema[produto_vendido]["Quantidade"]:
                print("Estoque insuficiente\n")
            else:
                # -------------------------
                # LÓGICA: diminuir estoque
                # -------------------------
                nova_quantidade = sistema[produto_vendido]["Quantidade"] - quantidade_vendida
                sistema[produto_vendido]["Quantidade"] = nova_quantidade

                # -----------
                # SAÍDAS
                # -----------
                print(f"Foram vendidos {quantidade_vendida} {sistema[produto_vendido]['Produto']} \n")
                print(sistema[produto_vendido])

        # -------------------------
        # PERGUNTA SE VAI SAIR
        # -------------------------
        op2 = input("Gostaria de continuar ou sair? (C/S): ")
        if op2.upper() == "S":
            print("Obrigado, volte sempre")
            break


    # ============================
    # OPÇÃO 4: RELATÓRIO TOTAL
    # ============================
    elif opçao == 4:

        # -----------------------------------
        # LÓGICA DO RELATÓRIO (DICIONÁRIO)
        # total = soma de (Quantidade * Preço)
        #
        # ✅ CORRIGIDO: agora percorre o dicionário de verdade
        # sem usar range(len()) e sem contador manual
        # -----------------------------------
        relatorio2 = 0

        for codigo, info in sistema.items():
            quantidade_total = info["Quantidade"]
            preço_produto = info["Preço"]
            relatorio2 += quantidade_total * preço_produto

        # -----------
        # SAÍDA
        # -----------
        print(f"O total investido foi de R$ {relatorio2}")

        # -------------------------
        # PERGUNTA SE VAI SAIR
        # -------------------------
        op2 = input("Gostaria de continuar ou sair? (C/S): ")
        if op2.upper() == "S":
            print("Obrigado, volte sempre")
            break


    # ============================
    # OPÇÃO 5: SAIR
    # ============================
    elif opçao == 5:
        print("Obrigado, volte sempre")
        break


    # ============================
    # OPÇÃO INVÁLIDA
    # ============================
    else:
        print("Opção inválida, tente novamente.\n")
