from flet import *
from views.login_screen.login_screen import Login
from views.signup_screen.signup_screen import SignUp
from views.welcome_screen.welcome_screen import Welcome
from views.home_screen.home_screen import Home
from views.profile_screen.profile_screen import (
    Profile,
    PersonalInformation,
    SecurityPasswords,
)
from views.notifications_screen.notifications_screen import (
    Notifications,
    MoreInfoAboutNotifications,
)
from views.devices_screen.devices_screen import Devices
from views.MostUsedApplications_screen.MostUsedApplications_screen import (
    MostUsedApplications,
)


def main(page: Page):
    # إعداد الخطوط
    page.fonts = {
        "LateefBoldFont": "/fonts/Lateef,Rakkas/Lateef/Lateef-Bold.ttf",
        "LateefNormalFont": "/fonts/Lateef,Rakkas/Lateef/Lateef-Medium.ttf",
        "Rakkas": "/fonts/Lateef,Rakkas/Rakkas/Rakkas-Regular.ttf",
        "ElMessiri": "/fonts/El_Messiri,Lateef,Rakkas/El_Messiri/ElMessiri-VariableFont_wght.ttf",
    }

    # إعدادات الموضوع
    page.theme_mode = ThemeMode.LIGHT
    page.rtl = True

    page.theme = Theme(
        font_family="LateefNormalFont",
        color_scheme_seed="#666666",
        text_theme=TextStyle(color="#110b22", font_family="LateefBoldFont"),
        appbar_theme=AppBarTheme(bgcolor="#110b22", color="#ffffff"),
    )

    def route_change(e):
        routes = {
            "/": Welcome,
            "/home": Home,
            "/login": Login,
            "/signup": SignUp,
            "/Profile": Profile,
            "/PersonalInformation": PersonalInformation,
            "/SecurityPasswords": SecurityPasswords,
            "/notifications": Notifications,
            "/MoreInfoAboutNotifications": MoreInfoAboutNotifications,
            "/devices": Devices,
            "/MostUsedApplications": MostUsedApplications,
        }

        # مسح الشاشة الحالية
        page.views.clear()

        # جلب الشاشة المناسبة بناءً على المسار
        page_class = routes.get(page.route, None)
        if page_class:
            page.views.append(
                page_class(route=page.route, page=page)
            )  # إضافة الشاشة المناسبة
        else:
            page.views.append(Text("Page not found"))  # إذا لم يكن المسار موجودًا

        page.update()

    # تحديد الدالة التي تدير التوجيه
    page.on_route_change = route_change
    if page.client_storage.contains_key("access") and page.client_storage.contains_key("refresh"):
        page.go("/home")
    else:
        page.go("/")


app(main, assets_dir="assets")
