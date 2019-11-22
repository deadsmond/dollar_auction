from core.utils import log
from flask import Flask, render_template, request, redirect, url_for
from core.auction_house import AuctionHouse


agent = None

# mark new run in logfile
log.info("Defining flask application")

# define application
app = Flask(__name__, template_folder='templates')


# --------------------------------------------- ENDPOINTS ----------------------------------------------------------
# address for game logon
@app.route('/', methods=['GET', 'POST'])
def login():

    # check if login attempt or start page get
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # check if player has logged in
        id_ = request.remote_addr
        name = request.form['name']
        if not agent.check_if_in(id_):
            # add player
            agent.add_player(id_=id_, name=name)
        # join the server
        return redirect(url_for('auction'))

# auction house route
@app.route('/auction', methods=['GET', 'POST'])
def auction():
    id_ = request.remote_addr
    name = agent.get_name(request.remote_addr)
    admin_ = (request.remote_addr == agent.admin)

    if request.method == 'POST':
        agent.add_bid(id_, request.form['bid'])  # TODO: where is agent

    return render_template('index.html',
                           name=name,
                           admin=admin_,
                           players=agent.players,
                           results=agent.results
                           )

# address for checkpoint
@app.route('/checkpoint', methods=['GET'])
def checkpoint():
    return render_template('checkpoint.html')


if __name__ == '__main__':
    # --------------------------------------------- SCRIPT INIT --------------------------------------------------------
    # mark new run in logfile
    log.info("Starting new auction house -----------------------------------------------------------------------------")
    # define agent
    agent = AuctionHouse()
    # mark new run in logfile
    log.info("running server...")
    app.run(debug=False, ssl_context='adhoc')
