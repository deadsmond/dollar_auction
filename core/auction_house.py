from core.utils import log


# object serving as room during auction, with several properties
class AuctionHouse:
    # general class attributes:
    # ------------------------------------------------------------------------

    def __repr__(self):
        return str(self.players)

    # initializer of class
    def __init__(self):

        # empty list to store responses from players
        self.players = []

        # empty list to store results of previous games
        self.results = []

        # admin id
        self.admin = ''

    def add_player(self, id_, name):

        # set first user as admin
        if not self.players:
            self.admin = id_

        # add player to list
        self.players.append([id_, name, 0])

        log.info("joined [%s] as [%s]" % (id_, name))

    # iterate through list to check if id is in game
    def check_if_in(self, id_):
        for player in self.players:
            if player[0] == id_:
                return True
        return False

    # iterate through list to get the name of id
    def get_name(self, id_):
        try:
            for player in self.players:
                if player[0] == id_:
                    return player[1]
            raise KeyError
        except KeyError as e:
            print(e)
            log.error(e)
            return "ERROR"
