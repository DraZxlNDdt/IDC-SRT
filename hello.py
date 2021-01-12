import flask as F
from sqlalchemy import Column, String, Integer, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import SingletonThreadPool

app = F.Flask(__name__)

engine = None
session = None
results = None
facename = None
face = None
name = None
intro = None

@app.route('/', methods=['GET'])
def index_get():
    pp = 5
    content = {
        'a': 5,
        'b': {
            'c': 5
        }
    }
    return F.render_template('index.html', **content, dd=pp)


@app.route('/2', methods=['GET'])
def index2_get():

    return F.render_template('index2.html')


@app.route('/schedule', methods=['GET'])
def schedule_get():
    return F.render_template('schedule.html')


@app.route('/guest', methods=['GET'])
def quest_get():
    pp = 5
    content = {
        'a': 5,
        'b': {
            'c': 5
        }
    }
    return F.render_template('guest.html', **content, dd=pp)


@app.route('/team', methods=['GET'])
def team_get():
    global engine, session, results, facename, face, name, intro
    session = Session()
    if session:
        name = list(map(lambda x: x[0],session.query(face_info.name).all()))
        intro = list(map(lambda x: x[0],session.query(face_info.introduction).all()))
        face = list(map(lambda x: x[0], session.query(face_info.face).all()))
    session.commit()
    session.close()
    return F.render_template('team.html', name=name, introduction=intro, face=face)


@app.route('/h', methods=['GET'])
def gg():
    id = F.request.args.get("id")
    return "id is %s " % id


Entity = declarative_base()
engine = create_engine('sqlite:///data.db', poolclass=SingletonThreadPool,
                       connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)


class face_info(Entity):
    # 表名
    __tablename__ = 'face_info'
    # 定义字段
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    face = Column(String, primary_key=False)
    introduction = Column(String, primary_key=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Entity.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7032, debug=True)