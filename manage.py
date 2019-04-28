# manage.py

import os
from flask_script import Manager # class for handling a set of commands
from app import create_app
from app import models


app = create_app(config_name=os.getenv('APP_SETTINGS'))
manager = Manager(app)



if __name__ == '__main__':
    manager.run()
