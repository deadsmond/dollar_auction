from core.utils import log
from argparse import ArgumentParser
from flask import Flask, render_template, request
from core.auction_house import AuctionHouse


agent = None

# mark new run in logfile
log.info("Defining flask application")

# define application
app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

# --------------------------------------------- ENDPOINTS ----------------------------------------------------------
# address for game logon
@app.route('/', methods=['GET', 'POST'])
def login():

    # check if login attempt or start page get
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # run validation in agent
        return render_template('index.html', messages=agent.add_player(request.form))

# auction house route
@app.route('/auction', methods=['GET', 'POST'])
def auction():
    return render_template('index.html', messages=agent.add_player(request.form))

# address for checkpoint
@app.route('/checkpoint', methods=['GET'])
def checkpoint():
    return "Server is not down"


if __name__ == '__main__':
    # --------------------------------------------- SCRIPT INIT --------------------------------------------------------
    # mark new run in logfile
    log.info("Starting new auction house -----------------------------------------------------------------------------")
    # parse arguments
    parser = ArgumentParser(description='Dollar auction hosting service:')
    # max
    parser.add_argument("-m", "--max", help="maximum number of players in one game.\n"
                                            "40 by default.",
                        default=40, required=False, type=int)
    # port
    parser.add_argument("-p", "--port", help="default port for service.\n"
                                             "8008 by default.",
                        default=8008, required=False, type=int)
    # value
    parser.add_argument("-v", "--value", help="default value of game.\n"
                                              "100 by default.",
                        default=100, required=False, type=int)

    args = parser.parse_args()

    # mark new run in logfile
    log.info("Defining auction house agent")
    # define agent
    agent = AuctionHouse(args)

    app.run(port=args.port)
