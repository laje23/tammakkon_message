from datetime import timedelta
from typing import Sequence, TypeVar

from domain.base import AppEntity
from domain.interfaces import IUnitOfWork, IStatisticsService

EntityT = TypeVar("EntityT", bound=AppEntity)


class StatisticsService(IStatisticsService):

    def __init__(self, unit_of_work: IUnitOfWork) -> None:
        self.unit_of_work = unit_of_work

    def return_null(self):
        return

    @staticmethod
    def _group_by_week(
        entities: Sequence[EntityT],
    ) -> dict[str, list[EntityT]]:

        result: dict[str, list[EntityT]] = {}

        for entity in entities:
            created_at = entity.created_at

            # شنبه = شروع هفته
            days_from_saturday = (created_at.weekday() + 2) % 7

            week_start = created_at.date() - timedelta(days=days_from_saturday)

            week_start_str = week_start.isoformat()

            result.setdefault(week_start_str, []).append(entity)

        return result

    def message_status(self) -> dict[str, dict[str, int]]:
        result: dict[str, dict[str, int]] = {}

        with self.unit_of_work as uow:
            messages = uow.Message.get_all()
        if not messages:
            return {
                "2000-01-01": {
                    "message_count": 0,
                    "text_message": 0,
                    "photo_message": 0,
                    "audio_message": 0,
                    "video_message": 0,
                    "document_message": 0,
                }
            }

        messages_grouped = self._group_by_week(messages)

        for week_date, messages in messages_grouped.items():

            text_message = 0
            photo_message = 0
            audio_message = 0
            video_message = 0
            document_message = 0

            for message in messages:
                message_type = str(message.type).lower()

                if message_type == "text":
                    text_message += 1

                elif message_type == "photo":
                    photo_message += 1

                elif message_type == "audio":
                    audio_message += 1

                elif message_type == "video":
                    video_message += 1

                elif message_type == "document":
                    document_message += 1

            result[week_date] = {
                "message_count": len(messages),
                "text_message": text_message,
                "photo_message": photo_message,
                "audio_message": audio_message,
                "video_message": video_message,
                "document_message": document_message,
            }

        return result

    def destination_status(self) -> dict[str, dict[str, int]]:
        result: dict[str, dict[str, int]] = {}

        with self.unit_of_work as uow:
            destinations = uow.Destination.get_all()
        if not destinations:
            return {
                "2000-01-01": {
                    "count": 0,
                    "group": 0,
                    "channel": 0,
                    "super_group": 0,
                    "private": 0,
                }
            }

        destinations_grouped = self._group_by_week(destinations)

        for week_date, destinations in destinations_grouped.items():

            group = 0
            channel = 0
            super_group = 0
            private = 0

            for destination in destinations:
                destination_type = str(destination.type).lower()

                if destination_type == "channel":
                    channel += 1

                elif destination_type == "group":
                    group += 1

                elif destination_type == "super_group":
                    super_group += 1

                elif destination_type == "private":
                    private += 1

            result[week_date] = {
                "count": len(destinations),
                "group": group,
                "channel": channel,
                "super_group": super_group,
                "private": private,
            }

        return result

    def get_dashboard_data(self) -> dict:
        return {
            "messages": self.message_status(),
            "destinations": self.destination_status(),
        }
