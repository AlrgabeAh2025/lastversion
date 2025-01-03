from flet import *


class MoreInfoAboutNotifications(View):
    def __init__(self, route , page):
        super().__init__(route=route)
        self.scroll = ScrollMode.AUTO
        self.bgcolor = "#ffffff"

        self.appbar = AppBar(
            leading=IconButton(
                icon=icons.ARROW_BACK,
                icon_color="#ffffff",
                on_click=lambda x: self.page.go("/notifications"),
            ),
            title=Text(
                "وصلة",
                size=30,
                weight=FontWeight.BOLD,
                color="#ffffff",
                font_family="ElMessiri",
            ),
            toolbar_height=100,
        )

        self.controls.append(
            ResponsiveRow(
                controls=[
                    Container(height=20),
                    Text(
                        "معلومات التنبيه",
                        style=TextStyle(
                            size=12,
                            weight=FontWeight.BOLD,
                            font_family="ElMessiri",
                        ),
                        color="#666666",
                        expand=True,
                        text_align=TextAlign.CENTER,
                    ),
                    Container(
                        content=Column(
                            controls=[
                                ResponsiveRow(
                                    controls=[
                                        Container(
                                            content=ListTile(
                                                leading=Icon(icons.PERSON),
                                                title=Text(
                                                    "تنبيه بخصوص ابنك محمد",
                                                    style=TextStyle(
                                                        size=15,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                    ),
                                                ),
                                                subtitle=Text(
                                                    "ابنك يشاهد محتوى مقيد بالفئة العمرية",
                                                    style=TextStyle(
                                                        size=8,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                                ResponsiveRow(
                                    controls=[
                                        Container(
                                            content=ListTile(
                                                leading=Icon(icons.TIMER),
                                                title=Text(
                                                    "وقت حدوث البلاغ",
                                                    style=TextStyle(
                                                        size=15,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                    ),
                                                ),
                                                subtitle=Text(
                                                    "12:35 مساء",
                                                    style=TextStyle(
                                                        size=10,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                                ResponsiveRow(
                                    controls=[
                                        Container(
                                            content=ListTile(
                                                leading=Icon(icons.TIMER),
                                                title=Text(
                                                    "محتوى البلاغ",
                                                    style=TextStyle(
                                                        size=15,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                    ),
                                                ),
                                                subtitle=Text(
                                                    "محتوى الشاشة الذي تم التقاطه",
                                                    style=TextStyle(
                                                        size=10,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                                Container(
                                    content=Image(src="/images/logo.png", width=150),
                                    border_radius=border_radius.all(10),
                                    width=300,
                                ),
                            ],
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        bgcolor="#ffffff",
                        border=border.all(0.5, "#110b22"),
                        border_radius=border_radius.all(5),
                    ),
                ],
                expand=True,
            )
        )


class Notifications(View):
    def __init__(self, route, page):
        super().__init__(route=route)
        self.scroll = ScrollMode.AUTO
        self.bgcolor = "#ffffff"

        self.appbar = AppBar(
            leading=IconButton(
                icon=icons.ARROW_BACK,
                icon_color="#ffffff",
                on_click=lambda x: self.page.go("/home"),
            ),
            title=Text(
                "وصلة",
                size=30,
                weight=FontWeight.BOLD,
                color="#ffffff",
                font_family="ElMessiri",
            ),
            toolbar_height=100,
        )

        self.controls.append(
            ResponsiveRow(
                controls=[
                    Container(height=20),
                    Text(
                        "الاشعارات والتنبيهات",
                        style=TextStyle(
                            size=12,
                            weight=FontWeight.BOLD,
                            font_family="ElMessiri",
                        ),
                        color="#666666",
                        expand=True,
                        text_align=TextAlign.CENTER,
                    ),
                    Column(
                        controls=[
                            Container(height=30),
                            ResponsiveRow(
                                controls=[
                                    Container(
                                        content=ListTile(
                                            leading=Icon(
                                                icons.ERROR, color=colors.ERROR
                                            ),
                                            title=Text(
                                                "تنبيه بخصوص ابنك محمد",
                                                style=TextStyle(
                                                    size=15,
                                                    weight=FontWeight.BOLD,
                                                    font_family="ElMessiri",
                                                ),
                                            ),
                                            subtitle=Text(
                                                "ابنك يشاهد محتوى مقيد بالفئة العمرية",
                                                style=TextStyle(
                                                    size=8,
                                                    weight=FontWeight.BOLD,
                                                    font_family="ElMessiri",
                                                ),
                                            ),
                                            trailing=PopupMenuButton(
                                                icon=icons.MORE_VERT,
                                                items=[
                                                    PopupMenuItem(
                                                        text="حذف",
                                                        icon=icons.DELETE,
                                                    ),
                                                ],
                                                menu_position=PopupMenuPosition.UNDER,
                                                icon_color="#110b22",
                                                tooltip="خيارات",
                                            ),
                                        ),
                                        bgcolor="#ffffff",
                                        border=border.all(0.5, "#110b22"),
                                        border_radius=border_radius.all(5),
                                        on_click=lambda x: self.page.go(
                                            "/MoreInfoAboutNotifications"
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                expand=True,
            )
        )
