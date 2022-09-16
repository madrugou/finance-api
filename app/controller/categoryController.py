from ..database.connection import Session
from ..model.category import Category


class CategoryController:

    def __init__(self):
        pass

    @staticmethod
    def read_categories():
        session = Session()
        categories = session.query(Category).order_by(Category.name_category).all()
        session.close()
        return categories

    @staticmethod
    def read_category_by_id(cd_category):
        session = Session()
        category = session.query(Category).filter(Category.cd_category == int(cd_category)).first()
        session.close()

        return category

    @staticmethod
    def create_category(new_category):
        category = Category(new_category.name_category)
        session = Session()
        session.add(category)
        session.commit()
        session.close()

    @staticmethod
    def update_category(update_category):
        session = Session()
        category = session.query(Category).filter(Category.cd_category == int(update_category.cd_category)).first()
        if category is not None:
            category.name_category = update_category.name_category
            session.commit()
            session.refresh(category)
        session.close()

    def delete_category(self, delete_category):
        session = Session()
        category = self.read_category_by_id(delete_category.cd_category)
        if category is not None:
            session.delete(category)
            session.commit()
        session.close()
