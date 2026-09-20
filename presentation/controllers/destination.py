from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError


class DestinationController:

    container = container

    def get_destination_by_id(self, id: int):

        with self.container.unit_of_work as uow:

            destination = uow.Destination.get_by_id(id)

            if not destination:
                raise NotFoundError("destination not found")

            return {
                "id": destination.id,
                "external_id": destination.external_id,
                "name": destination.name,
                "platform": destination.platform,
                "bot_account_id": destination.bot_account_id,
                "type": destination.type,
                "is_active": destination.is_active,
                "created_at": destination.created_at,
                "updated_at": destination.updated_at,
            }

    def get_all_destinations(self):

        result = []

        with self.container.unit_of_work as uow:

            destinations = uow.Destination.get_all()

            for destination in destinations:

                result.append({
                    "id": destination.id,
                    "name": destination.name,
                    "platform": destination.platform,
                    "type": destination.type,
                    "is_active": destination.is_active,
                })

        return result

    def update_destination(self, id: int, data):

        with self.container.unit_of_work as uow:

            destination = uow.Destination.get_by_id(id)

            if not destination:
                raise NotFoundError("destination not found")

            destination.update(
                name=data.name,
                external_id=data.external_id,
                bot_account_id=data.bot_account_id,
                type=data.type,
                platform= data.platform
            )

            if data.is_active:
                destination.activate()
            else:
                destination.deactivate()

            uow.Destination.update(destination)

            result = {
                "id": destination.id,
                "external_id": destination.external_id,
                "name": destination.name,
                "platform": destination.platform,
                "bot_account_id": destination.bot_account_id,
                "type": destination.type,
                "is_active": destination.is_active,
                "created_at": destination.created_at,
                "updated_at": destination.updated_at,
            }

            self.container.logger.log(
                f"destination with id {id} updated",
                self.container.logger.category.AUTH,
                self.container.logger.level.INFO,
                self.__class__.__name__,
            )

            return result