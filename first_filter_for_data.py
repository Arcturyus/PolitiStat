#%%
import pandas as pd

file_path = 'data/ESS Theme - Politics.csv'
data = pd.read_csv(file_path)

null_counts = data.isnull().sum()
all_null_columns = data.columns[data.isnull().all()]

print("Nombre de valeurs nulles par colonne :")
print(null_counts)

print("\nColonnes avec uniquement des valeurs nulles :")
print(all_null_columns.tolist())
#%%
null_percentages = data.isnull().mean() * 100
null_percentages_df = null_percentages.reset_index()
null_percentages_df.columns = ['Colonne', 'Pourcentage de valeurs nulles']
null_percentages_df = null_percentages_df.sort_values(by='Pourcentage de valeurs nulles', ascending=False)
null_percentages_df.to_csv('data/percentages_nulles.csv', index=False)

#%%

"""
    pweight : Poids de la population (doit être combiné avec dweight ou pspwght).
    dweight : Poids de conception. (design weight)
    cntry : Pays.
    idno : Numéro d'identification du répondant.
    edition : Édition.
    proddate : Date de production.
    pspwght : Poids post-stratification incluant le poids de conception.
    essround : Ronde de l'ESS (European Social Survey).
    badge : A porté ou affiché un badge/autocollant de campagne au cours des 12 derniers mois.
    bctprd : A boycotté certains produits au cours des 12 derniers mois.
    imwbcnt : Les immigrants rendent le pays meilleur ou pire pour vivre.
    imueclt : La vie culturelle du pays est minée ou enrichie par les immigrants.
    imbgeco : L'immigration est bonne ou mauvaise pour l'économie du pays.
    impcntr : Permettre à beaucoup/peu d'immigrants de pays pauvres hors d'Europe.
    vote : A voté lors de la dernière élection nationale.
    trstun : Confiance dans les Nations Unies.
    trstprl : Confiance dans le parlement du pays.
    trstplt : Confiance dans les politiciens.
    trstplc : Confiance dans la police.
    trstlgl : Confiance dans le système juridique.
    trstep : Confiance dans le Parlement européen.
    stflife : Satisfaction de la vie dans son ensemble.
    stfhlth : État des services de santé dans le pays de nos jours.
    stfedu : État de l'éducation dans le pays de nos jours.
    stfeco : Satisfaction de l'état actuel de l'économie dans le pays.
    stfdem : Satisfaction du fonctionnement de la démocratie dans le pays.
    sgnptit : A signé une pétition au cours des 12 derniers mois.
    polintr : Intérêt pour la politique.
    lrscale : Positionnement sur l'échelle gauche-droite.
    gincdif : Le gouvernement devrait réduire les différences de niveaux de revenu.
    freehms : Les gays et lesbiennes sont libres de vivre leur vie comme ils le souhaitent.
    contplt : A contacté un politicien ou un fonctionnaire du gouvernement au cours des 12 derniers mois.
    clsprty : Se sent plus proche d'un parti particulier que de tous les autres partis.
    name : Titre du jeu de données.
"""
colonnes_a_conserver = [
    'pweight', 'dweight', 'cntry', 'idno', 'edition', 'proddate',
    'pspwght', 'essround', 'badge', 'bctprd', 'imwbcnt', 'imueclt',
    'imbgeco', 'impcntr', 'vote', 'trstun', 'trstprl', 'trstplt',
    'trstplc', 'trstlgl', 'trstep', 'stflife', 'stfhlth', 'stfedu',
    'stfeco', 'stfdem', 'sgnptit', 'polintr', 'lrscale', 'gincdif',
    'freehms', 'contplt', 'clsprty', 'name'
]

data_filtre = data[colonnes_a_conserver]
data_filtre.to_pickle('data/Politics_filtered.pkl')
