import mimetypes


class BalePlatform:

    timeout = 20
    limit_file_size = 50_000
    
    
    
    base_url = "https://tapi.bale.ai/bot<token>/<method>"
    
    def create_url(self, token: str, method: str) -> str:
        return (
            self.base_url
            .replace("<token>", token)
            .replace("<method>", method)
        )
        
        
    def send_text(self, token,text:str="سلام" , chat_id:str = ""):
        url = self.create_url(token, "sendMessage")
        
        data = {"chat_id":chat_id , "text":text}
        
        return{"json":data , "url":url}

    def _send_media(
        self,
        *,
        method: str,
        token:str ,
        field_name: str,
        file: bytes,
        file_name: str,
        mime_type: str,
        chat_id: str,
        caption: str = "",
    ):
        url = self.create_url(token, method)

        data = {
            "chat_id": chat_id,
            "caption": caption,
        }

        files = {
            field_name: (
                file_name,
                file,
                mime_type,
            )
        }

        return {
            "url": url,
            "data": data,
            "files": files,
        }

    # -------------------------
    # Media
    # -------------------------

    def send_photo(
        self,
        token:str ,
        photo: bytes,
        file_name: str = "image.jpg",
        caption: str = "این یک عکس هست",
        chat_id: str = "4488387573",
    ):
        return self._send_media(
            method="sendphoto",
            token = token ,
            field_name="photo",
            file=photo,
            file_name=file_name,
            mime_type="image/jpeg",
            chat_id=chat_id,
            caption=caption,
        )

    def send_audio(
        self,
        token:str ,
        audio: bytes,
        file_name: str = "audio.mp3",
        caption: str = "این یک صدا هست",
        chat_id: str = "4488387573",
    ):
        return self._send_media(
            method="sendAudio",
            token = token ,
            field_name="audio",
            file=audio,
            file_name=file_name,
            mime_type="audio/mpeg",
            chat_id=chat_id,
            caption=caption,
        )

    def send_video(
        self,
        token :str ,
        video: bytes,
        file_name: str = "video.mp4",
        caption: str = "این یک ویدیو هست",
        chat_id: str = "4488387573",
    ):
        return self._send_media(
            method="sendvideo",
            token = token ,
            field_name="video",
            file=video,
            file_name=file_name,
            mime_type="video/mp4",
            chat_id=chat_id,
            caption=caption,
        )

    def send_document(
        self,
        token :str ,
        document: bytes,
        file_name: str = "document.pdf",
        caption: str = "این یک فایل هست",
        chat_id: str = "4488387573",
    ):
        return self._send_media(
            method="senddocument",
            token = token ,
            field_name="document",
            file=document,
            file_name=file_name,
            mime_type="application/pdf",
            chat_id=chat_id,
            caption=caption,
        )

    def send_voice(
        self,
        token :str ,
        voice: bytes,
        file_name: str = "voice.mp3",
        caption: str = "این یک فایل هست",
        chat_id: str = "4488387573",
    ):
        return self._send_media(
            method="sendVoice",
            token = token ,
            field_name="voice",
            file=voice,
            file_name=file_name,
            mime_type="audio/mpeg",
            chat_id=chat_id,
            caption=caption,
        )
