from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError


class BotAccountController:

    container = container

    def get_bot_account_by_id(self, id: int):

        with self.container.unit_of_work as uow:

            bot_account = uow.BotAccount.get_by_id(id)

            if bot_account:
                return {
                    "id": bot_account.id,
                    "platform": bot_account.platform,
                    "name": bot_account.name,
                    "is_active": bot_account.is_active,
                    "created_at": bot_account.created_at,
                    "updated_at": bot_account.updated_at,
                }

        raise NotFoundError("bot_account not found")


    def get_all_bots(self):

        result = []

        with self.container.unit_of_work as uow:

            bots = uow.BotAccount.get_all()

            for bot in bots:
                result.append({
                    "id": bot.id,
                    "name": bot.name,
                    "is_active": bot.is_active,
                    "platform": bot.platform,
                })

        return result


    def update_bot_account(
        self,
        id: int,
        data
    ):

        with self.container.unit_of_work as uow:

            bot_account = uow.BotAccount.get_by_id(id)

            if not bot_account:
                raise NotFoundError("bot_account not found")

            bot_account.update(
                platform=data.platform,
                name=data.name,
                token=data.token
            )

            if data.is_active:
                bot_account.activate()
            else:
                bot_account.deactivate()

            uow.BotAccount.update(bot_account)

            return {
                "id": bot_account.id,
                "name": bot_account.name,
                "platform": bot_account.platform,
                "is_active": bot_account.is_active,
                "created_at": bot_account.created_at,
                "updated_at": bot_account.updated_at,
            }
        
        self.container._logger.log(
            f"bot_account with id {bot_account.id} updated",
            self.container._logger.category.AUTH.value,
            self.container._logger.level.INFO.value,
            self.__class__.__name__ 
        )