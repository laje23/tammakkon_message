from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError

def get_message(id : int ):
    with container.unit_of_work as uow :
        message =uow.Message.get_by_id(id)
    if message :
        return {
            "id" : message.id,
            "media_id" : message.media_id,
            "type" : message.type ,
            "text" : message.text ,
            "created_by" : message.created_by ,
            "created_at" : message.created_at ,
            "updated_at" : message.updated_at
        }
    else :
        raise NotFoundError(f"message not found")