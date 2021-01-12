import flask as F
from flask import render_template,request,Flask
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

@app.route('/register', methods=['GET'])
def register_get():
    return F.render_template('register.html')

@app.route('/signup', methods=['GET'])
def signup_get():
    return F.render_template('signup.html')

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

@app.route('/gradesin',methods=['POST', 'GET'])
def gradesinp():
    formid = request.args.get('formid')
    session = Session()
    if session:
        if formid == '1':
            num = request.args.get('num')
            team1 = request.args.get('team1')
            grade1 = request.args.get('grade1')
            team2 = request.args.get('team2')
            grade2 = request.args.get('grade2')
            delete_game = session.query(grade_info).filter(grade_info.num == num).first()
            if delete_game:
                session.delete(delete_game)
                session.commit()
            grade = grade_info(num = num,team1 = team1,grade1 = grade1,team2 = team2,grade2 = grade2)
            session.add(grade)
            session.commit()
            session.close()
        if formid == '2':
            final1 =  request.args.get('final1')
            final2 =  request.args.get('final2')
            delete_game = session.query(grade_info).filter(grade_info.num == 7).first()
            if delete_game:
                session.delete(delete_game)
                session.commit()
            grade = grade_info(num = 7,team1 = final1,grade1 = 0,team2 = final2,grade2 = 0)
            session.add(grade)
            session.commit()
            session.close()
        if formid == '3':
            winner = request.args.get('winner')
            delete_game = session.query(grade_info).filter(grade_info.num == 8).first()
            if delete_game:
                session.delete(delete_game)
                session.commit()
            grade = grade_info(num = 8,team1 = winner,grade1 = 0,team2 = 'none',grade2 = 0)
            session.add(grade)
            session.commit()
            session.close()
    return F.render_template('grades_in.html')

@app.route('/gradesout',methods=['POST', 'GET'])
def gradesoutp():
    grade1 = ['?','?','?','?','?','?']
    grade2 = ['?','?','?','?','?','?']
    red = 0
    yellow = 0
    blue = 0
    green = 0
    session = Session()
    if session:
        for i in range(1,7):
            game = session.query(grade_info).filter(grade_info.num == i).first()
            if game:
                grade1[i-1] = game.grade1
                grade2[i-1] = game.grade2
        game1 = session.query(grade_info).filter(grade_info.num == 1).first()
        if game1:
            red = red + game1.grade1
            blue = blue + game1.grade2
        game2 = session.query(grade_info).filter(grade_info.num == 2).first()
        if game2:
            yellow = yellow + game2.grade1
            green = green + game2.grade2
        game3 = session.query(grade_info).filter(grade_info.num == 3).first()
        if game3:
            red = red + game3.grade1
            yellow = yellow + game3.grade2
        game4 = session.query(grade_info).filter(grade_info.num == 4).first()
        if game4:
            blue = blue + game4.grade1
            green = green + game4.grade2
        game5 = session.query(grade_info).filter(grade_info.num == 5).first()
        if game5:
            red = red + game5.grade1
            green = green + game5.grade2
        game6 = session.query(grade_info).filter(grade_info.num == 6).first()
        if game6:
            blue = blue + game6.grade1
            yellow = yellow + game6.grade2
        rank = [red,yellow,blue,green]
        rank.sort(reverse=True) #从大到小排序
        print(rank)
        r = [0,0,0,0]
        y = [0,0,0,0]
        n = ['?','?','?','?']
        j = 0
        final1 = '?'
        final2 = '?'
        winner = '?'
        for i in range(0,4):
            if rank[i] == red and y[0] == 0:
                r[j] = red
                n[j] = 'red'
                y[0] = 1
                j = j + 1
                continue
            if rank[i] == blue and y[1] == 0:
                r[j] = blue
                n[j] = 'blue'
                y[1] = 1
                j = j + 1
                continue
            if rank[i] == yellow and y[2] == 0:
                r[j] = yellow
                n[j] = 'yellow'
                y[2] = 1
                j = j + 1
                continue
            if rank[i] == green and y[3] == 0:
                r[j] = green
                n[j] = 'green'
                y[3] = 1
                j = j + 1
                continue

        game7 = session.query(grade_info).filter(grade_info.num == 7).first()
        if game7:
            final1 = game7.team1
            final2 = game7.team2
        game8 = session.query(grade_info).filter(grade_info.num == 8).first()
        if game8:
            winner = game8.team1
        session.close()
    return F.render_template('grades_out.html',g1 = grade1,g2 = grade2,r = r,n = n,final1 = final1,final2 = final2,winner = winner)

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
        
class grade_info(Entity):
  # 表名
  __tablename__ = 'grade_info'
  # 定义字段
  num = Column(Integer, primary_key=True)
  team1 = Column(String, primary_key=False)
  grade1 = Column(Integer, primary_key=False)
  team2 = Column(String, primary_key=False)
  grade2 = Column(Integer, primary_key=False)
  def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Entity.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7032, debug=True)