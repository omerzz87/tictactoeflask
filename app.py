from flask import Flask , render_template

app = Flask(__name__)

@app.route("/yts")
def etsy():
    return render_template ('yts.html')

@app.route("/Ali")
def anime():
    return render_template ('Ali.html')

@app.route("/")
def home():
    return render_template ('index.html')
@app.route("/tictac")
def Tictactoe():
    return render_template ('Tictactoe.html')

if __name__ == "__main__":
    app.run(debug=True)