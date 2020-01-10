#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
#========================================================================="
# https://github.com/pierzen/osm-contributor-stats/blob/master/Script-to-run-OsmContributorStats-Module-Extract-Objects-Calculate-Statistics.py
# Pierre Beland, 10-2013
# Example running version 0.1 of OsmContributorStats
# OSM Contributors Histor Statistics, for a specific bbox zone and date range
# STATISTIQUES Historiques, contributeurs OSM pour une zone bbox et paire de dates
#========================================================================="
#========================================================================="
"""
import os
from pathlib import Path
# replace below with the directory where both OsmApi.py and OsmContributorStats.py are stored
# os.chdir('test')
import OsmApi
# Instantiation classe OsmApi
osmApi = OsmApi.OsmApi(debug=0)
import OsmContributorStats
# Instantiation classe OsmContributorStats
fpath = Path(os.path.dirname(os.path.abspath(__file__)))
rep = fpath / 'test'
print(rep)
ContributorStats = OsmContributorStats.OsmContributorStats(
    rep=rep, lang="en", debug=0)
dir(ContributorStats)

#===============================================================================
# users :  array of contributor ID's or Name by team - if no users, all users in the bbox will be selected
users = [None] * 2
users[0] = ["feyeandal","roger83"]
users[1] = [""]

"""
Example with nicknames
users=[None]*2
users[0] = ["abc","def","gjol"]
users[1] = ["zyx","avb Yul"]
"""


# Example - Lome, Togo
# The examples below defines a Bbox covering Lome, Togo. The period covered si from 2013-06-26 to 2013-06-27.

# Step 1 - Extract History Data  - Extraire les données historiques
frm_dte = "2019-12-11"
to_dte = "2019-12-12"
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
