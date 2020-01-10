import os
import requests, pdb
from pathlib import Path
import OsmApi
import OsmContributorStats

# osmCha = {
#     "token": "3a9efa11ddd8ffd080ba96711cd5bd0d7faba114"
# }
# a = {"Authorization": "Token 3a9efa11ddd8ffd080ba96711cd5bd0d7faba114"}
# url = "https://osmcha.mapbox.com/api/v1/changesets/?date__gte=2019-12-11&date__lte=2019-12-13&comment=%23hotosm-project-6212"
# r = requests.get(url,headers=a)

# features = r.json()['features']
# print(features)

# url2 = "https://osmcha.mapbox.com/api/v1/changesets/78298803/"
# r = requests.get(url2,headers=a)
# f = r.json()

# url3 = " https://api.openstreetmap.org/api/0.6/changeset/78298803?include_discussion=true"
# z = requests.get(url3)
# print(z.content)
# pdb.set_trace()



# Instantiate
osmApi = OsmApi.OsmApi(debug=0)
fpath = Path(os.path.dirname(os.path.abspath(__file__)))
rep = fpath / 'test3'
print(rep)

# Create dir
print("TEST")
try:
    os.makedirs(rep)
except Exception as e:
    print(e)
    pass

ContributorStats = OsmContributorStats.OsmContributorStats(
    rep=rep, lang="en", debug=0)
# print(dir(ContributorStats))

# users :  array of contributor ID's or Name by team - if no users, all users in the bbox will be selected
users = [None] * 2
users[0] = ["feyeandal","roger83"]
users[1] = [""]

# Step 1 - Extract History Data  - Extraire les données historiques
frm_dte = "2019-12-1"
to_dte = "2019-12-31"
min_lat=4.22
max_lat=114.10
min_lon=21.32
max_lon=126.81

ContributorStats.API6_Collect_Changesets(team_from=0, team_to=0, from_date=frm_dte,
                                         to_date=to_dte,
                                         min_lon=min_lon, max_lon=max_lon, min_lat=min_lat, max_lat=max_lat,
                                         prefix="osmef-togo-", users=users)

# print("step 2")
# Step 2 - Statistics from data stored locally	- Statistiques produite à partir des données enregistrées localement
ContributorStats.Changesets_Contributor_Statistics(team_from=0, team_to=0, from_date=frm_dte,
                                                   to_date=to_dte,
                                                   min_lon=min_lon, max_lon=max_lon, min_lat=min_lat, max_lat=max_lat,
                                                   prefix="osmef-togo-", users=users)


print("\n-----------------------------------------------------")

ContributorStats.__del__()
del OsmContributorStats

import sys
sys.exit('\n=== Travail complété ===')
