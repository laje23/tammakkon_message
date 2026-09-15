from domain.interfaces import IUnitOfWork


class Statuse:

    def __init__(self, unit_of_work: IUnitOfWork) -> None:
        self.unit_of_work = unit_of_work

    def message_status(self):
        with self.unit_of_work as uow:
            messages = uow.Message.get_all()

        count = len(messages)
        text_message = 0
        photo_message = 0
        audio_message = 0
        video_message = 0
        document_message = 0

        for message in messages:
            if message.type in ["text", "TEXT"]:
                text_message += 1
            if message.type in ["photo", "PHOTO"]:
                photo_message += 1
            if message.type in ["audio", "AUDIO"]:
                audio_message += 1
            if message.type in ["video", "VIDEO"]:
                video_message += 1
            if message.type in ["document", "DOCUMENT"]:
                document_message += 1

        return {
            "message_count": count,
            "text_message": text_message,
            "photo_message": photo_message,
            "audio_message": audio_message,
            "video_message": video_message,
            "document_message": document_message,
        }
