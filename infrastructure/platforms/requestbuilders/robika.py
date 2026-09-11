import mimetypes
from config.platform import robika_setting

class RobikaPlatform:

    base_url = robika_setting.base_url


    def create_url(self, token: str, method: str) -> str:
        return (
            self.base_url
            .replace("<token>", token)
            .replace("<method>", method)
        )
        
    def get_updates(self , token:str)-> dict:
        url = self.create_url(token , "getUpdates")
        
        return {"url":url}

    def send_text(self, token : str ,text:str , chat_id:str ):
        url = self.create_url(token, "sendMessage")
        
        data = {"chat_id":chat_id , "text":text}
        
        return{"json":data , "url":url}

    def send_file(self,token:str ,file_id, chat_id:str, caption:str =""):
        url = self.create_url(token , "sendFile")
        
        data = {
            "chat_id":chat_id,
            "file_id":file_id,
            "text":caption
        }
        return {"url":url , "json":data}
    
        
    
    def request_send_file(self , token ,mimetype):
        url = self.create_url(token , "requestSendFile")
        
        data = {
            "type" : mimetype
        }
        
        return {"url" : url , "json":data}
    
    def upload_file(self, url: str, file: bytes):
        return {
            "url": url,
            "files": {
                "file": file
            }
        }