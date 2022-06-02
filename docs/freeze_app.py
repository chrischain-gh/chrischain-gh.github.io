from flask_frozen import Freezer
from app import app

freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = '/Users/chris/Documents/Python_Projects/Projects/chrischain-gh.github.io/docs'
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
app.config['FREEZER_RELATIVE_URLS'] = True

if __name__ == '__main__':
    freezer.freeze()