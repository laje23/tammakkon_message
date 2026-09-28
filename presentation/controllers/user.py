from domain.entities import User
from infrastructure.dependency_Injection import container
from presentation.controllers.decorators import safe_class
from domain.exeptions import NotFoundError


@safe_class
class UserController:

    container = container

    def _log(self, message):
        self.container.logger.log(
            message,
            self.container.logger.category.SYSTEM,
            self.container.logger.level.INFO,
            self.__class__.__name__,
        )

    def create_user(self, data):

        password = self.container.hash_service.hash(data.password)

        user = User(None, data.user_name, password, data.is_active)

        with self.container.unit_of_work as uow:
            uow.User.create(user)

        self._log("user created")

        return {"success": True, "message": "کاربر با موفقیت ثبت شد"}

    def get_all_user(self):

        with self.container.unit_of_work as uow:

            users = uow.User.get_all()

            if not users:
                raise NotFoundError("users is empty")

            return users

    def get_user_by_id(self, id: int):

        with self.container.unit_of_work as uow:

            user = uow.User.get_by_id(id)

            if not user:
                raise NotFoundError("user not found")

            return user

    def update_user(self, id: int, data):

        with self.container.unit_of_work as uow:

            user = uow.User.get_by_id(id)

            if not user:
                raise NotFoundError("user not found")

            update_data = {
                "user_name": data.user_name,
            }

            if data.password:
                update_data["password"] = self.container.hash_service.hash(
                    data.password
                )

            user.update(**update_data)
            if data.is_active:
                user.activate()
            else:
                user.deactivate()

            uow.User.update(user)

        self._log("user updated")

        return {"success": True, "message": "کاربر با موفقیت ویرایش شد"}

    def delete_user(self, id: int):

        with self.container.unit_of_work as uow:

            user = uow.User.get_by_id(id)

            if not user:
                raise NotFoundError("user not found")

            uow.User.delete(id)

        self._log("user deleted")

        return {"success": True, "message": "کاربر با موفقیت حذف شد"}

    def get_roles(self, id: int):
        with self.container.unit_of_work as uow:
            roles = uow.User.get_roles(id)
            personal_roles = roles
            roles = uow.Role.get_all()
            all_role = roles
            return {
                "personal_role": personal_roles,
                "all_role": all_role,
            }

    def update_roles(self, user_id, data):
        remove_list: list[int]
        add_list: list[int]

        remove_list = data.remove_list
        add_list = data.add_list
        with self.container.unit_of_work as uow:
            uow.User.remove_roles(user_id, remove_list)
            uow.User.add_roles(user_id, add_list)
