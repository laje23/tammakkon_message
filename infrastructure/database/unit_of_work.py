from infrastructure.database.base import sessionlocal, BaseModel, engine
from infrastructure.database.repository import *
from domain.exeptions import DataBaseError
from domain.interfaces import IUnitOfWork


class UnitOfWork(IUnitOfWork):

    def __init__(self):
        BaseModel.metadata.create_all(bind=engine)

    def __enter__(self):
        self.session = sessionlocal()

        return self

    def get_repository(self, entity_type: type):
        return getattr(self, entity_type.__name__)

    @property
    def User(self):
        if self.session:
            self._users = UserRepository(self.session)

        return self._users

    @property
    def Role(self) -> RoleRepository:
        if self.session:
            self._role = RoleRepository(self.session)

        return self._role

    @property
    def BotAccount(self) -> BotAccountRepository:
        if self.session:
            self._bot_account = BotAccountRepository(self.session)

        return self._bot_account

    @property
    def Destination(self) -> DestinationRepository:
        if self.session:
            self._destination = DestinationRepository(self.session)

        return self._destination

    @property
    def log(self) -> LogRepository:
        if self.session:
            self._log = LogRepository(self.session)

        return self._log

    @property
    def Message(self) -> MessageRepository:
        if self.session:
            self._message = MessageRepository(self.session)

        return self._message

    @property
    def Media(self) -> MediaRepository:
        if self.session:
            self._media = MediaRepository(self.session)

        return self._media

    @property
    def UserAccount(self) -> UserAccountRepository:
        if self.session:
            self._user_account = UserAccountRepository(self.session)

        return self._user_account

    @property
    def MessageTarget(self) -> MessageTargetRepository:
        if self.session:
            self._message_target = MessageTargetRepository(self.session)

        return self._message_target

    def __exit__(self, exc_type, exc_value, traceback):
        if self.session:
            if exc_type is not None:
                self.session.rollback()
                print(exc_value)
                print(traceback)
                print(exc_type)
                raise DataBaseError(
                    exc_value,
                    traceback,
                )
            else:
                self.session.commit()

            self.session.close()

            self.session = None
            self.users = None
