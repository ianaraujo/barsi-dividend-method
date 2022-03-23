import requests
import pandas as pd

REQUEST_BASE_URL = 'https://statusinvest.com.br/acao/companytickerprovents?ticker={}&chartProventsType=2'

lista_ativos = ['BBAS3', 'ABEV3']

for codigo in lista_ativos:

    url = REQUEST_BASE_URL.format(codigo)

    res = requests.get(url)

    d = dict(res.json())

    data = pd.DataFrame(d['assetEarningsYearlyModels'])

    data.rename(columns = {'rank':'year', 'value':'dividend_per_share'}, inplace = True)

    print(data)

# idiv = pd.read_csv('~/Projects/python/barsi-dividend-method/data/idiv.csv')