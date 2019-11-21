from core.utils import log


# object serving as room during auction, with several properties
class AuctionHouse:
    # general class attributes:
    # ------------------------------------------------------------------------

    def __repr__(self):
        return str(self.players)

    # initializer of class
    def __init__(self):

        # empty dictionary object to store responses from players
        self.players = {}

        self.admin = ''

    def add_player(self, id_, name):
        # set first user as admin
        if not self.players:
            self.admin = id_

        self.players[id_] = name
        log.info("joined [%s] as [%s]" % (id_, name))

    def check_if_in(self, id_):
        return id_ in self.players

    def get_name(self, id_):
        try:
            return self.players[id_]
        except KeyError as e:
            print(e)
            log.error(e)
            return "ERROR"
