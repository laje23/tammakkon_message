from infrastructure.dependency_Injection import container
from presentation.controllers.decorators import safe_class 

@safe_class
class DashboardController:

    def get_datas(self) -> dict:
        return container.statistics_service.get_dashboard_data()
