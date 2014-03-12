__author__ = 'pepo'
from flask import render_template
from app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<int:page>', methods=['GET', 'POST'])
def index():
    mainmenu = [{'name': 'linux'}, {'name': 'aktuell'}, {'name': 'hw-projects'}, {'name': 'link4'}]
    return render_template('index.html',
        mainmenu = mainmenu,
        title = 'Home',
        form = 'form',
        posts = 'posts')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    next = request.args.get('next')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        if authenticate(app.config['AUTH_SERVER'], username, password):
            user = User.query.filter_by(username=username).first()
            if user:
                if login_user(DbUser(user)):
                    # do stuff
                    flash("You have logged in")

                    return redirect(next or url_for('index', error=error))
        error = "Login failed"
    return render_template('login.html', login=True, next=next, error=error)