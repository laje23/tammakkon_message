from infrastructure.platforms.requestbuilders import EitaaPlatform
from domain.interfaces import ISender
from  infrastructure.platforms.send_method import send_post


class EitaaSender(ISender):
    Platform = EitaaPlatform()
    def _send_post(self , data: dict)-> dict:
        return send_post(data=data)
    
    def _check_send(self , response_data)->bool:
        if response_data["ok"]is "True" or response_data["ok"]:
            return True
        else :
            return False
    
    def send_text(self, chat_id: str, token: str, text: str) -> bool:
        data=self.Platform.send_text(token=token , text=text , chat_id=chat_id)
        
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
    def send_photo(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        data=self.Platform.send_photo(token=token , photo=file , chat_id=chat_id , caption=text)
        
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
    def send_audio(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        data=self.Platform.send_audio(token=token , audio=file , chat_id=chat_id , caption=text)
        
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
    def send_video(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        data=self.Platform.send_video(token=token , video=file , chat_id=chat_id , caption=text)
        
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
        
    def send_document(self, chat_id: str, token: str, text: str, file: bytes) -> bool:
        data=self.Platform.send_document(token=token , document=file , chat_id=chat_id , caption=text)
        
        response_data=self._send_post(data)
        
        return self._check_send(response_data)
        
        
        



