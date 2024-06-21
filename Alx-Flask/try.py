from flaskblog import app, db
from flaskblog.models import User, Post

with app.app_context():
    # Add a user to the session
    #user_1 = User(username='John', email='john@example.com', password='123456')
    #db.session.add(user_1)
    #db.session.commit()
    #user1=User.query.all()
    #user1=User.query.filter_by(username="ahmed").first()
    #print(user1)
    #post=Post(title="second", content="Blog1", author=user1)
    #db.session.add(post)
    #db.session.commit()
    post1=Post.query.all()
    #db.session.delete(post1)
    #db.session.commit()
    print(post1)
    #db.session.delete(user)
    #db.session.commit()
    #user=User.query.all()
    #print(user)