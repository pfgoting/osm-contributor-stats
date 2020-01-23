import os
import requests, pdb
from pathlib import Path
import OsmApi
import OsmContributorStats

# Instantiate
osmApi = OsmApi.OsmApi(debug=0)
fpath = Path(os.path.dirname(os.path.abspath(__file__)))
rep = fpath / 'test2'
print(rep)

# Create dir
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
users[0] = ["",]
users[1] = [""]

# Step 1 - Extract History Data  - Extraire les données historiques
frm_dte = "2019-12-11"
to_dte = "2019-12-13"
# min_lat=6.64
# min_lon=124.62
# max_lat=7.12
# max_lon=125.42
min_lat=7.27
min_lon=121.60
max_lat=12.39
max_lon=126.72
# Tag to search
comment_filter = ["#hotosm-project-6212", "#UPNOAH"]
# comment_filter = ["hotosm-project-6734","hotph"] #"#hotph" #hotosm-project-6734
# comment_filter =  "hotosm-project-6734"#"hotosm-project-7147"

ContributorStats.API6_Collect_Changesets(team_from=0, team_to=0, from_date=frm_dte,
                                         to_date=to_dte,
                                         min_lon=min_lon, max_lon=max_lon, min_lat=min_lat, max_lat=max_lat,
                                         prefix="osmef-togo-", users=users, comment_filter=comment_filter)


# Step 2 - Statistics from data stored locally	- Statistiques produite à partir des données enregistrées localement
ContributorStats.Changesets_Contributor_Statistics(team_from=0, team_to=0, from_date=frm_dte,
                                                   to_date=to_dte,
                                                   min_lon=min_lon, max_lon=max_lon, min_lat=min_lat, max_lat=max_lat,
                                                   prefix="osmef-togo-", users=users)


print("\n-----------------------------------------------------")

ContributorStats.__del__()
del OsmContributorStats

import sys
sys.exit('\n=== Extraction complete ===')
