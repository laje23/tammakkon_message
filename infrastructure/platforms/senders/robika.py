from infrastructure.platforms.requestbuilders import RobikaPlatform
from domain.interfaces import ISender
import httpx 


class RobikaSender(ISender):
    Platform = RobikaPlatform()
    def _send_post(self , data: dict)-> dict:
        response =httpx.post(**data)
        response.raise_for_status()
        return response.json()
    
    def _check_send(self , response_data)->bool:
        if response_data["ok"]is "True" or response_data["ok"]:
            return True
        else :
            return False
    
    def send_text(self, chat_id: str, token: str, text: str) -> bool:
        data=self.Platform.send_text(token=token , text=text , chat_id=chat_id)
        
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
    
    def _get_file_id(self , token ,file: bytes , mim_type:str)->str:
        
        data1=self.Platform.request_send_file(token= token , mimetype=mim_type)
        respons1=self._send_post(data1)
        data2=self.Platform.upload_file(url=respons1["data"]["upload_url"] , file=file)
        respons2=self._send_post(data2)
        return respons2["data"]["file_id"]
    
        
    def send_photo(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        file_id=self._get_file_id(token=token , file=file , mim_type="Image")
        data =self.Platform.send_file(token=token , chat_id=chat_id , caption=text,file_id=file_id)
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
        
    def send_audio(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        file_id=self._get_file_id(token=token , file=file , mim_type="Audio")
        data =self.Platform.send_file(token=token , chat_id=chat_id , caption=text,file_id=file_id)
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
        
    def send_video(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        file_id=self._get_file_id(token=token , file=file , mim_type="Video")
        data =self.Platform.send_file(token=token , chat_id=chat_id , caption=text,file_id=file_id)
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
        
    def send_document(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        file_id=self._get_file_id(token=token , file=file , mim_type="Document")
        data =self.Platform.send_file(token=token , chat_id=chat_id , caption=text,file_id=file_id)
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
        
        
