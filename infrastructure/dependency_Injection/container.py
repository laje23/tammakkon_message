from domain.interfaces import *
from application.service import *
from infrastructure.database.unit_of_work import UnitOfWork
from infrastructure.platforms import GetPlatform


class _Container:

    _uow: IUnitOfWork | None = None
    _logger: ILogger | None = None
    _statistics_service: IStatisticsService | None = None
    _command_bus: ICommandBus | None = None
    _event_bus: IEventBus | None = None
    _hash_service: IHashService | None = None
    _encryption_service: IEncription | None = None
    _get_platform: IGetPlatform | None = None
    _media_service: IStorageService | None = None
    _authentication: IAuthenticationService | None = None

    @property
    def unit_of_work(self) -> IUnitOfWork:
        if self._uow is None:
            self._uow = UnitOfWork()

        return self._uow

    @property
    def logger(self) -> ILogger:
        if self._logger is None:
            self._logger = LogService(self.unit_of_work)

        return self._logger

    @property
    def statistics_service(self) -> IStatisticsService:
        if self._statistics_service is None:
            self._statistics_service = StatisticsService(self.unit_of_work)

        return self._statistics_service

    @property
    def hash_service(self) -> IHashService:
        if self._hash_service is None:
            self._hash_service = HashService()

        return self._hash_service

    @property
    def encryption_service(self) -> IEncription:
        if self._encryption_service is None:
            self._encryption_service = EncryptionService()

        return self._encryption_service

    @property
    def get_platform_service(self) -> IGetPlatform:
        if self._get_platform is None:
            self._get_platform = GetPlatform()

        return self._get_platform

    @property
    def media_service(self) -> IStorageService:
        if self._media_service is None:
            self._media_service = StorageService()

        return self._media_service

    @property
    def authentication(self) -> IAuthenticationService:
        if self._authentication is None:
            self._authentication = AuthenticationService(
                self.unit_of_work, self.hash_service
            )

        return self._authentication


container = _Container()
