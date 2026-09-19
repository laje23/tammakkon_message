from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError

def get_message_target(id : int ):
    with container.unit_of_work as uow :
        message_target =uow.MessageTarget.get_by_id(id)
    if message_target :
        return {
            "id" : message_target.id ,
            "message_id" : message_target.message_id ,
            "destination_id" : message_target.destination_id,
            "status" : message_target.status ,
            "retry_count" : message_target.retry_count,
            "last_error" : message_target.last_error,
            "send_at" : message_target.send_at,
            "created_at" : message_target.created_at,
            "updated_at" : message_target.updated_at,
        }
    else :
        raise NotFoundError(f"message_target not found")