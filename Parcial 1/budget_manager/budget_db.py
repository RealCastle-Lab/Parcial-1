from models import Article, session

def add_article(name, description, price):
    new_article = Article(name=name, description=description, price=price)
    session.add(new_article)
    session.commit()

def get_article(article_id):
    return session.query(Article).filter(Article.id == article_id).first()

def update_article(article_id, name=None, description=None, price=None):
    article = session.query(Article).filter(Article.id == article_id).first()
    if article:
        if name:
            article.name = name
        if description:
            article.description = description
        if price:
            article.price = price
        session.commit()
        return True
    return False

def delete_article(article_id):
    article = session.query(Article).filter(Article.id == article_id).first()
    if article:
        session.delete(article)
        session.commit()
        return True
    return False
