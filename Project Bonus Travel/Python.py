# Passo a passo de solução

# Abrir os 6 arquivos em Excel

# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada

# Será necessário utilizar algumas integrações (importando módulo) as seguintes ferramentas: pandas/ openpyxl/ twilio.

# Pandas e Openpyxl (integração do Python com Excel)
# Twilio (integração do Python com o SMS)



import pandas as pd 

list_month = ['january', 'february', 'march', 'april', 'may', 'june']

for month in list_month:
    print(month)
    spreedsheet_sales = pd.read_excel(f'{month}.xlsx')
    print(spreedsheet_sales)
    if (spreedsheet_sales['Vendas'] > 550000):any()