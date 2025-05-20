import requests
import pandas as pd


dados_gerais = []
for year in range(2021, 2025):
    url = (f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/"
           f"Despesas_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)"
           f"?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='AC'&$top=10000&$skip=0&$format=json"
           f"&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,NOM_PAST,"
           f"IDN_EXIB_CODI,COD_PAST,COD_SUBF,TIP_PASTA,COD_EXIB,COD_EXIB_FORMATADO,"
           f"COD_FONTE,NOM_ITEM,IDN_CLAS,NOM_COLU,NUM_NIVE,NUM_ORDE,VAL_DECL")
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for item in dados['value']:
                item['ANO'] = year
            dados_gerais.extend(dados['value'])

dados_despesas_ac = pd.DataFrame(dados_gerais)
dados_despesas_ac.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_acre_siope.csv', index=False)
dados_despesas_ac.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_acre_siope.xlsx', index=False)


dados_totais = []
for year in range(2021, 2025):
    url = (f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/"
           f"Receita_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)"
           f"?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='AC'&$top=10000&$format=json"
           f"&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,"
           f"COD_EXIB_FORMATADO,NOM_ITEM,IDN_CLAS,NOM_COLU,NUM_NIVE,NUM_ORDE,VAL_DECL")
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for item in dados['value']:
                item['ANO'] = year
            dados_totais.extend(dados['value'])

dados_totais_ac = pd.DataFrame(dados_totais)
dados_totais_ac.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_acre_siope.csv', index=False)
dados_totais_ac.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_acre_siope.xlsx', index=False)
