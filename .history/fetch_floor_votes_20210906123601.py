def get_votes(member):
    import requests 
    import pandas as pd 
    import json 
    base_url = r"https://oda.ft.dk/api/Stemme?$inlinecount=allpages&$filter=akt%C3%B8rid%20eq%20"
    vote_types = {
        1: "For",
        2: "Imod",
        3: "Fravær",
        4: "Hverken for eller imod"
    }
    vote_url = base_url + str(member)
    votes = requests.get(vote_url).content
    # print(votes)
    votes_json = json.loads(votes)
    return print(votes_json)

get_votes(158)
