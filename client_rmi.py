import Pyro5.api

def main():
  try:
    # Conecta ao objeto remoto
    calculadora = Pyro5.api.Proxy("PYRONAME:calculadora.remota")

    # Obtém a entrada do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Chamada remota
    sum_result = calculadora.soma(num1, num2)
    sub_result = calculadora.subtracao(num1, num2)
    mul_result = calculadora.multiplicacao(num1, num2)
    div_result = calculadora.divisao(num1, num2)

    # Imprime os resultados formatados sem zeros desnecessários
    print(f"Soma: {sum_result:g}")
    print(f"Subtração: {sub_result:g}")
    print(f"Multiplicação: {mul_result:g}")
    print(f"Divisão: {div_result:g}")

  except Pyro5.errors.PyroError as err:
    print(f"Erro: {err}")
  except ValueError:
    print("Entrada inválida. Digite apenas números.")

if __name__ == "__main__":
  main()

