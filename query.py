from db import get_database
dbname = get_database()
 
posts1 = dbname["posts1"]

post_details = posts1.find()
for post in post_details:
   print(post)