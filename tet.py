from infrastructure.database.unit_of_work import UnitOfWork
from domain.entities import *
from domain.types import *

bot = BotAccount(None, PlatformType.BALE, "name", "token")
roll = Role(None, "name", "description")
user = User(None, "name", "s;lajf;lsj", True)
with UnitOfWork() as uow:
    # uow.User.create(user)
    uow.Role.create(roll)
    uow.BotAccount.create(bot)
