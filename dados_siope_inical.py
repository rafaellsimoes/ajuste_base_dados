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


# dados Amazonas 

dados_totais = []

for year in range(2021, 2025):
    url = (f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/"
           f"Despesas_Funcao_Educacao_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)"
           f"?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='AM'&$top=10000"
           f"&$filter=TIPO%20eq%20'Estadual'"
           f"&$format=json"
           f"&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,NUM_ORDE,DES_SUBF,VAL_DESP_EMPE,VAL_DESP_LIQU,VAL_DESP_PAGA")
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for item in dados['value']:
                item['ANO'] = year
            dados_totais.extend(dados['value'])

dados_receitas_am_despesas = pd.DataFrame(dados_totais) 
dados_receitas_am_despesas.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_amazonas_siope.csv',index=False)
dados_receitas_am_despesas.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_amazonas_siope.xlsx',index=False)

print(dados_receitas_am_despesas.head())

dados_totais = []
for year in range(2021, 2025):
    url = (f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/"
          f"Receita_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)"
          f"?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='AM'&$top=10000"
          f"&$filter=TIPO%20eq%20'Estadual'"
          f"&$format=json"
          f"&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,COD_EXIB_FORMATADO,"
          f"NOM_ITEM,IDN_CLAS,NOM_COLU,NUM_NIVE,NUM_ORDE,VAL_DECL")
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for item in dados['value']:
                item['ANO'] = year
            dados_totais.extend(dados['value'])
            
dados_despesas_am = pd.DataFrame(dados_totais) 
print(dados_despesas_am.head())

dados_despesas_am.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_amazonas_siope.csv',index=False)
dados_despesas_am.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_amazonas_siope.xlsx',index=False)          
print(dados_despesas_am.head())

Dados Roraima

dados_totais = []

for year in range(2019, 2025):
    url = (f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/"
           f"Despesas_Funcao_Educacao_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)"
           f"?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='RR'&$top=10000"
           f"&$filter=TIPO%20eq%20'Estadual'"
           f"&$format=json"
           f"&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,NUM_ORDE,DES_SUBF,VAL_DESP_EMPE,VAL_DESP_LIQU,VAL_DESP_PAGA")
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for i in dados['value']:
                dados['ANO'] = year
            dados_totais.extend(dados['value'])
            
dados_despesas_rr = pd.DataFrame(dados_totais) 
dados_despesas_rr.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_roraima_siope.csv',index=False)
dados_despesas_rr.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_roraima_siope.xlsx',index=False)

dados_totais = []
 
for year in range(2019,2025):
    url = f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/Receita_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='RR'&$top=10000&$skip=0&$filter=TIPO%20eq%20'Estadual'&$format=json&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,COD_EXIB_FORMATADO,NOM_ITEM,IDN_CLAS,NOM_COLU,NUM_NIVE,NUM_ORDE,VAL_DECL"       
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for i in dados['value']:
                dados['ANO'] = year
            dados_totais.extend(dados['value'])
            
dados_receitas_rr = pd.DataFrame(dados_totais)

dados_receitas_rr.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_roraima_siope.csv',index=False)
dados_receitas_rr.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_roraima_siope.xlsx',index=False)
print(dados_receitas_rr.head())

Dados do Amapá

dados_totais = []

for year in range(2019,2025):
    url = f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/Despesas_Funcao_Educacao_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='AP'&$top=10000&$skip=0&$filter=TIPO%20eq%20'Estadual'&$format=json&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,NUM_ORDE,DES_SUBF,VAL_DESP_EMPE,VAL_DESP_LIQU,VAL_DESP_PAGA"
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for i in dados['value']:
                dados['ANO'] = year
            dados_totais.extend(dados['value'])
    
dados_despesas_ap = pd.DataFrame(dados_totais)
dados_despesas_ap.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_amapa_siope.csv',index=False)
dados_despesas_ap.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\despesas_amapa_siope.xlsx',index=False)

dados_totais = []

for year in range(2019,2025):
    url = f"https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata/Receita_Siope(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)?@Ano_Consulta={year}&@Num_Peri=1&@Sig_UF='AP'&$top=10000&$skip=0&$filter=TIPO%20eq%20'Estadual'&$format=json&$select=TIPO,NUM_ANO,NUM_PERI,COD_UF,SIG_UF,COD_MUNI,NOM_MUNI,COD_EXIB_FORMATADO,NOM_ITEM,IDN_CLAS,NOM_COLU,NUM_NIVE,NUM_ORDE,VAL_DECL"
    
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get('value'):
            for i in dados['value']:
                dados['ANO'] = year
            dados_totais.extend(dados['value'])
            
dados_receitas_ap = pd.DataFrame(dados_totais)
dados_receitas_ap.to_csv(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_amapa_siope.csv',index=False)
dados_receitas_ap.to_excel(r'C:\Users\orafa\OneDrive\Documents\dados impopulares\Dados Sociais\Educação + Judiciário\Dados SIOPE - ACRE\receitas_amapa_siope.xlsx',index=False)
print(dados_receitas_ap) - como vc melhoraria, com um vetor com a siglas dos estados?
