from core.utils import log


# object serving as room during auction, with several properties
class AuctionHouse:
    # general class attributes:
    # ------------------------------------------------------------------------------------------------------------------

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

    # ----------------- PLAYER SUPPORT ---------------------------------------------------------------------------------
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
        log.error("check_if_in: could not find [%s] on list" % id_)
        return False

    # iterate through list to get the name of id
    def get_name(self, id_):
        try:
            for player in self.players:
                if player[0] == id_:
                    return player[1]
            log.error("get_name: could not find [%s] on list" % id_)
            raise KeyError
        except KeyError as e:
            log.error(e)
            return "ERROR"

    # ----------------- GAME MAINTENANCE -------------------------------------------------------------------------------
    def add_bid(self, id_, bid):
        for player in self.players:
            if player[0] == id_:
                if player[2] < bid:
                    player[2] = bid
                    log.info("[%s][%s] changed bid from %s to %s" %
                             (player[0], player[1], player[2], bid))
                    yield
                else:
                    log.warning("[%s][%s] tried to bid from %s to %s. Not cool, bro. Not cool." %
                                (player[0], player[1], player[2], bid))
                    yield
        log.error("add_bid: could not find [%s] on list" % id_)
