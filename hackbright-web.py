from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""
    
    return render_template("student_search.html")


###########################

@app.route("/student-add-form")
def student_add_form():
    """Show the page with the form to add a student"""

    return render_template("student_add.html")


@app.route("/process-student-add", methods=['POST'])
def process_student_add():
    """Add a student."""

    first = request.form.get('fname')
    print first
    last = request.form.get('lname')
    github = request.form.get('github')
    first, last, github = hackbright.make_new_student(first,last,github)

    return render_template("student_added.html", 
                            first=first,
                            last=last,
                            github=github)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template ("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html
    # return "%s is the GitHub account for %s %s" % (github, first, last)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
