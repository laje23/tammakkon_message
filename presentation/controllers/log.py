from infrastructure.dependency_Injection import container
from presentation.controllers.decorators import safe_class


@safe_class
class LogController:
    container = container

    def get_logs(self):
        with self.container.unit_of_work as uow:
            logs = uow.log.get_all()
            return logs
