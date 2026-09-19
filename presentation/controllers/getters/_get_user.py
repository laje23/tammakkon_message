from infrastructure.dependency_Injection import container
from domain.exeptions import NotFoundError

def get_user(id : int ):
    with container.unit_of_work as uow :
        user =uow.User.get_by_id(id)
    if user :
        return {
            "id" :user.id ,
            "user_name" :user.user_name ,
            "is_active" :user.is_active ,
            "created_at" :user.created_at ,
            "updated_at" :user.updated_at ,
        }
    else :
        raise NotFoundError(f"user not found")