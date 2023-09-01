#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review, User

if __name__ == '__main__':
    engine = create_engine('sqlite:///many_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # import ipdb; ipdb.set_trace()

    # game1 = Game(title="title", genre="genre", platform="platformmer", price=12)
    # print(game1)
    # session.add(game1)
    # session.commit()

    # game11 = session.query(Game).filter(Game.id == 12).first()
    # print(game11)
    # session.delete(game11)
    # session.commit()

    # user_review = session.query(Review).filter(Review.id == 2).first()
    # print(user_review)
    # print(user_review.game)
    # print(user_review.user)
    #
    # new_review = Review(score=4,comment="mamamia, here we go again!", game_id = 10, user_id = 4)
    # session.add(new_review)
    # session.commit()

    game10 = session.query(Game).filter(Game.id == 10).first()
    session.commit()
    print(game10.users)

    user4 = session.query(User).filter(User.id == 4).first()
    print(user4)

    game10.users.append(user4)
    session.commit()
    print(game10.users)



