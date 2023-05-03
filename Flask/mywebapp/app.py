from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/admin')
def admin_page():
    return 'welcome to the admin page'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/admin/<admin>')
def hello_guest(admin):
    return 'welcome to the admin page'

if __name__ == '__main__':
    app.run()