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