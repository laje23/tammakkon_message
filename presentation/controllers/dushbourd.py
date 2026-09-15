from infrastructure.dependency_Injection import container


class DashboardController:

    def get_datas(self) -> dict:
        return container.statistics_service.get_dashboard_data()