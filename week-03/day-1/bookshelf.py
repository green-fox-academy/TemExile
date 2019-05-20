class book(object):
    def __init__(self, author, title, release_year, b_type, page):
        self.author = author
        self.title = title
        self.release_year = release_year
        self.b_type = b_type
        self.page = page
    def toString(self):
        return f'{self.author}: {self.title}({self.release_year})'
    def weight(self):
        if self.b_type == 'Hardcover':
            w = 100 + self.page * 10
            return w
        elif self.b_type == 'Paperback':
            w = 20 + self.page * 10
            return w

class bookshelf(object):
    def __init__(self, booklist = []):
        self.booklist = []
        self.bookdic = {}
        self.lightest = ''
        self.mostpage = ''

    def addbook(self, newbook):
        if newbook.author not in self.bookdic:
            self.bookdic[newbook.author] = [[newbook.title, newbook.release_year,
            newbook.page, newbook.weight()]]
            self.booklist.append([newbook.author, newbook.title, newbook.release_year,
            newbook.page, newbook.weight()])
        elif newbook.author in self.bookdic:
            self.bookdic[newbook.authro].append([newbook.title, newbook.release_year,
            newbook.page, newbook.weight()])
            self.booklist.append([newbook.author, newbook.title, newbook.release_year,
            newbook.page, newbook.weight()])

    def lightestbook(self):
        lightlist = []
        for line in self.booklist:
            lightlist.append(line[4])
        lgt = lightlist.index(min(lightlist))
        self.lightest = self.booklist[lgt][0]
        return self.lightest
    
    def themost(self):
        pagedic = {}
        for name in self.bookdic.keys():
            totalpage = 0
            for line in self.bookdic[name]:
                totalpage += line[2]
            pagedic[name] = totalpage
    



