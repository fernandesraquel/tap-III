import xmlrpc.client

def main():
  try:
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    # Obtem a entrada do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Chamada remota
    sum_result = proxy.soma(num1, num2)
    sub_result = proxy.subtracao(num1, num2)
    mul_result = proxy.multiplicacao(num1, num2)
    div_result = proxy.divisao(num1, num2)

    # Imprime os resultados formatados sem zeros desnecessários
    print(f"Soma: {sum_result:g}")
    print(f"Subtração: {sub_result:g}")
    print(f"Multiplicação: {mul_result:g}")
    print(f"Divisão: {div_result:g}")

  except xmlrpc.client.Fault as err:
    print(f"Erro: {err}")
  except ValueError:
    print("Entrada inválida. Digite apenas números.")

if __name__ == "__main__":
  main()
