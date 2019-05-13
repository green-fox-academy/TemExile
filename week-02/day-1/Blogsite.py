class BlogPost(object):
    def __init__(self, author_name, title, text, publication_date):
        self.author_name = author_name
        self.title = title
        self.text = text
        self.publication_date = publication_date

exp1 = BlogPost('John Doe', 'Lorem Ipsum', 'Lorem iposum dolor sit amet.',
                '2000.05.04')
exp2 = BlogPost('Tim Urban', 'Wait but why',
                'A popular long-form, stick-figure-illustrated blog about almost everything.',
                '2010.10.10')

class Blog(object):
    def __init__(self, list):
        self.list = list
    def adding(self, post):
        self.list.append(post)
    def deleted(self, index):
        self.list.pop(index)
    def updated(self, index, newpost):
        self.list.insert(index, newpost)

b = [exp1, exp2]
c = Blog(b)
c.adding(BlogPost('asdf','1111','444','1223'))
print(c.list)
c.deleted(2)
print(c.list)
c.updated(2,BlogPost('abcc','cdwe','444','1235'))
print(c.list)