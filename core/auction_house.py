from core.utils import log


# object serving as room during auction, with several properties
class AuctionHouse:
    # general class attributes:
    # ------------------------------------------------------------------------
    # initializer of class
    def __init__(self, args):
        # store init arguments
        self.args = args

        # empty dictionary object to store responses from players
        self.properties = {
            "players": [

            ]
        }

    def add_player(self, payload):
        try:
            if \
                    payload['id'] and \
                    payload['nick'] and \
                    payload['id'] not in self.properties['players']:

                self.properties['players'][payload['id']] = payload['nick']
                return "login of player %s successful" % payload['nick']
            else:
                return "login of player %s was not successful" % payload['nick']
        except Exception as e:
            log.error(e)
            return e
