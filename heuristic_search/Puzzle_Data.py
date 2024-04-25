# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
def DataGathering():
    inFile1=open('heavy_cost_results.txt','r')
    inFile2=open('unit_cost_results.txt','r')
    Content1=inFile1.readlines()
    Content2=inFile2.readlines()
    Puzzle_number=[]
    Heavy_initial_heuristics=[]
    Heavy_initial_distance=[]
    Heavy_final_Sln_cst=[]
    Heavy_final_Sln_len=[]
    Heavy_tot_nodes_exp=[]
    Heavy_tot_nodes_gen=[]
    Unit_initial_heuristics=[]
    Unit_initial_distance=[]
    Unit_final_Sln_cst=[]
    Unit_final_Sln_len=[]
    Unit_tot_nodes_exp=[]
    Unit_tot_nodes_gen=[]
    for i in range(len(Content1)):
        if i%33==1:
            Puzzle_number.append(Content1[i].strip())
        if i%33==8:
            Con=Content1[i].split()
            num=Con[3].strip('"')
            Heavy_initial_heuristics.append(float(num))
        if i%33==9:
            Con=Content1[i].split()
            num=Con[3].strip('"')
            Heavy_initial_distance.append(float(num))
        if i%33==11:
            Con=Content1[i].split()
            num=Con[4].strip('"')
            Heavy_final_Sln_cst.append(float(num))
        if i%33==14:
            Con=Content1[i].split()
            num=Con[4].strip('"')
            Heavy_final_Sln_len.append(float(num))
        if i%33==17:
            Con=Content1[i].split()
            num=Con[4].strip('"')
            Heavy_tot_nodes_exp.append(float(num))
        if i%33==18:
            Con=Content1[i].split()
            num=Con[4].strip('"')
            Heavy_tot_nodes_gen.append(float(num))
    for j in range(len(Content2)):
        if j%33==8:
            Con=Content2[j].split()
            num=Con[3].strip('"')
            Unit_initial_heuristics.append(float(num))
        if j%33==9:
            Con=Content2[j].split()
            num=Con[3].strip('"')
            Unit_initial_distance.append(float(num))
        if j%33==11:
            Con=Content2[j].split()
            num=Con[4].strip('"')
            Unit_final_Sln_cst.append(float(num))
        if j%33==14:
            Con=Content2[j].split()
            num=Con[4].strip('"')
            Unit_final_Sln_len.append(float(num))
        if j%33==17:
            Con=Content2[j].split()
            num=Con[4].strip('"')
            Unit_tot_nodes_exp.append(float(num))
        if j%33==18:
            Con=Content2[j].split()
            num=Con[4].strip('"')
            Unit_tot_nodes_gen.append(float(num))

    data={
    'Heavy_initial_heuristics': Heavy_initial_heuristics,
    "Heavy_initial_distance": Heavy_initial_distance,
    "Heavy_final_Sln_cst": Heavy_final_Sln_cst,
    "Heavy_final_Sln_len": Heavy_final_Sln_len,
    "Heavy_tot_nodes_exp": Heavy_tot_nodes_exp,
    "Heavy_tot_nodes_gen": Heavy_tot_nodes_gen,
    "Unit_initial_heuristics": Unit_initial_heuristics,
    "Unit_initial_distance": Unit_initial_distance,
    "Unit_final_Sln_cst": Unit_final_Sln_cst,
    "Unit_final_Sln_len": Unit_final_Sln_len,
    "Unit_tot_nodes_exp": Unit_tot_nodes_exp,
    "Unit_tot_nodes_gen": Unit_tot_nodes_gen,
    }

    row_labels=Puzzle_number 
    Data=pd.DataFrame(data=data,index=row_labels)
    inFile1.close()
    inFile2.close()
    return Data


# %%
Data=DataGathering()


# %%
Data['Hvy h/d']=Data['Heavy_initial_heuristics'].values/Data['Heavy_initial_distance'].values
Data['HScst/HSlen']=Data['Heavy_final_Sln_cst'].values/Data['Heavy_final_Sln_len'].values
Data['HScst/UScst']=Data['Heavy_final_Sln_cst'].values/Data['Unit_final_Sln_cst'].values
Data['UScst/USlen']=Data['Unit_final_Sln_cst'].values/Data['Unit_final_Sln_len'].values


# %%
#loop through the puzzles
Puzzles=Data.index
Heavy_better=[]
Unit_better=[]
for puz in Puzzles:
    if Data.loc[[puz],['Heavy_tot_nodes_exp']].values < Data.loc[[puz],['Unit_tot_nodes_exp']].values:
        Heavy_better.append(puz)
    else:
        Unit_better.append(puz)
Hvy_does_better= Data.loc[Heavy_better]
Unit_does_better=Data.loc[Unit_better]


# %%
Hvy_does_better['HScst/HSlen'].values.mean()


# %%
Unit_does_better['HScst/HSlen'].values.mean()


# %%



