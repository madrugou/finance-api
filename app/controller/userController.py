from ..database.connection import Session
from ..model.user import User
from loguru import logger
import bcrypt


class UserController:

    def __init__(self):
        pass

    @staticmethod
    def create_hash_password(password):
        password = password.encode("utf-8")
        password_hash = bcrypt.hashpw(password, bcrypt.gensalt())

        return password_hash

    def check_hash_password(self, password):
        check = password.encode("utf-8")
        if bcrypt.checkpw(check, self.create_hash_password(password)):
            logger.success("Login success")
        else:
            logger.error("Incorrect password")

    def change_password(self, old_password, new_password):
        """
        Verificar se a senha antiga bate com a senha do banco, se sim, altero para a senha nova

        :return:
        """
        pass

    @staticmethod
    def read_users():
        session = Session()
        users = session.query(User).order_by(User.name_user).all()
        session.close()
        return users

    @staticmethod
    def read_user_by_id(cd_user):
        session = Session()
        user = session.query(User).filter(User.cd_user == int(cd_user)).first()
        session.close()

        return user

    def create_user(self, new_user):
        user = User(new_user.name_user, new_user.email_user, self.create_hash_password(new_user.password))
        session = Session()
        session.add(user)
        session.commit()
        session.close()

    @staticmethod
    def update_user(update_user):
        session = Session()
        user = session.query(User).filter(User.cd_user == int(update_user.cd_user)).first()
        if user is not None:
            user.name_user = update_user.name_user
            user.email_user = update_user.email_user
            session.commit()
            session.refresh(user)
        session.close()

    def delete_user(self, delete_user):
        session = Session()
        user = self.read_user_by_id(delete_user.cd_user)
        if user is not None:
            session.delete(user)
            session.commit()
        session.close()
