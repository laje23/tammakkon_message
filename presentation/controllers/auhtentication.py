from infrastructure.dependency_Injection import container


def authenticate(data):
    user = container.authentication.authenticate(
        data.username,
        data.password,
    )

    if not user:
        return {
            "success": False,
            "message": "نام کاربری یا رمز عبور اشتباه است.",
        }
    if not user.is_active:
        return {
            "success": False,
            "message": "شما توسط مدیر مسدود شده اید",
        }
    permissions = []
    if user.id:
        permissions = container.authentication.get_user_permissions(user.id)

    return {
        "success": True,
        "message": "خوش آمدید",
        "permissions": permissions,
    }
