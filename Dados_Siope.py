import requests
import pandas as pd


BASE_URL = "https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/"
SAVE_PATH = r'path_to_save'


ESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
           'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
           'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
ANOS = {
    'AC': range(2015, 2025),
    'AM': range(2015, 2025),
    'RR': range(2015, 2025),
    'AP': range(2015, 2025),
    'PA': range(2015, 2025),
    'RO': range(2015, 2025),
    'TO': range(2015, 2025),
    'MA': range(2015, 2025),
    'PI': range(2015, 2025),
    'CE': range(2015, 2025),
    'RN': range(2015, 2025),
    'PB': range(2015, 2025),
    'PE': range(2015, 2025),
    'AL': range(2015, 2025),
    'SE': range(2015, 2025),
    'BA': range(2015, 2025),
    'ES': range(2015, 2025),
    'RJ': range(2015, 2025),
    'SP': range(2015, 2025),
    'MG': range(2015, 2025),
    'PR': range(2015, 2025),
    'SC': range(2015, 2025),
    'RS': range(2015, 2025),
    'MS': range(2015, 2025),
    'DF': range(2015, 2025),
    'MT': range(2015, 2025),
    'GO': range(2015, 2025)
}

def fetch_data(endpoint, estado, year, filters=None, select_fields=None):
    url = f"{BASE_URL}{endpoint}(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)"
    url += f"?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='{estado}'"
    url += f"&$top=10000&$format=json"
    if filters:
        url += f"&$filter={filters}"
    if select_fields:
        url += f"&$select={select_fields}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        dados = response.json()
        if dados.get('value'):
            for item in dados['value']:
                item['ANO'] = year
            return dados['value']
        return []
    except requests.exceptions.RequestException as e:
        return []

def save_data(df, tipo, estado):
    if df.empty:
        return
    filename = f"{tipo.lower()}_{estado.lower()}_siope"
    try:
        df.to_csv(f"{SAVE_PATH}\\{filename}.csv", index=False, encoding='utf-8-sig')
        df.to_excel(f"{SAVE_PATH}\\{filename}.xlsx", index=False)

    except Exception as e:
for estado in ESTADOS:
    despesas_totais = []
    endpoint = "Despesas_Funcao_Educacao_Siope" if estado != 'AC' else "Despesas_Siope"
    
    for year in ANOS[estado]:
        filters = "TIPO%20eq%20'Estadual'" if estado != 'AC' else None
        select_fields = (
            "TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,NUM_ORDE,DES_SUBF,VAL_DESP_EMPE,VAL_DESP_LIQU,VAL_DESP_PAGA" 
            if estado != 'AC' else 
            "TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,NOM_PAST,IDN_EXIB_CODI,COD_PAST,COD_SUBF,TIP_PASTA,COD_EXIB,COD_EXIB_FORMATADO,COD_FONTE,NOM_ITEM,IDN_CLAS,NOM_COLU,NUM_NIVE,NUM_ORDE,VAL_DECL"
        )
        
        dados = fetch_data(endpoint, estado, year, filters, select_fields)
        despesas_totais.extend(dados)
    
    if despesas_totais:
        df_despesas = pd.DataFrame(despesas_totais)
        save_data(df_despesas, "despesas", estado)
    receitas_totais = []
    for year in ANOS[estado]:
        filters = "TIPO%20eq%20'Estadual'" if estado != 'AC' else None
        select_fields = "TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,COD_EXIB_FORMATADO,NOM_ITEM,IDN_CLAS,NOM_COLU,NUM_NIVE,NUM_ORDE,VAL_DECL"
        dados = fetch_data("Receita_Siope", estado, year, filters, select_fields)
        receitas_totais.extend(dados)
    if receitas_totais:
        df_receitas = pd.DataFrame(receitas_totais)
        save_data(df_receitas, "receitas", estado)

print("\nProcessamento concluído!")
        
