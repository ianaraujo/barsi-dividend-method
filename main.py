import requests
import pandas as pd

idiv = pd.read_csv("data/idiv.csv", sep=';')

REQUEST_BASE_URL = 'https://statusinvest.com.br/acao/companytickerprovents?ticker={}&chartProventsType=2'

lista_ativos = idiv['codigo'].to_list()

df = pd.DataFrame()

for codigo in lista_ativos:

    res = requests.get(REQUEST_BASE_URL.format(codigo))

    d = dict(res.json())

    data = pd.DataFrame(d['assetEarningsYearlyModels'])

    data = data.assign(stock = codigo)

    data.rename(columns = {'rank':'year', 'value':'dividend_per_share'}, inplace = True)

    data = data[['stock', 'year', 'dividend_per_share']] # reorder columns

    df = df.append(data)

print(df)
