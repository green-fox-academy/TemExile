class book(object):
    def __init__(self, author, title, release_year):
        self.author = author
        self.title = title
        self.release_year = release_year
    def toString(self):
        return f'{self.author}: {self.title}({self.release_year})'

class bookshelf(object):
    def __init__(self, booklist = []):
        self.booklist = booklist
        self.bookdic = {}
        self.mostbook = ''
        self.earliestbook = ''
        self.latestbook = ''
    def addbook(self, newbook):
        if newbook.author not in self.bookdic:
            self.bookdic[newbook.author] = [[newbook.title, newbook.release_year]]
            self.booklist.append([newbook.author, newbook.title, newbook.release_year])
        elif newbook.author in self.bookdic:
            self.bookdic[newbook.authro].append([newbook.title, newbook.release_year])
            self.booklist.append([newbook.author, newbook.title, newbook.release_year])
    def removebook(self, oldbook):
        self.booklist.remove([oldbook.author, oldbook.title, oldbook.release_year])
        self.bookdic[oldbook.author].remove([oldbook.title, oldbook.release_yeaer])
    def favouriteAuthor(self):
        authordic = {}
        for name in self.bookdic:
            authordic[name] = len(name)
        self.mostbook = max(authordic)
        return self.mostbook
    def earliestPublished(self):
        early_year = []
        for book in self.booklist:
            early_year.append(book[2])
        year = min(early_year)
        self.earliestbook = self.booklist[year][1]
        return self.earliestbook
    def latestPublished(self):
        late_year = []
        for book in self.booklist:
            late_year.append(book[2])
        year = max(late_year)
        self.latestbook = self.booklist[year][1]
        return self.latestbook
    def toString(self):
        return (f'There are {len(self.booklist)} books, '
        f'the earliest published book is {self.earliestbook}, ' 
        f'the latest published book is {self.latestbook}, '
        f'and the favouriate author is {self.mostbook}')