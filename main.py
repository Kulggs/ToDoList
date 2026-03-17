
class ToDo:
    def __init__(self, title):
        self.title = title
        self._done = False

    def done(self):
        self._done = True

    def is_done(self):
        return self._done

