class PostIt(object):
    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color

exp1 = PostIt('orange', 'Idea 1', 'blue')
exp2 = PostIt('pink', 'Awesome', 'black')
exp3 = PostIt('yellow', 'Superb', 'green')

