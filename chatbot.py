print("E aí, mano! Bem-vindo ao Bot da Quebrada")
print("Tô aqui pra te dar o papo reto sobre currículo, bolsas e tech. Bora nessa?")

while True:
    print("\nTu quer ajuda com:")
    print("1 - Montar um currículo")
    print("2 - Achar bolsa de estudo")
    print("3 - Entrar na área de tecnologia")
    print("0 - Sair do Bot")

    opcao = int(input("Escolhe aí: "))

    if opcao == 1:
        print("\nMassa demais! Bora montar teu currículo")

        nome = input("Qual é teu nome completo, fera? ")
        objetivo = input("Qual é teu corre, ou seja, que tipo de trampo tu tá procurando? ")
        experiencia = input("Já tem alguma experiência ou curso na área? Se sim, manda aí: ")

        print("\nShow! Agora segura tua prévia do currículo base:\n")
        print("========== CURRÍCULO BASE ==========")
        print(f"Nome: {nome}")
        print(f"Objetivo: {objetivo}")
        print(f"Experiência/Curso: {experiencia}")
        print("====================================")

        continuar = input("\nQuer colocar mais informações no currículo? (s/n): ").lower()
        if continuar == "s":
            complemento = input("Manda aí mais um detalhe que tu acha massa colocar, tipo como tu trabalha em grupo, ou quais são tuas especialidades: ")
            print("\nAtualizado! Olha como ficou agora:\n")
            print("========== CURRÍCULO COMPLETO ==========")
            print(f"Nome: {nome}")
            print(f"Objetivo: {objetivo}")
            print(f"Experiência/Curso: {experiencia}")
            print(f"Extra: {complemento}")
            print("========================================")
        else:
            print("\nSuave, currículo prontinho! Agora é só mandar nos corres")

    elif opcao == 2:
        print("\nBeleza! Bora ver se tu se encaixa em alguma bolsa")
        renda = float(input("Me diz tua renda familiar por mês (em R$): "))
        idade = int(input("E quantos anos tu tem? "))

        if renda <= 2000 and idade <= 29:
            print("\nEita! Tu tem chance boa, viu? Dá uma olhada em:")
            print("- PE no Campus")
            print("https://www3.educacao.pe.gov.br/ppc/")
            print("- Educa Mais Brasil")
            print("https://www.educamaisbrasil.com.br/")
            print("- Quero Bolsa")
            print("https://querobolsa.com.br/")
        else:
            print("\nTalvez não role bolsa social, mas ainda tem opção! Tenta:")
            print("- Bolsas por mérito")
            print("- Cursos em empresas como Alura, Recode, Proa, etc.")
            print("https://www.alura.com.br/")
            print("https://recode.org.br/")
            print("https://www.proa.org.br/")

    elif opcao == 3:
        print("\nBora mergulhar no mundo tech!")
        conhece = input("Tu já manja alguma coisa de programação? (s/n): ").lower()

        if conhece == "s":
            print("\nTopado! Segue esses caminhos:")
            print("- Rocketseat (Discover)")
            print("https://www.rocketseat.com.br/discover")
            print("- Alura Start")
            print("https://startalura.com.br/")
            print("- Programação Web (Senac PE)")
            print("https://www.sp.senac.br/cursos-livres/curso-de-programador-web")
        else:
            print("\nSuave! Começa assim ó:")
            print("- Curso de Lógica no YouTube")
            print("https://youtube.com/playlist?list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV")
            print("- Curso de Python básico na Fundação Bradesco")
            print("https://www.ev.org.br/")
            print("- HTML e CSS no Curso em Vídeo")
            print("https://www.cursoemvideo.com/")

    elif opcao == 0:
        print("\nValeu, mano! Até a próxima 😎")
        break

    else:
        print("\nVixe, opção inválida. Escolhe 1, 2 ou 3 aí que eu te ajudo de boa")

    # Pergunta se quer voltar pro início
    voltar = input("\nQuer voltar pro início e escolher outra opção? (s/n): ").lower()
    if voltar != "s":
        print("\nBeleza, valeu! Até mais 😎")
        break