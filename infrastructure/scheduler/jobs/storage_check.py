from infrastructure.dependency_Injection import container



def check_storage_usage():

    used_percent = container.storage_service.check_folders_capacity()
    if used_percent >= 80 and not container.storage_service.storage_warning_active:

        container.logger.log(
            f"Storage capacity is {used_percent:.2f}% used",
            container.logger.category.SYSTEM,
            container.logger.level.WARNING,
            "check_storage_usage"
        )

        container.storage_service.storage_warning_active = True

    elif used_percent < 80:

        container.storage_service.storage_warning_active = False