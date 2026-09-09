import mimetypes

class EitaaPlatform:
    base_url = "https://eitaayar.ir/api/<token>/<method>"
    token = "bot397007:d69c18d7-a0dc-484d-834d-52ddf779c69a"
    
    
    
    def create_url(self, token , method):
        url = self.base_url.replace("<token>", token).replace("<method>", method)
    
        return url
    
    def send_text(self, token :str ,text:str="سلام" , chat_id:str = ""):
        url = self.create_url(token, "sendMessage")
        
        data = {"chat_id":chat_id , "text":text}
        
        return{"data":data , "url":url}
        
    

    def _send_media(
        self,
        token : str ,
        file: bytes,
        chat_id: int,
        filename: str,
        caption: str = "",
        mime_type: str | None = None,
    ):
        url = self.create_url(token, "sendFile")

        mime_type = (
            mime_type
            or mimetypes.guess_type(filename)[0]
            or "application/octet-stream"
        )

        return {
            "url": url,
            "data": {
                "chat_id": chat_id,
                "caption": caption,
            },
            "files": {
                "file": (
                    filename,
                    file,
                    mime_type,
                )
            },
        }

    def send_photo(
        self,
        token : str ,
        photo: bytes,
        chat_id: int,
        file_name :str = "aname",
        caption: str = "",
    ):
        return self._send_media(
            file=photo,
            token= token , 
            chat_id=chat_id,
            filename=file_name,
            caption=caption,
            mime_type="image/jpeg",
        )
        
    def send_audio(
        self,
        token : str ,
        audio: bytes,
        chat_id: int,
        file_name :str = "",
        caption: str = "",
    ):
        return self._send_media(
            file=audio,
            token= token , 
            chat_id=chat_id,
            filename=file_name,
            caption=caption,
            mime_type="audio/mp3",
        )
        
    def send_video(
        self,
        token : str ,
        video: bytes,
        chat_id: int,
        file_name :str = "",
        caption: str = "",
    ):
        return self._send_media(
            file=video,
            token= token , 
            chat_id=chat_id,
            filename=file_name,
            caption=caption,
            mime_type="video/mp4",
        )
    
        
    def send_document(
        self,
        token : str ,
        document: bytes,
        chat_id: int,
        file_name :str = "",
        caption: str = "",
    ):
        return self._send_media(
            token= token , 
            file=document,
            chat_id=chat_id,
            filename=file_name,
            caption=caption,
            mime_type="document/pdf",
        )
    