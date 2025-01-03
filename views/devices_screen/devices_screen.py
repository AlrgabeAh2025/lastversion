from flet import *


class Devices(View):
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
                            ResponsiveRow(
                                controls=[
                                    Text(
                                        "اضافة المزيد الاجهزة",
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
                            ResponsiveRow(
                                controls=[
                                    Container(
                                        content=ListTile(
                                            title=Text(
                                                "اضافة جهاز اخر",
                                                style=TextStyle(
                                                    size=15,
                                                    weight=FontWeight.BOLD,
                                                    font_family="ElMessiri",
                                                ),
                                            ),
                                            trailing=IconButton(
                                                icon=icons.QR_CODE,
                                            ),
                                        ),
                                        bgcolor="#ffffff",
                                        border=border.all(0.5, "#110b22"),
                                        border_radius=border_radius.all(5),
                                        on_click=lambda x: print(120),
                                    ),
                                ],
                            ),
                            Container(height=30),
                            ResponsiveRow(
                                controls=[
                                    Text(
                                        "الاجهزة التي اضفتها سابقا",
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
                            Column(
                                controls=[
                                    ResponsiveRow(
                                        controls=[
                                            Container(
                                                content=ListTile(
                                                    leading=Icon(
                                                        icons.PHONE_ANDROID_OUTLINED,
                                                        color="#110b22",
                                                    ),
                                                    title=Text(
                                                        "جهاز رقم 1",
                                                        style=TextStyle(
                                                            size=15,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    subtitle=Text(
                                                        "تمت الاضافة بتاريخ (12\6\2024)",
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

    def handle_dismissal(self, e):
        self.page.add(Text("Drawer dismissed"))

    def handle_change(self, e):
        self.page.add(Text(f"Selected Index changed: {e}"))
        self.page.close(self.drawer)