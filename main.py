import requests
import pandas as pd

REQUEST_BASE_URL = 'https://statusinvest.com.br/acao/companytickerprovents?ticker={}&chartProventsType=2'

lista_ativos = ['BBAS3', 'ABEV3']

df = pd.DataFrame()

for codigo in lista_ativos:

    res = requests.get(REQUEST_BASE_URL.format(codigo))

    d = dict(res.json())

    data = pd.DataFrame(d['assetEarningsYearlyModels'])

    data = data.assign(stock = codigo)

    data.rename(columns = {'rank':'year', 'value':'dividend_per_share'}, inplace = True)

    data = data[['stock', 'year', 'dividend_per_share']]

    df = df.append(data)

print(df)

# idiv = pd.read_csv('~/Projects/python/barsi-dividend-method/data/idiv.csv')