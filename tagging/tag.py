

from db import get_database

chychoVault = get_database()
posts = chychoVault["posts2"]

privacy =  ("""Whispering WikiLeaks' Vault 7 "Year Zero": CIA Hacking Tools Revealed""",
            "NSA’s Desperation for Secrecy Leads to Stupidity, Alienating the Hacker Community: ‘Freedom Downtime’, a Call to Arms",
            "The Irony and the Hypocrisy, the U.S. Department of Defense Is Using Blackberry for Its Privacy",
            "How to Protect Ourselves on Social Networks and from Data Collection Systems of Governments and Corporations",
            "The Surveillance State Killed BlackBerry, and the Same Fate Awaits Other Tech Giants",
            "Why the U.S. Government has such a hard-on for Edward Snowden",
            "Anomalies, Prisons, and Geophysics: How Governments Use Data and How to Stop Them",
            "So let me get this straight, we fast track renditions but hunt down whistleblowers on presidential planes!",
            "Bradley Manning and the trial of the United States Military",
            "A Candid Speaker and Three Hypocrites address the 67th session of the United Nations General Assembly ")


for title in privacy:
    posts.find_one_and_update({'title': {"$regex": title}},{'$push':{'tag':["popular"]}})