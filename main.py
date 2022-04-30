import requests
import pandas as pd

idiv = pd.read_csv("data/idiv.csv", sep=';')

REQUEST_BASE_URL = 'https://statusinvest.com.br/acao/companytickerprovents?ticker={}&chartProventsType=2'

ativos_idiv = idiv['codigo'].to_list()


def dividend_info(ativos: list) -> pd.DataFrame:

    df = pd.DataFrame()

    for codigo in ativos:

        res = requests.get(REQUEST_BASE_URL.format(codigo))

        d = dict(res.json())

        data = pd.DataFrame(d['assetEarningsYearlyModels'])

        data = data.assign(stock=codigo)

        data = data.rename(
            columns={'rank': 'year', 'value': 'dividend_per_share'})

        data = data[['stock', 'year', 'dividend_per_share']]  # reorder columns

        df = df.append(data)

    return df


df = dividend_info(ativos=ativos_idiv)

<<<<<<< HEAD
df_dividend = df.groupby('stock')[['dividend_per_share']].mean()

=======
df = df[df['year'].between(2017, 2021)]

mean_dividend_5y = pd.DataFrame(df['dividend_per_share'].groupby(df['stock']).mean())
>>>>>>> 049ffc3a6e114d6a92e47ccd4a31aa88c99c5964
