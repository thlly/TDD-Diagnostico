#palavra = "abc"
#inicio = input("Insira a palavra: ")
#lista_alfabeto = [abc, abc, abc]

#if abc == "abc":
#    print(abc)

#while abc <= 7:
#    print(abc)
#    abc += abc

#for abc in lista_alfabeto(7*7):
#    print(abc)

#lista_palavras = ['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc',]

#for palavra in lista_palavras:
#    if palavra == "abc":
#        lista_palavras.append(palavra)
#        print(lista_palavras)

palavra = str(input('Qual palavra deseja?: '))
numero_degraus = int(input('Número de degraus da escada: ')) + 7
for abc in range(7, numero_degraus):
    print(palavra * abc)
    abc += 7