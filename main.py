import pandas as pd
from IPython.display import display

# show results
print("Saved results into files bills_votes.csv e legislators_sup_opp.csv.")

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
# Adding o primary sponsor
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


# Question 1. For every legislator in the dataset, how many bills did the legislator support(voted for the bill)? How many bills did the legislator oppose?

votes_per_legislator_per_bill.loc[:, "Supported bills"] = (votes_per_legislator_per_bill.vote_type == 1).astype(int)
votes_per_legislator_per_bill.loc[:, "Opposed bills"] = (votes_per_legislator_per_bill.vote_type == 2).astype(int)
group_data = votes_per_legislator_per_bill[['name','Supported bills', 'Opposed bills']].groupby(["name"]).sum().reset_index()
group_data.rename(columns={"name": "Legislator"}, inplace=True)

display(group_data)


# Question 2. For every bill in the data set, how many legislators supported the bill? How many legislators opposed the bill? Who was the primary sponsor of the bill?
votes_per_legislator_per_bill.loc[:, "Supporters"] = (votes_per_legislator_per_bill.vote_type == 1).astype(int)
votes_per_legislator_per_bill.loc[:, "Opposers"] = (votes_per_legislator_per_bill.vote_type == 2).astype(int)
group_data = votes_per_legislator_per_bill[['title', 'Supporters', 'Opposers', 'Primary sponsor']].groupby('title').agg(
    Supporters=('Supporters', 'sum'),
    Opposers=('Opposers', 'sum'),
    Primary=('Primary sponsor', 'first')
).reset_index()

group_data.rename(columns={'title': 'Bill', 'Primary': 'Primary sponsor'}, inplace=True)

display(group_data)
