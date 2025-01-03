from flet import *


class PersonalInformation(View):
    def __init__(self, route, page):
        super().__init__(route=route)
        self.scroll = ScrollMode.AUTO

        self.appbar = AppBar(
            leading=IconButton(
                icon=icons.ARROW_BACK,
                icon_color="#ffffff",
                on_click=lambda x: self.page.go("/Profile"),
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

        self.controls = [
            ResponsiveRow(
                controls=[
                    Column(
                        controls=[
                            Container(
                                content=Image(src="/images/logo.png", width=150),
                                border_radius=border_radius.all(150),
                                bgcolor="red",
                            ),
                            Container(height=20),
                            ResponsiveRow(
                                controls=[
                                    Text(
                                        "تعديل المعلومات الشخصية",
                                        style=TextStyle(
                                            size=12,
                                            weight=FontWeight.BOLD,
                                            font_family="ElMessiri",
                                        ),
                                        color="#666666",
                                        text_align=TextAlign.START,
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    TextField(
                                        label="اسم المستخدم",
                                        border_radius=border_radius.all(22),
                                        border_color="#171335",
                                        text_style=TextStyle(
                                            size=15, font_family="ElMessiri"
                                        ),
                                        label_style=TextStyle(
                                            size=14, font_family="ElMessiri"
                                        ),
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    TextField(
                                        label="الاسم الاول",
                                        border_radius=border_radius.all(22),
                                        border_color="#171335",
                                        text_style=TextStyle(
                                            size=15, font_family="ElMessiri"
                                        ),
                                        label_style=TextStyle(
                                            size=14, font_family="ElMessiri"
                                        ),
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    TextField(
                                        label="الاسم الاخير",
                                        border_radius=border_radius.all(22),
                                        border_color="#171335",
                                        text_style=TextStyle(
                                            size=15, font_family="ElMessiri"
                                        ),
                                        label_style=TextStyle(
                                            size=14, font_family="ElMessiri"
                                        ),
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    ElevatedButton(
                                        "حفظ التعديلات",
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(radius=22),
                                            bgcolor="#171335",
                                            color="#ffffff",
                                            text_style=TextStyle(
                                                size=15,
                                                weight=FontWeight.BOLD,
                                                font_family="ElMessiri",
                                            ),
                                            padding=5,
                                        ),
                                    ),
                                ]
                            ),
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    )
                ],
                vertical_alignment=CrossAxisAlignment.CENTER,
                alignment=alignment.center,
            ),
        ]


class SecurityPasswords(View):
    def __init__(self, route, page):
        super().__init__(route=route)
        self.scroll = ScrollMode.AUTO

        self.appbar = AppBar(
            leading=IconButton(
                icon=icons.ARROW_BACK,
                icon_color="#ffffff",
                on_click=lambda x: self.page.go("/Profile"),
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

        self.controls = [
            ResponsiveRow(
                controls=[
                    Column(
                        controls=[
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    Text(
                                        "تغيير كلمة مرور حسابك",
                                        style=TextStyle(
                                            size=12,
                                            weight=FontWeight.BOLD,
                                            font_family="ElMessiri",
                                        ),
                                        color="#666666",
                                        text_align=TextAlign.START,
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    TextField(
                                        label="كلمة المرور الحالية",
                                        border_radius=border_radius.all(22),
                                        border_color="#171335",
                                        text_style=TextStyle(
                                            size=15, font_family="ElMessiri"
                                        ),
                                        label_style=TextStyle(
                                            size=14, font_family="ElMessiri"
                                        ),
                                        password=True,
                                        can_reveal_password=True,
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    TextField(
                                        label="كلمة المرور الجديدة",
                                        border_radius=border_radius.all(22),
                                        border_color="#171335",
                                        text_style=TextStyle(
                                            size=15, font_family="ElMessiri"
                                        ),
                                        label_style=TextStyle(
                                            size=14, font_family="ElMessiri"
                                        ),
                                        password=True,
                                        can_reveal_password=True,
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    TextField(
                                        label="تأكيد كلمة المرور الحديدة",
                                        border_radius=border_radius.all(22),
                                        border_color="#171335",
                                        text_style=TextStyle(
                                            size=15, font_family="ElMessiri"
                                        ),
                                        label_style=TextStyle(
                                            size=14, font_family="ElMessiri"
                                        ),
                                        password=True,
                                        can_reveal_password=True,
                                    ),
                                ],
                            ),
                            Container(height=10),
                            ResponsiveRow(
                                controls=[
                                    ElevatedButton(
                                        "حفظ التعديلات",
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(radius=22),
                                            bgcolor="#171335",
                                            color="#ffffff",
                                            text_style=TextStyle(
                                                size=15,
                                                weight=FontWeight.BOLD,
                                                font_family="ElMessiri",
                                            ),
                                            padding=5,
                                        ),
                                    ),
                                ]
                            ),
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    )
                ],
                vertical_alignment=CrossAxisAlignment.CENTER,
                alignment=alignment.center,
            ),
        ]


class Profile(View):
    def __init__(self, route , page):
        super().__init__(route=route)
        self.scroll = ScrollMode.AUTO

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
                    Container(height=10),
                    Column(
                        controls=[
                            Container(
                                content=Image(src="/images/logo.png", width=150),
                                border_radius=border_radius.all(150),
                            ),
                            Container(
                                content=Text(
                                    "اسم المستخدم",
                                    size=20,
                                    weight=FontWeight.BOLD,
                                    color="#666666",
                                    font_family="ElMessiri",
                                ),
                            ),
                            Container(height=30),
                            Column(
                                controls=[
                                    ResponsiveRow(
                                        controls=[
                                            Container(
                                                content=ListTile(
                                                    title=Text(
                                                        "البيانات الشخصية",
                                                        style=TextStyle(
                                                            size=15,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    trailing=IconButton(
                                                        icon=icons.PERSON,
                                                    ),
                                                ),
                                                bgcolor="#ffffff",
                                                border=border.all(0.5, "#110b22"),
                                                border_radius=border_radius.all(5),
                                                on_click=lambda x: self.page.go(
                                                    "/PersonalInformation"
                                                ),
                                            ),
                                        ],
                                    ),
                                    ResponsiveRow(
                                        controls=[
                                            Container(
                                                content=ListTile(
                                                    title=Text(
                                                        "الامان وكلمة المرور",
                                                        style=TextStyle(
                                                            size=15,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    trailing=IconButton(
                                                        icon=icons.LOCK,
                                                    ),
                                                ),
                                                bgcolor="#ffffff",
                                                border=border.all(0.5, "#110b22"),
                                                border_radius=border_radius.all(5),
                                                on_click=lambda x: self.page.go(
                                                    "/SecurityPasswords"
                                                ),
                                            ),
                                        ],
                                    ),
                                    ResponsiveRow(
                                        controls=[
                                            Container(
                                                content=ListTile(
                                                    title=Text(
                                                        "تسجيل الخروج",
                                                        style=TextStyle(
                                                            size=15,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    trailing=IconButton(
                                                        icon=icons.LOGOUT,
                                                    ),
                                                ),
                                                bgcolor="#ffffff",
                                                border=border.all(0.5, "#110b22"),
                                                border_radius=border_radius.all(5),
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                expand=True,
            )
        )
