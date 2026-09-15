from domain.interfaces import *
from infrastructure.bus import *
from application.service import *
from infrastructure.dependency_Injection import container
from infrastructure.database.unit_of_work import UnitOfWork

uow = UnitOfWork()
logger = LogService(uow)
status_service_ = StatisticsService(uow)
command_bus_ = CommandBus()
event_bus_ = EventBus()
hash_service_ = HashService()
encryption_service = EncryptionService()
platform_service = GetPlatform()
media_reader = ReadMedia()

def register_container():

    container.register(IUnitOfWork, uow)
    container.register(ILogger, logger)
    container.register(ICommandBus, command_bus_)
    container.register(IEventBus, event_bus_)
    container.register(IHashService, hash_service_)
    container.register(IEncription, encryption_service)
    container.register(IGetPlatform, platform_service)
    container.register(IReadMedia, media_reader)
    container.register(IStatisticsService , status_service_)
