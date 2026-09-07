from infrastructure.database.base import sessionlocal
from infrastructure.database.repository import *
from domain.exeptions import DataBaseError


class UnitOfWork:

    def __init__(self):
        self.users: UserRepository | None = None

    def __enter__(self):
        self.session = sessionlocal()

        return self

    def get_repository(self, entity_type: type):
        return getattr(self, entity_type.__name__)

    @property
    def User(self):
        if self._users is None and self.session is not None:
            self._users = UserRepository(self.session)

        return self._users

    @property
    def Role(self) -> RoleRepository:
        if self._role is None and self.session is not None:
            self._role = RoleRepository(self.session)

        return self._role

    @property
    def BotAccount(self) -> BotAccountRepository:
        if self._bot_account is None and self.session is not None:
            self._bot_account = BotAccountRepository(self.session)

        return self._bot_account

    @property
    def Destination(self) -> DestinationRepository:
        if self._destination is None and self.session is not None:
            self._destination = DestinationRepository(self.session)

        return self._destination

    @property
    def log(self) -> LogRepository:
        if self._log is None and self.session is not None:
            self._log = LogRepository(self.session)

        return self._log

    @property
    def Message(self) -> MessageRepository:
        if self._message is None and self.session is not None:
            self._message = MessageRepository(self.session)

        return self._message

    @property
    def Media(self) -> MediaRepository:
        if self._media is None and self.session is not None:
            self._media = MediaRepository(self.session)

        return self._media

    @property
    def UserAccount(self) -> UserAccountRepository:
        if self._user_account is None and self.session is not None:
            self._user_account = UserAccountRepository(self.session)

        return self._user_account

    @property
    def MessageTarget(self) -> MessageTargetRepository:
        if self._message_target is None and self.session is not None:
            self._message_target = MessageTargetRepository(self.session)

        return self._message_target

    def __exit__(self, exc_type, exc_value, traceback):
        if self.session:
            if exc_type is not None:
                self.session.rollback()
                raise DataBaseError(
                    "an error in databas", {"type": exc_type, "error": exc_value}
                )
            else:
                self.session.commit()

            self.session.close()

            self.session = None
            self.users = None
