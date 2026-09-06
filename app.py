from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "college_placement_secret"

# Temporary application storage
applications = []

# Temporary profile storage
profile_data = {}


# ---------------- HOME / DASHBOARD ----------------

@app.route("/")
def home():

    # If user is not logged in, show login page
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:

            # Store login information
            session["username"] = username

            # Open dashboard after successful login
            return redirect(url_for("home"))

        return "<h2>Please enter username and password.</h2>"

    return render_template("login.html")


# ---------------- PLACEMENT ----------------

@app.route("/placement")
def placement():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("placements.html")


# ---------------- INTERNSHIP ----------------

@app.route("/internship")
def internship():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("internships.html")


# ---------------- INTERNSHIP APPLICATION FORM ----------------

@app.route("/apply_internship")
def apply_internship():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("apply_internship.html")


# ---------------- SUBMIT INTERNSHIP APPLICATION ----------------

@app.route("/submit_internship", methods=["POST"])
def submit_internship():

    if "username" not in session:
        return redirect(url_for("login"))

    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    college = request.form.get("college")
    department = request.form.get("department")
    cgpa = request.form.get("cgpa")
    skills = request.form.get("skills")

    application = {
        "type": "Internship",
        "name": name,
        "email": email,
        "phone": phone,
        "college": college,
        "department": department,
        "cgpa": cgpa,
        "skills": skills,
        "company": "Internship Opportunity",
        "role": "Intern",
        "status": "Submitted"
    }

    applications.append(application)

    return redirect(url_for("applications_page"))


# ---------------- PLACEMENT APPLICATION FORM ----------------

@app.route("/apply_placement")
def apply_placement():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("apply_placement.html")


# ---------------- SUBMIT PLACEMENT APPLICATION ----------------

@app.route("/submit_placement", methods=["POST"])
def submit_placement():

    if "username" not in session:
        return redirect(url_for("login"))

    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    college = request.form.get("college")
    department = request.form.get("department")
    cgpa = request.form.get("cgpa")
    skills = request.form.get("skills")

    application = {
        "type": "Placement",
        "name": name,
        "email": email,
        "phone": phone,
        "college": college,
        "department": department,
        "cgpa": cgpa,
        "skills": skills,
        "company": "Placement Opportunity",
        "role": "Software / Engineering Role",
        "status": "Submitted"
    }

    applications.append(application)

    return redirect(url_for("applications_page"))


# ---------------- MY APPLICATIONS ----------------

@app.route("/applications")
def applications_page():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "applications.html",
        applications=applications
    )


# ---------------- MY PROFILE ----------------

@app.route("/profile", methods=["GET", "POST"])
def profile():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        profile_data["name"] = request.form.get("name")
        profile_data["email"] = request.form.get("email")
        profile_data["phone"] = request.form.get("phone")
        profile_data["college"] = request.form.get("college")
        profile_data["department"] = request.form.get("department")
        profile_data["year"] = request.form.get("year")
        profile_data["roll_number"] = request.form.get("roll_number")
        profile_data["skills"] = request.form.get("skills")

        return render_template(
            "profile.html",
            profile=profile_data,
            message="Profile saved successfully!"
        )

    return render_template(
        "profile.html",
        profile=profile_data
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=False,use_reloader=False)
