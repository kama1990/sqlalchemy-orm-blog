import fake as fake
from faker import Faker

from session import session
from models import Author, Article


def main():
    author = session.query(Author).get(10)

    fake = Faker()
    article = Article(
        title=fake.sentence(),  # dodaje nam fake title - dla podanego autora w get
        content="New article content"
    )

    author.articles.append(article)
    session.commit()  # bez session commit nie zadziała


if __name__ == "__main__":
    main()