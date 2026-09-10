from domain.interfaces import IUnitOfWork, IEventBus , IGetPlatform , IReadMedia , IEncription
from domain.commands import  SendMessagesCommand
from domain.exeptions import OperationFailedError
from domain.types import MessageType
class SendMessagesHandler:
    
    def __init__(self, unit_of_work: IUnitOfWork, event_bus: IEventBus , get_platform : IGetPlatform , media_reader : IReadMedia , encriper:IEncription) -> None:
        self.unit_of_work = unit_of_work
        self.event_bus = event_bus
        self.get_platform = get_platform
        self.media_reader = media_reader
        self.encriper = encriper




    def get_media(self , media_id)-> bytes:
        with self.unit_of_work as uow :
            media = uow.Media.get_by_id(media_id)
            if media :
                return self.media_reader.read(media.stored_name)
            else :
                raise OperationFailedError("reading media file faild")


    def handle(self, command:SendMessagesCommand):
        
        platform =self.get_platform.get_platform(command.platform)
        method_dict ={
            MessageType.TEXT : platform.send_text,
            MessageType.PHOTO : platform.send_photo,
            MessageType.AUDIO : platform.send_audio,
            MessageType.VIDEO : platform.send_video,
            MessageType.DOCUMENT:platform.send_document
        }
        if command.media_id:
            file =self.get_media(command.media_id)
        else : 
            file = None 
        
        
        method = method_dict[command.message_type]

        method(
            chat_id=command.chat_external_id,
            token=self.encriper.decrip(command.token) ,
            caption=command.text,
            file=file
        )
            
        