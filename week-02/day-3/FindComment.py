import json


def find_post(file):

    with open(file, encoding = 'utf-8', mode = 'r') as a:
        b = json.load(a)
    temp = 0
    for full_post in b:
        if full_post['comments'] is not None:
            x = full_post['comments']
            like_count = 0
            for comments in x:
                like_count += comments['like_count']
            if temp < like_count:
                temp = like_count
                poppost = full_post
    return poppost


print(find_post('posts.json'))

