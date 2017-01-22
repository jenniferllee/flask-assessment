from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/application-form')
def show_form():
    jobs = ['Software Engineer', 'QA Engineer', 'Product Manager']
    return render_template("application-form.html",
                           jobs=jobs)


@app.route('/application-success', methods=["POST"])
def application_response():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    position = request.form.get("job")
    salary = float(request.form.get("salary"))
    salary = "${:,.2f}".format(salary)

    return render_template("application-response.html",
                           firstname=firstname,
                           lastname=lastname,
                           position=position,
                           salary=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
