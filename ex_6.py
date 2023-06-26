"""
Nome: Progressão Aritmética
Autor: Nikolas
Data: 26/06/2023
Versão: 0.0.1
"""

### Atribuição de variáveis e entrada de dados

n = float(input(f"Digite o primeiro termo 'n' de uma progressão aritmética:"))
print(n)

r = float(input(f"\nDigite a razão da progressão aritmética:"))
print(r)

nesima = float(input(f"\nDigite a n-ésima posição na série do termo desejado:"))
print(nesima)


### Processamento de dados

# Equação de Termos da P.A. --> termo_desejado_a = (primeiro_termo_an + ((n-ésima_posição - 1)*razão) )

termo = n + (nesima - 1)*r

# Equação de Soma dos Termos da P.A. --> soma_pa = ((primeiro_termo_an + termo_desejado_a)*(n-ésima_posição))/2

soma = ((n + termo)*(nesima))/2

### Saída de dados

print("\nO",nesima,"º termo da progressão aritmética com termo inicial igual a",n," e razão igual a",r,"é:",termo,".\nA soma dos termos da P.A. até (incluso) o número",termo,"é igual a:",soma,".")
