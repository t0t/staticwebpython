from flask_frozen import Freezer
from app import app

# Create a Freezer instance with your app object and call its freeze() method.
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()