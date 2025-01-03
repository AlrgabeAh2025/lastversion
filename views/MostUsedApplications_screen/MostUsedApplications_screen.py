from flet import *


class MostUsedApplications(View):
    def __init__(self, route, page):
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
                            Container(height=30),
                            Column(
                                controls=[
                                    ResponsiveRow(
                                        controls=[
                                            Text(
                                                "قائمة التطبيقات",
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
                                    Container(
                                        content=ResponsiveRow(
                                            controls=[
                                                ListTile(
                                                    title=Text(
                                                        "1h:35m",
                                                        style=TextStyle(
                                                            size=10,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    leading=Text(
                                                        "Facebook",
                                                        style=TextStyle(
                                                            size=15,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    trailing=Icon(
                                                        icons.FACEBOOK
                                                    ),
                                                    subtitle= ProgressBar(value=0.8),
                                                ),
                                            ],
                                        ),
                                        bgcolor="#ffffff",
                                        border=border.all(0.5, "#110b22"),
                                        border_radius=border_radius.all(5),
                                        alignment=alignment.center
                                    ),
                                    Container(
                                        content=ResponsiveRow(
                                            controls=[
                                                ListTile(
                                                    title=Text(
                                                        "1h:35m",
                                                        style=TextStyle(
                                                            size=10,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    leading=Text(
                                                        "Facebook",
                                                        style=TextStyle(
                                                            size=15,
                                                            weight=FontWeight.BOLD,
                                                            font_family="ElMessiri",
                                                        ),
                                                    ),
                                                    trailing=Icon(
                                                        icons.FACEBOOK
                                                    ),
                                                    subtitle= ProgressBar(value=0.8),
                                                ),
                                            ],
                                        ),
                                        bgcolor="#ffffff",
                                        border=border.all(0.5, "#110b22"),
                                        border_radius=border_radius.all(5),
                                        alignment=alignment.center
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
