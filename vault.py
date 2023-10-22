from chycho.db import get_database
from bson.objectid import ObjectId

class postRepository:

    def getPosts(self):
        chychoVault = get_database()
        posts = chychoVault["posts3"]
        posts_dicts = posts.find()

        all_posts = []
        for post in posts_dicts:
            all_posts.append(post)

        return all_posts

    def getPostByTitle(self,title):
        chychoVault = get_database()
        posts = chychoVault["posts3"]

        return posts.find_one({"title": title})

    def getPostById(self,id):
        chychoVault = get_database()
        posts = chychoVault["posts3"]
        
        return posts.find_one({"_id": ObjectId(id)})

    def getPostByTag(self,tag):
        chychoVault = get_database()
        posts = chychoVault["posts3"]
        
        return posts.find_one({"tag": tag})

    def searchPostsByTag(self,tag):
        chychoVault = get_database()
        posts = chychoVault["posts3"]
        
        posts = posts.find({"tag": tag})
        post_list = []
        for post in posts:
            post_list.append(post)
            print(post['title'])

        return post_list

    def searchPostsByType(self,type):
        chychoVault = get_database()
        posts = chychoVault["posts3"]
        
        posts = posts.find({"type": type})
        post_list = []
        for post in posts:
            post_list.append(post)
            print(post['title'])

        return post_list

    def searchPosts(self, search_query):
        chychoVault = get_database()
        posts = chychoVault["posts3"]

        query = {"title": { "$regex": search_query, "$options": 'i'}}

        search_results = posts.find(query)
        queried_posts = []
        for post in search_results:
            queried_posts.append(post)
            print(post['title'])

        return queried_posts
    
    def updatePost(self, id, editedPost, tag):
        chychoVault = get_database()
        posts = chychoVault["posts3"]

        if tag != "":
            print(tag)
            posts.find_one_and_update({'_id': ObjectId(id)},{'$push': {'tag': tag}})

        posts.update_one({'_id': ObjectId(id)},{"$set": {'body': editedPost}})
