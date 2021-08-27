import os
BASE_DIR=os.path.dirname(__file__)

#SQL database address
SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
#do not add this feature, soon wiil be removed 
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY="dev"
