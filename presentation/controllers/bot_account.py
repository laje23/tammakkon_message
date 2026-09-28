from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError
from domain.entities import BotAccount
from fastapi import HTTPException
from presentation.controllers.decorators import safe_class


@safe_class
class BotAccountController:

    container = container

    def _log(self, message):
        self.container.logger.log(
            message,
            self.container.logger.category.SYSTEM,
            self.container.logger.level.INFO,
            self.__class__.__name__,
        )

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
                result.append(
                    {
                        "id": bot.id,
                        "name": bot.name,
                        "is_active": bot.is_active,
                        "platform": bot.platform,
                    }
                )

        return result

    def update_bot_account(self, id: int, data):

        with self.container.unit_of_work as uow:

            bot_account = uow.BotAccount.get_by_id(id)

            if not bot_account:
                raise NotFoundError("bot_account not found")

            token = (
                self.container.encryption_service.encrip(data.token)
                if data.token
                else None
            )

            bot_account.update(platform=data.platform, name=data.name, token=token)

            if data.is_active:
                bot_account.activate()
            else:
                bot_account.deactivate()

            uow.BotAccount.update(bot_account)

            self._log("bot updated")

            return {
                "id": bot_account.id,
                "name": bot_account.name,
                "platform": bot_account.platform,
                "is_active": bot_account.is_active,
                "created_at": bot_account.created_at,
                "updated_at": bot_account.updated_at,
            }

    def delete_bot_account(self, id: int):

        with self.container.unit_of_work as uow:
            if uow.Destination.exists_by_bot_account_id(id):
                return {"success": False, "message": "بات به چند مقصد متصل است"}
        self._log("bot deleted")

        return {"success": True, "message": "بات با موفقیت حذف شد."}

    def create_bot_account(self, data):
        token = self.container.encryption_service.encrip(data.token)

        bot = BotAccount(
            None,
            platform=data.platform,
            name=data.name,
            token=token,
            is_active=data.is_active,
        )

        with self.container.unit_of_work as uow:
            uow.BotAccount.create(bot)

        self._log("bot created")
        return {"success": True, "message": "بات با موفقیت ساخته شد."}
