#%%

def get_variable_description(variable_name):
    """
    Retourne la description d'une variable.

    Args:
        variable_name (str): Le nom de la variable.

    Returns:
        str: La description de la variable, ou un message d'erreur si non trouvée.
    """
    if variable_name in ESS_CODEBOOK:
        if "description" in ESS_CODEBOOK[variable_name]:
            return ESS_CODEBOOK[variable_name]["description"]
        else:
            return f"Pas de description pour la variable '{variable_name}'."
    else:
        return f"Variable '{variable_name}' non trouvée dans le codebook."
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

ESS_CODEBOOK = {
    "pweight": {
        "description": "Poids de la population (doit être combiné avec dweight ou pspwght). / Population size weight (must be combined with dweight or pspwght).",
        "mapping": {}, # numérique pas de mapping direct fixe
        "type": "weight"
    },
    "dweight": {
        "description": "Poids de conception. / Design weight.", # Modified description to match the filter list more closely
        "mapping": {}, #  numérique
        "type": "weight"
    },
    "cntry": {
        "description": "Pays. / Country.",
        "mapping": {
            "AL": "Albania",
            "AT": "Austria",
            "BE": "Belgium",
            "BG": "Bulgaria",
            "CH": "Switzerland",
            "CY": "Cyprus",
            "CZ": "Czechia",
            "DE": "Germany",
            "DK": "Denmark",
            "EE": "Estonia",
            "ES": "Spain",
            "FI": "Finland",
            "FR": "France",
            "GB": "United Kingdom",
            "GE": "Georgia",
            "GR": "Greece",
            "HR": "Croatia",
            "HU": "Hungary",
            "IE": "Ireland",
            "IS": "Iceland",
            "IL": "Israel",
            "IT": "Italy",
            "LT": "Lithuania",
            "LU": "Luxembourg",
            "LV": "Latvia",
            "ME": "Montenegro",
            "MK": "North Macedonia",
            "NL": "Netherlands",
            "NO": "Norway",
            "PL": "Poland",
            "PT": "Portugal",
            "RO": "Romania",
            "RS": "Serbia",
            "RU": "Russian Federation",
            "SE": "Sweden",
            "SI": "Slovenia",
            "SK": "Slovakia",
            "TR": "Turkey",
            "UA": "Ukraine",
            "XK": "Kosovo"
        },
        "type": "country_code"
    },
    "idno": {
        "description": "Numéro d'identification du répondant. / Respondent's identification number.",
        "mapping": {}, # Identifiant unique
        "type": "identifier"
    },
    "edition": {
        "description": "Édition. / Edition.",
        "mapping": {}, # Texte ou numérique
        "type": "metadata"
    },
    "proddate": {
        "description": "Date de production. / Production date.",
        "mapping": {}, # Date
        "type": "metadata_date"
    },
    "pspwght": {
        "description": "Poids post-stratification incluant le poids de conception. / Post-stratification weight including design weight.",
        "mapping": {}, # Probablement numérique
        "type": "weight"
    },
    "essround": {
        "description": "Ronde de l'ESS (European Social Survey). / ESS round.",
        "mapping": {}, # Numérique
        "type": "metadata_numeric"
    },
    "name": {
        "description": "Titre du jeu de données. / Title of dataset.",
        "mapping": {}, # Texte
        "type": "metadata_text"
    },
    "badge": {
        "description": "A porté ou affiché un badge/autocollant de campagne au cours des 12 derniers mois. / Worn or displayed campaign badge/sticker last 12 months.",
        "mapping": {
            1: "Yes",
            2: "No",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_yes_no"
    },
    "bctprd": {
        "description": "A boycotté certains produits au cours des 12 derniers mois. / Boycotted certain products last 12 months.",
        "mapping": {
            1: "Yes",
            2: "No",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_yes_no"
    },
    "imwbcnt": {
        "description": "Les immigrants rendent le pays meilleur ou pire pour vivre. / Immigrants make country worse or better place to live.",
        "mapping": {
            0: "Worse place to live",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Better place to live",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_opinion"
    },
    "imueclt": {
        "description": "La vie culturelle du pays est minée ou enrichie par les immigrants. / Country's cultural life undermined or enriched by immigrants.",
        "mapping": {
            0: "Cultural life undermined",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Cultural life enriched",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_opinion"
    },
    "imbgeco": {
        "description": "L'immigration est bonne ou mauvaise pour l'économie du pays. / Immigration bad or good for country's economy.",
        "mapping": {
            0: "Bad for the economy",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Good for the economy",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_opinion"
    },
    "impcntr": {
        "description": "Permettre à beaucoup/peu d'immigrants de pays pauvres hors d'Europe. / Allow many/few immigrants from poorer countries outside Europe.",
        "mapping": {
            1: "Allow many to come and live here",
            2: "Allow some",
            3: "Allow a few",
            4: "Allow none",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_opinion"
    },
    "vote": {
        "description": "A voté lors de la dernière élection nationale. / Voted last national election.",
        "mapping": {
            1: "Yes",
            2: "No",
            3: "Not eligible to vote",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_vote"
    },
    "trstun": {
        "description": "Confiance dans les Nations Unies. / Trust in the United Nations.",
        "mapping": {
            0: "No trust at all",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Complete trust",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_trust"
    },
    "trstprl": {
        "description": "Confiance dans le parlement du pays. / Trust in country's parliament.",
        "mapping": {
            0: "No trust at all",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Complete trust",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_trust"
    },
    "trstplt": {
        "description": "Confiance dans les politiciens. / Trust in politicians.",
        "mapping": {
            0: "No trust at all",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Complete trust",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_trust"
    },
    "trstplc": {
        "description": "Confiance dans la police. / Trust in the police.",
        "mapping": {
            0: "No trust at all",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Complete trust",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_trust"
    },
    "trstlgl": {
        "description": "Confiance dans le système juridique. / Trust in the legal system.",
        "mapping": {
            0: "No trust at all",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Complete trust",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_trust"
    },
    "trstep": {
        "description": "Confiance dans le Parlement européen. / Trust in the European Parliament.",
        "mapping": {
            0: "No trust at all",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Complete trust",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_trust"
    },
    "stflife": {
        "description": "Satisfaction de la vie dans son ensemble. / How satisfied with life as a whole.",
        "mapping": {
            0: "Extremely dissatisfied",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Extremely satisfied",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_satisfaction"
    },
    "stfhlth": {
        "description": "État des services de santé dans le pays de nos jours. / State of health services in country nowadays.",
        "mapping": {
            0: "Extremely bad",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Extremely good",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_state_evaluation"
    },
    "stfedu": {
        "description": "État de l'éducation dans le pays de nos jours. / State of education in country nowadays.",
        "mapping": {
            0: "Extremely bad",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Extremely good",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_state_evaluation"
    },
    "stfeco": {
        "description": "Satisfaction de l'état actuel de l'économie dans le pays. / How satisfied with present state of economy in country.",
        "mapping": {
            0: "Extremely dissatisfied",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Extremely satisfied",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_satisfaction"
    },
    "stfdem": {
        "description": "Satisfaction du fonctionnement de la démocratie dans le pays. / How satisfied with the way democracy works in country.",
        "mapping": {
            0: "Extremely dissatisfied",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Extremely satisfied",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_satisfaction"
    },
    "sgnptit": {
        "description": "A signé une pétition au cours des 12 derniers mois. / Signed petition last 12 months.",
        "mapping": {
            1: "Yes",
            2: "No",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_yes_no"
    },
    "polintr": {
        "description": "Intérêt pour la politique. / How interested in politics.",
        "mapping": {
            1: "Very interested",
            2: "Quite interested",
            3: "Hardly interested",
            4: "Not at all interested",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_interest"
    },
    "lrscale": {
        "description": "Positionnement sur l'échelle gauche-droite. / Placement on left right scale.",
        "mapping": {
            0: "Left",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "Right",
            77: "Refusal",
            88: "Don't know",
            99: "No answer"
        },
        "type": "scale_0_10_political_spectrum"
    },
    "gincdif": {
        "description": "Le gouvernement devrait réduire les différences de niveaux de revenu. / Government should reduce differences in income levels.",
        "mapping": {
            1: "Agree strongly",
            2: "Agree",
            3: "Neither agree nor disagree",
            4: "Disagree",
            5: "Disagree strongly",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "likert_5_agreement"
    },
    "freehms": {
        "description": "Les gays et lesbiennes sont libres de vivre leur vie comme ils le souhaitent. / Gays and lesbians free to live life as they wish.",
        "mapping": {
            1: "Agree strongly",
            2: "Agree",
            3: "Neither agree nor disagree",
            4: "Disagree",
            5: "Disagree strongly",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "likert_5_agreement"
    },
    "contplt": {
        "description": "A contacté un politicien ou un fonctionnaire du gouvernement au cours des 12 derniers mois. / Contacted politician or government official last 12 months.",
        "mapping": {
            1: "Yes",
            2: "No",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_yes_no"
    },
    "clsprty": {
        "description": "Se sent plus proche d'un parti particulier que de tous les autres partis. / Feel closer to a particular party than all other parties.",
        "mapping": {
            1: "Yes",
            2: "No",
            7: "Refusal",
            8: "Don't know",
            9: "No answer"
        },
        "type": "categorical_yes_no"
    }

}
