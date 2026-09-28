from domain.exeptions import ValidationError, NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session 
from sqlalchemy import select, insert, delete 

from infrastructure.database.models import UserModel, RoleModel
from infrastructure.database.relation_tables.user_role import user_role_table

from domain.entities import User, Role
from infrastructure.database.mappers import UserMapper, RoleMapper
from domain.repositories import IUserRepository


class UserRepository(SQLAlchemyRepository[UserModel], IUserRepository):

    def __init__(self, session: Session):
        super().__init__(session)

        self.mapper = UserMapper()
        self.role_mapper = RoleMapper()

    @property
    def model(self) -> type[UserModel]:
        return UserModel

    # ---------------------------------------------------------
    # User
    # ---------------------------------------------------------

    def create(self, entity: User):
        model = self.mapper.to_model(entity)
        model = super().create(model)

    def update(self, entity: User) -> int:
        if not entity.id:
            raise ValidationError("entity id is empty")

        model = super().get_by_id(entity.id)

        if model is None:
            raise NotFoundError(
                f"User with id={entity.id} not found"
            )

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

        return model.id

    def get_by_id(self, id: int) -> User | None:
        model = super().get_by_id(id)

        if model:
            return self.mapper.to_entity(model)

        return None
    
    def get_by_username(self , username:str):
        query = select(UserModel).where(
            UserModel.user_name == username
        )
        model =self.session.execute(query).scalar()
        if model :
            return self.mapper.to_entity(model)
            
    

    def get_all(self) -> list[User]:
        models = super().get_all()

        return [
            self.mapper.to_entity(model)
            for model in models
        ]

    def search_username(self, name: str) -> list[User]:
        query = select(UserModel).where(
            UserModel.user_name.ilike(f"%{name}%")
        )

        models = self.session.execute(query).scalars().all()

        return [
            self.mapper.to_entity(model)
            for model in models
        ]

    # ---------------------------------------------------------
    # Roles
    # ---------------------------------------------------------

    def add_role(
        self,
        user_id: int,
        role_id: int,
    ) -> None:

        # بررسی وجود کاربر
        user = super().get_by_id(user_id)

        if user is None:
            raise NotFoundError(
                f"User with id={user_id} not found"
            )

        # بررسی وجود Role
        role = self.session.get(RoleModel, role_id)

        if role is None:
            raise NotFoundError(
                f"Role with id={role_id} not found"
            )

        # بررسی اینکه این Role قبلاً به User داده نشده باشد
        query = select(user_role_table).where(
            user_role_table.c.user_id == user_id,
            user_role_table.c.role_id == role_id,
        )

        exists = self.session.execute(query).first()

        if exists:
            return

        # ایجاد رابطه
        query = insert(user_role_table).values(
            user_id=user_id,
            role_id=role_id,
        )

        self.session.execute(query)
        self.session.flush()

    def remove_role(
        self,
        user_id: int,
        role_id: int,
    ) -> None:

        # بررسی وجود کاربر
        user = super().get_by_id(user_id)

        if user is None:
            raise NotFoundError(
                f"User with id={user_id} not found"
            )

        # حذف رابطه User و Role
        query = delete(user_role_table).where(
            user_role_table.c.user_id == user_id,
            user_role_table.c.role_id == role_id,
        )

        result = self.session.execute(query)

        if result.rowcount == 0:  # type: ignore
            raise NotFoundError(
                f"Role with id={role_id} is not assigned to user {user_id}"
            )

        self.session.flush()

    def get_roles(
        self,
        user_id: int,
    ) -> list[Role]:

        # بررسی وجود کاربر
        user = super().get_by_id(user_id)

        if user is None:
            raise NotFoundError(
                f"User with id={user_id} not found"
            )

        query = (
            select(RoleModel)
            .join(
                user_role_table,
                user_role_table.c.role_id == RoleModel.id,
            )
            .where(
                user_role_table.c.user_id == user_id
            )
        )

        models = self.session.execute(query).scalars().all()

        return [
            self.role_mapper.to_entity(model)
            for model in models
        ]

    def add_roles(
        self,
        user_id: int,
        role_ids: list[int],
    ) -> None:

        # بررسی وجود کاربر
        user = super().get_by_id(user_id)

        if user is None:
            raise NotFoundError(
                f"User with id={user_id} not found"
            )

        for role_id in role_ids:

            # بررسی وجود Role
            role = self.session.get(RoleModel, role_id)

            if role is None:
                raise NotFoundError(
                    f"Role with id={role_id} not found"
                )

            # بررسی اینکه Role قبلاً اختصاص داده نشده باشد
            query = select(user_role_table).where(
                user_role_table.c.user_id == user_id,
                user_role_table.c.role_id == role_id,
            )

            exists = self.session.execute(query).first()

            if exists:
                continue

            # ایجاد رابطه
            query = insert(user_role_table).values(
                user_id=user_id,
                role_id=role_id,
            )

            self.session.execute(query)

        self.session.flush()


    def remove_roles(
        self,
        user_id: int,
        role_ids: list[int],
    ) -> None:

        # بررسی وجود کاربر
        user = super().get_by_id(user_id)

        if user is None:
            raise NotFoundError(
                f"User with id={user_id} not found"
            )

        for role_id in role_ids:

            query = delete(user_role_table).where(
                user_role_table.c.user_id == user_id,
                user_role_table.c.role_id == role_id,
            )

            self.session.execute(query)

        self.session.flush()