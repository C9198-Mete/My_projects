from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world from Flask!!!"

@app.route("/second")
def second():
    return "Bize her yer Malatya!!!"

@app.route("/third/subthird")
def third():
    return "This page is the subpage of the third page"

@app.route("/forth/<string:id>")
def forth(id):
    return f'id number of this page is {id}'






if __name__== "__main__" :
    app.run(debug=True)