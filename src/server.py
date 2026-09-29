from flask import Flask, render_template, request.args


app = Flask(__name__)


# the function to call if the user call "/"

@app.route("/")
def hello_world():
    global names 
    return render_template('index.html')


@app.route('/catch', methods=['POST'])
  def catch():
    global names
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name) 



# how to add catch 