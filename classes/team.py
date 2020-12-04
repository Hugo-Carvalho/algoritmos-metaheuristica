class Team(object):
    def __init__(self, name, aptitude, match, binary, ids):
        self.name = name
        self.aptitude = aptitude
        self.match = match
        self.binary = binary
        self.ids = ids

    def __str__(self):
        return self.name

    def get_aptitude(self):
        return self.aptitude

    def get_match(self):
        return self.match

    def get_binary(self):
        return self.binary

    def get_ids(self):
        return self.ids

    def ratio(self):
        return (self.aptitude)/(self.match)

class TeamBest(object):
    def __init__(self, name, aptitude, match, binary):
        self.name = name
        self.aptitude = aptitude
        self.match = match
        self.binary = binary

    def get_aptitude(self):
        return self.aptitude

    def get_match(self):
        return self.match

    def get_binary(self):
        return self.binary