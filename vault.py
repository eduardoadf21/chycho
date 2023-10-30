from chycho.db import get_database
import pymongo
from bson.objectid import ObjectId
import datetime

class postRepository:

    def getPosts(self):
        chychoVault = get_database()
        posts = chychoVault["posts6"]
        posts_dicts = posts.find().sort('date',pymongo.DESCENDING)

        all_posts = []
        for post in posts_dicts:
            all_posts.append(post)

        return all_posts

    def getPostByTitle(self,title):
        chychoVault = get_database()
        posts = chychoVault["posts6"]

        return posts.find_one({"title": title})

    def getPostById(self,id):
        chychoVault = get_database()
        posts = chychoVault["posts6"]
        
        return posts.find_one({"_id": ObjectId(id)})

    def getPostByTag(self,tag):
        chychoVault = get_database()
        posts = chychoVault["posts6"]
        
        return posts.find_one({"tag": tag})

    def searchPostsByTag(self,tag):
        chychoVault = get_database()
        posts = chychoVault["posts6"]
        
        posts = posts.find({"tag": tag}).sort('date',pymongo.DESCENDING)

        post_list = []
        for post in posts:
            post_list.append(post)
            #print(post['title'])

        return post_list

    def searchPostsByType(self,type):
        chychoVault = get_database()
        posts = chychoVault["posts6"]
        
        posts = posts.find({"type": type})
        post_list = []
        for post in posts:
            post_list.append(post)
            #print(post['title'])

        return post_list

    def searchPosts(self, search_query):
        chychoVault = get_database()
        posts = chychoVault["posts6"]

        query = {"title": { "$regex": search_query, "$options": 'i'}}

        search_results = posts.find(query)
        queried_posts = []
        for post in search_results:
            queried_posts.append(post)
            #print(post['title'])

        return queried_posts
    
    def updatePost(self, id, editedPost, tag, tags):
        chychoVault = get_database()
        posts = chychoVault["posts6"]

        if tag != "":
            #print(tag)
            posts.find_one_and_update({'_id': ObjectId(id)},{'$push': {'tag': tag}})
        if len(tags)>0:
           for tag in tags:
                posts.find_one_and_update({'_id': ObjectId(id)},{'$push': {'tag': tag}})

        posts.update_one({'_id': ObjectId(id)},{"$set": {'body': editedPost}})

    def newPost(self, title, body, tag, tags):
        chychoVault = get_database()
        posts = chychoVault["posts6"]
        post = {}
        post['title'] = title
        post['author'] = "chycho"
        post['body'] = body
        post['tag'] = []
        tags.append(tag)
        post['tag'] = tags
        print(post['tag'])
        post['date'] = datetime.datetime.now()

        posts.insert_one(post)
    
    def deletePost(self,id):
        chychoVault = get_database()
        posts = chychoVault["posts6"]

        posts.delete_one({"_id": ObjectId(id)})

class userRepository:
    def getUser(self,username,password):
        chychoVault = get_database()
        users = chychoVault["users"]
        return users.find_one({"$and": [{'name':username},{'password':password}]})

    def getUserById(self,id):
        chychoVault = get_database()
        users = chychoVault["users"]
        return users.find_one({"id": id})