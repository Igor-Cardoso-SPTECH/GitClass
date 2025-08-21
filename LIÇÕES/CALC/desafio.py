

def pergunta():
 while True:
    peso = float(input("Digite Seu peso (Kg):"))
    altura = float(input("Digite Sua altura (M): "))   
    if validar(peso,altura):
        break




 imc = peso/(altura**2)




 print(f"\nSeu peso:{peso}\n"\
      f"Sua Altura: {altura}\n"\
      f"Seu IMC é: {round(imc,2)}"   )

 if imc < 16:
  mensagem = "Baixo peso muito grave"
 elif imc < 17:
   mensagem ="Baixo peso grave"
 elif imc < 18.5:
   mensagem ="Baixo peso"
 elif imc < 25:
   mensagem ="Peso ideal"
 elif imc < 30:
   mensagem ="Sobrepeso"
 elif imc < 35:
   mensagem = "Obesidade grau I"
 elif imc < 40:
   mensagem ="Obesidade grau II"
 else:
   mensagem ="Obesidade mórbida"


 print(f" \nSeu IMC é {round(imc,2)} – {mensagem}")
 retornar()


def validar(peso,altura):
 
    if peso <= 0:
        print('Valor Incorreto preencha novamente')
        return False
    if altura <= 0:
        print('Valor Incorreto preencha novamente')
        return False

    return True


def retornar():
 while(True):
  resposta = input("\nDeseja calcular o IMC de outra pessoa? (s/n):")
 
  if (resposta == "s"):
     pergunta()
     break
  elif(resposta == "n"):
     print("\nEncerrando a calculadora...")
     break
  else:
    print("\nUse somente (s) ou (n) para que não tenhamos problema na BIOS")


pergunta()