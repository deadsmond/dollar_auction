from flask import Flask, render_template, request
from core.analyser import Analyser


# define application
app = Flask(__name__, template_folder='.')
app.config["DEBUG"] = True

# define agent
Analyser = Analyser()


# address for analysis
@app.route('/', methods=['GET', 'POST'])
def webpage():

    # default values
    endpoint = "Illuminati"
    depth = 3

    # if it is POSTed form:
    if request.method == 'POST':

        # validate input
        input = request.form['search']
        if len(input) in range(1, 30):
            endpoint = input

        try:
            if int(request.form['depth']) in range(1, 11):
                depth = int(request.form['depth'])
        except ValueError:
            pass

    [messages, error] = Analyser.analysis_results(endpoint, depth)
    return render_template('index.html', messages = messages, error = error)


# address for checkpoint
@app.route('/checkpoint', methods=['GET'])
def checkpoint():
    return "Server is not down"
