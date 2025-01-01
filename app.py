from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/account_links.html')
def account_links():
    return render_template('account_links.html')

@app.route('/ig_links.html')
def ig_links():
    return render_template('ig_links.html')

@app.route('/photography.html')
def photography():
    return render_template('photography.html')

@app.route('/video.html')
def video():
    return render_template('video.html')

@app.route('/resumes/resume_aviation.html')
def resume_aviation():
    return render_template('resumes/resume_aviation.html')

@app.route('/resumes/music_resume.html')
def music_resume():
    return render_template('resumes/music_resume.html')

@app.route('/python_projects/aircraft_mpg.html')
def aircraft_mpg():
    return render_template('python_projects/aircraft_mpg.html')

@app.route('/python_projects/regsearch.html')
def regsearch():
    return render_template('python_projects/regsearch.html')

@app.route('/python_projects/pyscript_test_aircraft_mpg.html')
def pyscript_test_aircraft_mpg():
    return render_template('python_projects/pyscript_test_aircraft_mpg.html')

@app.route('/aircraft_pipe_dreams.html')
def aircraft_pipe_dreams():
    return render_template('aircraft_pipe_dreams.html')

@app.route('/zenith_build_study.html')
def zenith_build_study():
    return render_template('zenith_build_study.html')

@app.route('/housing_studies/mortgage_planning.html')
def mortgage_planning():
    return render_template('housing_studies/mortgage_planning.html')

@app.route('/lancair_360_build/lancair_360_build_manual.html')
def lancair_360_build_manual():
    return render_template('lancair_360_build/lancair_360_build_manual.html')

@app.route('/lancair_legacy_build/lancair_legacy_build_manual.html')
def lancair_legacy_build_manual():
    return render_template('lancair_legacy_build/lancair_legacy_build_manual.html')

if __name__ == '__main__':
    app.run(debug=True)