

class Analyser:
    # general class attributes:
    # ------------------------------------------------------------------------
    # initializer of class
    def __init__(self):
        # pattern: Uppercase, then anything that is not in (.!?), then one of (.!?)
        self.pattern_regex = ""

        # empty collection object to store responses from analysis
        self.collection = []
