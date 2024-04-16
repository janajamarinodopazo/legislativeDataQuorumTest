import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

# Instanciando os serviços e repositórios
# legislator_service = LegislatorService()
# bills_service = BillsService()

# # Escrevendo os resultados nos arquivos CSV
# WriteCsv.write_bills_votes(bills_votes)
# WriteCsv.write_legislators_sup_opp(legislator_votes)

# # Processando os dados
# legislator_votes = legislator_service.count_bills_votes()
# bills_votes = bills_service.count_legislator_votes()


# Exibindo os resultados
print("Resultados salvos nos arquivos bills_votes.csv e legislators_sup_opp.csv.")

bills = pd.read_csv("bills.csv")
legislator = pd.read_csv("legislators.csv")
votes = pd.read_csv("votes.csv")
vote_results = pd.read_csv("vote_results.csv")

# Votes per legislator
votes_per_legislator = pd.merge(
    vote_results,
    legislator,
    how="left",
    left_on="legislator_id",
    right_on="id",
    suffixes=('', "_y")
)
del votes_per_legislator['id_y']
# Adding bill information
votes_per_legislator_per_bill = pd.merge(
    votes_per_legislator,
    votes,
    how="left",
    left_on="vote_id",
    right_on="id",
    suffixes=('', '_y')
)
del votes_per_legislator_per_bill['id_y']
votes_per_legislator_per_bill = pd.merge(
    votes_per_legislator_per_bill,
    bills,
    how="left",
    left_on="bill_id",
    right_on="id",
    suffixes=('', '_y')
)
del votes_per_legislator_per_bill['id_y']
# Adicionando o primary sponsor
votes_per_legislator_per_bill = pd.merge(
    votes_per_legislator_per_bill,
    legislator,
    how="left",
    left_on="sponsor_id",
    right_on="id",
    suffixes=('', '_y')
)
del votes_per_legislator_per_bill['id_y']
votes_per_legislator_per_bill.rename(columns={"name_y": "Primary sponsor"}, inplace=True)





# Question 1. Qual bill cada legislator votou?
# CONSIDERANDO UM legislator QUALQUER
votes_per_legislator_per_bill.loc[:, "Supported bills"] = (votes_per_legislator_per_bill.vote_type == 1).astype(int)
votes_per_legislator_per_bill.loc[:, "Opposed bills"] = (votes_per_legislator_per_bill.vote_type == 2).astype(int)
dados_agrupados = votes_per_legislator_per_bill[['name', 'Supported bills', 'Opposed bills']].groupby(["name"]).sum().reset_index()
dados_agrupados.rename(columns={"name": "Legislator"}, inplace=True)

legislator = dados_agrupados.Legislator.values[5]
display(dados_agrupados[dados_agrupados.Legislator == legislator])

# Question 2. Para cada bill, quantos legislators apoiaram e quantos se opuseram. Quem foi o primary sponsor
votes_per_legislator_per_bill.loc[:, "Supporters"] = (votes_per_legislator_per_bill.vote_type == 1).astype(int)
votes_per_legislator_per_bill.loc[:, "Opposers"] = (votes_per_legislator_per_bill.vote_type == 2).astype(int)
dados_agrupados = votes_per_legislator_per_bill[['title', 'Supporters', 'Opposers', 'Primary sponsor']].groupby('title').agg(
    Supporters=('Supporters', 'sum'),
    Opposers=('Opposers', 'sum'),
    Primary=('Primary sponsor', 'first')
).reset_index()

dados_agrupados.rename(columns={'title': 'Bill', 'Primary': 'Primary sponsor'}, inplace=True)
bill = dados_agrupados.Bill.values[0]
display(dados_agrupados[dados_agrupados.Bill == bill])