from domain.exeptions import ValidationError , NotFoundError
from infrastructure.database.repository import SQLAlchemyRepository
from sqlalchemy.orm import Session
from infrastructure.database.models import BotAccountModel
from domain.entities import  BotAccount
from infrastructure.database.mappers import BotAccountMapper
from domain.repositories import IBotAccountRepository

class BotAccountRepository(SQLAlchemyRepository[BotAccountModel] ,IBotAccountRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.mapper = BotAccountMapper()
    
    @property
    def model(self) -> type[BotAccountModel]:
        return BotAccountModel
    
    
    def create(self, entity:BotAccount):
        model = self.mapper.to_model(entity)
        model =super().create(model)

    def update(self, entity: BotAccount):
        if not entity.id :
            raise ValidationError("entity id is empty")
        
        model = super().get_by_id(entity.id)
        
        if model is None:
            raise NotFoundError(f"BotAccount with id={entity.id} not found")

        self.mapper.update_model(entity, model)

        self.session.flush()
        self.session.refresh(model)

    def delete(self, entity: BotAccount) -> None:
        model =self.mapper.to_model(entity)
        super().delete(model) 
    
    def get_by_id(self,  id: int) -> BotAccountModel | None:
        return super().get_by_id(id)
    
    def get_all(self) -> list[BotAccountModel]|None:
        return super().get_all()