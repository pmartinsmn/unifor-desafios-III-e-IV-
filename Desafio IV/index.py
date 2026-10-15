from datetime import date
class Funcionario:
    def __init__(self, nome, data_contratacao, salario):
        self.nome = nome
        self.data_contratacao = data_contratacao
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * percentual / 100
        self.salario += aumento

    def bonus(self):
        print(f"{self.nome} recebeu o bonus de funcionario.")


class Gerente(Funcionario):
    def aumentar_salario(self, percentual):
        hoje = date.today()

        anos_servico = hoje.year - self.data_contratacao.year

        if (hoje.month, hoje.day) < (
            self.data_contratacao.month,
            self.data_contratacao.day
        ):
            anos_servico -= 1

        percentual_total = percentual + anos_servico

        super().aumentar_salario(percentual_total)

    def bonus(self):
        print(f"{self.nome} recebeu o bonus de gerente.")

funcionario = Funcionario(
    "Carlos",
    date(2022, 5, 10),
    2000.00
)

gerente = Gerente(
    "Mariana",
    date(2022, 5, 10),
    2000.00
)

print("=== ANTES DO AUMENTO ===")
print(f"Funcionario: R$ {funcionario.salario:.2f}")
print(f"Gerente: R$ {gerente.salario:.2f}")


funcionario.aumentar_salario(10)
gerente.aumentar_salario(10)


print("\n=== DEPOIS DO AUMENTO ===")
print(f"Funcionario: R$ {funcionario.salario:.2f}")
print(f"Gerente: R$ {gerente.salario:.2f}")


print("\n=== BONUS POLIMORFICO ===")

pessoas = [funcionario, gerente]

for pessoa in pessoas:
    pessoa.bonus()