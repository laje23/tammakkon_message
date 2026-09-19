from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError

def get_destination(id : int ):
    with container.unit_of_work as uow :
        destination =uow.Destination.get_by_id(id)
    if destination :
        return {
            "id" : destination.id ,
            "external_id" : destination.external_id ,
            "name" : destination.name ,
            "platform " : destination.platform  ,
            "bot_account_id" : destination.bot_account_id ,
            "type" : destination.type ,
            "is_active" : destination.is_active ,
            "created_at" : destination.created_at ,
            "updated_at" : destination.updated_at ,

        }
    else :
        raise NotFoundError(f"destination not found")


