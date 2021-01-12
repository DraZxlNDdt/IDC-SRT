from sqlalchemy import Column, String, Integer, Float, create_engine
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = None
session = None
results = None
facename = None
face = None
name = None

"""描述该功能...
"""
def do():
  global engine, session, results, facename, face, name
  session = Session()
  if session:
    results = session.query(face_info).filter(face_info.id==1).delete()
    session.add(face_info(id=1,  name="Jerry", face="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.mp.sohu.com%2Fq_mini%2Cc_zoom%2Cw_640%2Fupload%2F20170731%2F4c99710550954d8a8f65dce6bbe27370_th.jpg&refer=http%3A%2F%2Fimg.mp.sohu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1613006046&t=0816d820afd6f50e15f4d806963ce10c", introduction="An orange mouse"))
    results = session.query(face_info).filter(face_info.id==2).delete()
    session.add(face_info(id=2,  name="Tom", face="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1606972096128&di=ce04cf178e4d14b7cebd371a8756b493&imgtype=0&src=http%3A%2F%2Fgss0.baidu.com%2F94o3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F6a63f6246b600c339761c419104c510fd8f9a1c2.jpg", introduction="A blue cat"))
    # results = session.query(face_info).fliter(face_info.id==3).delete()
    # facename = list(map(lambda x: x[0],session.query(face_info.name).all()))
    # face = list(map(lambda x: x[0],session.query(face_info.face).all()))
    # print(facename)

    session.commit()
    session.close()


Entity = declarative_base()
engine = create_engine('sqlite:///data.db', poolclass=SingletonThreadPool, connect_args={'check_same_thread': False})
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

do()