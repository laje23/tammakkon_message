from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError
from presentation.controllers.decorators import safe_class
from domain.entities import Role


@safe_class
class RoleController:

    container = container

    def _log(self, message):
        self.container.logger.log(
            message,
            self.container.logger.category.SYSTEM,
            self.container.logger.level.INFO,
            self.__class__.__name__,
        )

    def get_roles(self):
        with self.container.unit_of_work as uow:
            return uow.Role.get_all()

    def get_role_by_id(self, id: int):
        with self.container.unit_of_work as uow:
            role = uow.Role.get_by_id(id)

            if not role:
                raise NotFoundError("Role not found")

            return role

    def create_role(self, data):

        role = Role(
            None,
            name=data.name,
            description=data.description,
        )

        with self.container.unit_of_work as uow:
            uow.Role.create(role)
            self._log("role created")

        return {
            "success": True,
            "message": "نقش ساخته شد",
        }

    def update_role(self, id, data):

        with self.container.unit_of_work as uow:

            role = uow.Role.get_by_id(id)

            if not role:
                raise NotFoundError("Role not found")

            role.update(
                name=data.name,
                description=data.description,
            )

            uow.Role.update(role)

            self._log("role updated")

        return {
            "success": True,
            "message": "نقش ویرایش شد",
        }

    def delete_role(self, id):

        with self.container.unit_of_work as uow:

            role = uow.Role.get_by_id(id)

            if not role:
                raise NotFoundError("Role not found")

            uow.Role.delete(id)

            self._log("role deleted")

        return {
            "success": True,
            "message": "نقش حذف شد",
        }

    def get_role_permissions(self, id):

        with self.container.unit_of_work as uow:

            role = uow.Role.get_by_id(id)

            if not role:
                raise NotFoundError("Role not found")

            return uow.Role.get_permissions(id)

    def update_role_permissions(self, id, data):

        with self.container.unit_of_work as uow:

            role = uow.Role.get_by_id(id)

            if not role:
                raise NotFoundError("Role not found")

            if data.remove_list:
                uow.Role.remove_permissions(
                    id,
                    data.remove_list,
                )

            if data.add_list:
                uow.Role.add_permissions(
                    id,
                    data.add_list,
                )

            self._log("permissions of role changed")

        return {
            "success": True,
            "message": "مجوزهای نقش تغییر کرد",
        }
