from db import get_database

chychoVault = get_database()
posts = chychoVault["posts2"]

#posts.find_one_and_update({'title': 'About Page'},{'$set': {'tag': 'about'}})


#posts.find_one_and_update({ 'title': 'Mathematics: Finding What You Need'},{'$set': {'tag': 'math'}})
#posts.find_one_and_update({'title': "Math in Real Life: Table of Contents"},{'$set': {'tag':'real_math'}})
#posts.find_one_and_update({'title': "ASMR Math: Introduction and Table of Contents "},{'$set': {'tag':'asmr_math'}})
#posts.find_one_and_update({'title': "All About Comic Books: Readings, Reviews and Recommendations, Comic Book Hauls, Framings, Collections and Articles"},{'$set': {'tag':'comic'}})