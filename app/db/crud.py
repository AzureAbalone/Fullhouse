from app.db.database import session, User


def create(name: str, password: str):
    user = User(name=name, password=password)
    session.add(user)
    session.commit()


def read():
    users = session.query(User).all()
    for u in users:
        print(u.name, u.password)


def update():
    user = session.query(User).filter(User.id == 1).first()
    user.password = "abc123"
    session.commit()


def delete(name: str, password: str):
    user = session.query(User).filter(User.name == name).first()
    session.delete(user)
    session.commit()
