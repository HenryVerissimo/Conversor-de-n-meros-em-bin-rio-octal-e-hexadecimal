pergunta = str(input("Deseja converter um número? (sim/não) ").strip().lower())

while pergunta not in "nao não":
    if pergunta == "sim":
        while True:
            try:
                numero = int(input("Digite o número inteiro que deseja converter: ").strip())
                break
            except ValueError:
                print("Você precisa digitar um número inteiro ")

        escolha = str(input("Digite o tipo de conversão que deseja fazer (binário, octal, hexadecimal): ").strip().lower())
        quociente = numero
        resultado = ""
        conversao = ""

        if escolha in "binario binário octal hexadecimal":
            while True:
                if escolha == "binario" or escolha == "binário":
                    
                    #Convertendo o número em código binário
                    while quociente > 0:
                        if resultado == "":
                            resultado = str(quociente % 2)
                        else:
                            resultado = resultado + str(quociente % 2)
                        quociente = quociente // 2
                        conversao = "binário"
                    break

                elif escolha == "octal":

                    #Conovertendo o número em octal
                    while quociente > 0:
                        if resultado == "":
                            resultado = str(quociente % 8)
                        else:
                            resultado = resultado + str(quociente % 8)
                        quociente = quociente // 8
                        conversao = "octal"
                    break

                elif escolha == "hexadecimal":

                    #convertendo o número em hexadecimal
                    while quociente > 0:
                        if resultado == "":
                            if (quociente % 16) < 10:
                                resultado = str(quociente % 16)
                            else:
                                numeroLetra = quociente % 16
                                if numeroLetra == 10:
                                    resultado = resultado + "A"
                                elif numeroLetra == 11:
                                    resultado = resultado + "B"
                                elif numeroLetra == 12:
                                    resultado = resultado + "C"
                                elif numeroLetra == 13:
                                    resultado = resultado + "D"
                                elif numeroLetra == 14:
                                    resultado = resultado + "E"
                                else:
                                    resultado = resultado + "F"
                        else:
                            if quociente % 16 < 10:
                                resultado = resultado + str(quociente % 16)
                            else:
                                numeroLetra = quociente % 16
                                if numeroLetra == 10:
                                    resultado = resultado + "A"
                                elif numeroLetra == 11:
                                    resultado = resultado + "B"
                                elif numeroLetra == 12:
                                    resultado = resultado + "C"
                                elif numeroLetra == 13:
                                    resultado = resultado + "D"
                                elif numeroLetra == 14:
                                    resultado = resultado + "E"
                                else:
                                    resultado = resultado + "F"

                        quociente = quociente // 16
                        conversao = "hexadecimal"
                    break
                    
            #invertendo a ordem dos caracteres
            resultado = resultado[::-1]

            print(f"O número {numero} em {conversao} fica: \033[1;32m{resultado}\033[m") 

        else:
            print("Opção de conversão inválida!")
    else:
        print("Você precisa digitar sim ou não!")

    print(100 * "-")
    pergunta = str(input("Deseja converter um número? (sim/não) ").strip().lower())

print("Prçograma finalizado!")             
             
            
                    