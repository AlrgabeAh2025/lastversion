from flet import *
import requests


class Home(View):

    def __init__(self, route, page):
        super().__init__(route=route)
        self.scroll = ScrollMode.AUTO
        self.page = page
        self.baseUrl = "http://127.0.0.1:8000"
        self.innerChild = {}
        self.children = []
        self.childrenList = []

        self.drawer = NavigationDrawer(
            on_dismiss=self.handle_dismissal,
            on_change=self.handle_change,
            controls=[
                Container(height=12),
                NavigationDrawerDestination(
                    label="الرئيسية",
                    icon_content=Icon(icons.HOME_OUTLINED),
                    selected_icon_content=Icon(icons.HOME),
                ),
                Divider(thickness=2),
                NavigationDrawerDestination(
                    label="الاجهزة المرتبطة",
                    icon_content=Icon(icons.PHONE_ANDROID_OUTLINED),
                    selected_icon_content=Icon(icons.PHONE_ANDROID),
                ),
                NavigationDrawerDestination(
                    label="تسجيل الخروج",
                    icon_content=Icon(icons.LOGOUT_OUTLINED),
                    selected_icon_content=Icon(icons.LOGOUT),
                ),
            ],
        )

        self.appbar = AppBar(
            actions=[
                IconButton(
                    icon=icons.PERSON,
                    icon_color="#ffffff",
                    on_click=lambda x: self.page.go("/Profile"),
                ),
                IconButton(
                    icon=icons.NOTIFICATIONS,
                    icon_color="#ffffff",
                    on_click=lambda x: self.page.go("/notifications"),
                ),
            ],
            leading=IconButton(
                icon=icons.MENU,
                icon_color="#ffffff",
                on_click=lambda e: self.page.open(self.drawer),
            ),
            toolbar_height=100,
            title=Text(
                "وصلة",
                size=30,
                weight=FontWeight.BOLD,
                color="#ffffff",
                font_family="ElMessiri",
            ),
        )

        loader = self.loaderUi()
        self.controls.append(loader)

    def loaderUi(self):
        self.scroll = None
        return Column(
            controls=[
                Container(
                    content=ProgressRing(visible=True),  # Progress ring loader
                    alignment=alignment.center,
                    height=float("inf"),  # Make the container take full height
                    expand=True,  # Ensure the container expands to fill available space
                ),
            ],
            expand=True,  # Make the column expand to take up all available space
        )

    def handle_dismissal(self, e):
        self.page.add(Text("Drawer dismissed"))

    def handle_change(self, e):
        routs = {
            "0": "/home",
            "1": "/devices",
            "2": "/",
        }
        self.page.client_storage.clear()
        self.page.go(routs[e.data])
        self.page.close(self.drawer)

    def did_mount(self):
        refresh = self.page.client_storage.get("refresh")
        task = self.page.run_task(self.checkAccessToken, refresh)
        if task.result()[0]:
            self.page.client_storage.set("access", task.result()[1])
            self.page.client_storage.set("refresh", task.result()[2])
            self.page.run_task(self.loadChildren, task.result()[1])
        else:
            self.page.client_storage.clear()
            self.page.go("/")

    def buildHasChildrenUi(self):
        self.scroll = ScrollMode.AUTO
        self.controls.clear()
        self.controls.append(
            ResponsiveRow(
                controls=[
                    Dropdown(
                        label="اختر احد الابناء لعرض بياناته",
                        width=100,
                        options=self.childrenList,
                        label_style=TextStyle(
                            size=13,
                            weight=FontWeight.NORMAL,
                            font_family="ElMessiri",
                        ),
                        on_change=self.changeSelectedChild,
                    ),
                    Container(height=10),
                    Column(
                        controls=[
                            Container(
                                content=Image(
                                    src=(
                                        "/images/BChild.png"
                                        if self.innerChild["childData"]["child_gender"]
                                        == "1"
                                        else "/images/GChild.png"
                                    ),
                                    width=150,
                                ),
                                border_radius=border_radius.all(150),
                            ),
                            Container(
                                content=Text(
                                    f"({self.innerChild['childData']['child_first_name']})",
                                    size=20,
                                    weight=FontWeight.BOLD,
                                    color="#666666",
                                    font_family="ElMessiri",
                                ),
                            ),
                            Container(
                                content=Text(
                                    "اخر موعد اتصال",
                                    size=8,
                                    weight=FontWeight.NORMAL,
                                    color="#666666",
                                    font_family="ElMessiri",
                                ),
                            ),
                            Container(height=20),
                            ResponsiveRow(
                                controls=[
                                    Text(
                                        "قائمة الاختصارات",
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
                                        content=Column(
                                            controls=[
                                                Icon(
                                                    icons.WIDGETS,
                                                    size=50,
                                                    color="#110b22",
                                                ),
                                                Text(
                                                    "استخدام التطبيقات",
                                                    style=TextStyle(
                                                        size=11,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                        color="#666666",
                                                    ),
                                                ),
                                            ],
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                            alignment=MainAxisAlignment.SPACE_AROUND,
                                        ),
                                        padding=10,
                                        alignment=alignment.center,
                                        height=120,
                                        border_radius=10,
                                        col={"xs": 6, "sm": 10, "md": 5, "xl": 5},
                                        border=border.all(width=1, color="#110b22"),
                                        on_click=lambda x: self.page.go(
                                            "/MostUsedApplications"
                                        ),
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Icon(
                                                    icons.SECURITY,
                                                    size=50,
                                                    color="#110b22",
                                                ),
                                                Text(
                                                    "التنبيهات",
                                                    style=TextStyle(
                                                        size=11,
                                                        weight=FontWeight.BOLD,
                                                        font_family="ElMessiri",
                                                        color="#666666",
                                                    ),
                                                ),
                                            ],
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                            alignment=MainAxisAlignment.SPACE_AROUND,
                                        ),
                                        padding=10,
                                        alignment=alignment.center,
                                        height=120,
                                        border_radius=10,
                                        col={"xs": 6, "sm": 10, "md": 5, "xl": 5},
                                        border=border.all(width=1, color="#110b22"),
                                        on_click=lambda x: self.page.go(
                                            "/notifications"
                                        ),
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                col={"sm": 2, "md": 4, "xl": 2},
                            ),
                            ResponsiveRow(
                                controls=[
                                    Text(
                                        "التطبيقات الاكثر استخدام",
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
                                    controls=self.innerChild["apps"],
                                ),
                                bgcolor="#ffffff",
                                border=border.all(0.5, "#110b22"),
                                border_radius=border_radius.all(5),
                                alignment=alignment.center,
                            ),
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                expand=True,
            )
        )
        self.update()

    def buildHasNoChild(self):
        self.controls.clear()
        self.controls.append(
            ResponsiveRow(
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                ListTile(
                                    leading=Icon(icons.INFO),
                                    title=Text(
                                        "انت لم تضف جهاز بعد الرجاء اضافة جهاز اولا",
                                        size=13,
                                        weight=FontWeight.NORMAL,
                                        color="#666666",
                                        font_family="ElMessiri",
                                    ),
                                ),
                                Container(
                                    content=Text(
                                        "اولا اضغط على الزر بالاسفل لمسح رمز (QR) على جهاز طفلك ثم يمكنك الحصول على اشعارات فورية بخصوص المحتوى الذي يتابعه طفلك والعديد من المعلومات الاخرى",
                                        size=13,
                                        weight=FontWeight.NORMAL,
                                        color="#666666",
                                        font_family="ElMessiri",
                                    ),
                                    padding=20,
                                ),
                            ]
                        ),
                        bgcolor="#ffffff",
                        border=border.all(color="#110b22", width=1),
                        border_radius=border_radius.all(10),
                    ),
                    Container(height=30),
                    Container(
                        content=Text(
                            "اضغط لاضافة جهاز",
                            size=13,
                            weight=FontWeight.NORMAL,
                            color="#666666",
                            font_family="ElMessiri",
                        ),
                    ),
                    Container(
                        content=Column(
                            controls=[
                                IconButton(icon=icons.QR_CODE, icon_size=120),
                                Container(
                                    content=Text(
                                        "امسح رمز (QR) على جهاز طفلك",
                                        size=14,
                                        weight=FontWeight.NORMAL,
                                        color="#666666",
                                        font_family="ElMessiri",
                                    ),
                                ),
                            ],
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        bgcolor="#ffffff",
                        border=border.all(color="#110b22", width=1),
                        border_radius=border_radius.all(10),
                        padding=padding.symmetric(vertical=20),
                    ),
                ],
                expand=True,
            )
        )
        self.update()

    def changeSelectedChild(self, event):
        self.innerChild["childData"] = self.children[int(event.data)]["childData"]
        self.innerChild["apps"] = self.children[int(event.data)]["apps"]
        self.buildHasChildrenUi()

    async def sendPostRequest(self, url, body={}, headers=None):
        headers = (
            headers
            if headers is not None
            else {
                "Content-Length": "165",
                "Content-Type": "application/json",
                "User-Agent": "PostmanRuntime/7.39.1",
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Host": "127.0.0.1:8000",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }
        )
        try:
            response = requests.post(url=f"{self.baseUrl}/{url}/", data=body)
            json = response.json()
            if response.status_code == 200:
                return [True, json , response.status_code]
            else:
                return [False, json ,response.status_code ]
        except requests.exceptions.Timeout:
            return [False, "اتصال الانترنت بطئ"]
        except requests.exceptions.ConnectionError:
            return [False, "حدث خطأ في الاتصال بالخادم. تحقق من اتصالك بالإنترنت."]

    async def sendGetRequest(self, url, body={}, access=None):
        headers = {
            "Content-Length": "165",
            "Content-Type": "multipart/form-data; boundary=--------------------------954726683782670649146059",
            "Authorization": f"Bearer {access}",
            "User-Agent": "PostmanRuntime/7.39.1",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Host": "127.0.0.1:8000",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }
        try:
            response = requests.get(
                url=f"{self.baseUrl}/{url}/", data=body, headers=headers
            )
            json = response.json()
            if response.status_code == 200:
                return [True, json]
            else:
                return [False, json]
        except requests.exceptions.Timeout:
            return [False, "اتصال الانترنت بطئ"]
        except requests.exceptions.ConnectionError:
            return [False, "حدث خطأ في الاتصال بالخادم. تحقق من اتصالك بالإنترنت."]

    async def checkAccessToken(self, refresh):
        state, result , statusCode = await self.sendPostRequest(
            url="refresh", body={"refresh": refresh}
        )
        if state:
            return [state, result["access"], result["refresh"]]
        else:
            return [state]

    async def loadChildren(self, access):
        state, result = await self.sendGetRequest("Children", access=access)
        if state and len(result) > 0:
            for index, childData in enumerate(result.values()):
                self.childrenList.append(
                    dropdown.Option(
                        content=Text(f'{childData[0]["child_first_name"]}'), text=index
                    )
                )
                self.children.append(
                    {
                        "childData": childData[0],
                        "apps": [
                            ListTile(
                                title=Text(
                                    f"{app['hour']}",
                                    style=TextStyle(
                                        size=10,
                                        weight=FontWeight.BOLD,
                                        font_family="ElMessiri",
                                    ),
                                ),
                                leading=Text(
                                    f"{app['appName']}",
                                    style=TextStyle(
                                        size=15,
                                        weight=FontWeight.BOLD,
                                        font_family="ElMessiri",
                                    ),
                                ),
                                trailing=Icon(icons.FACEBOOK),
                                subtitle=ProgressBar(value=0.8),
                            )
                            for app in childData[1]
                        ],
                    }
                )
            self.innerChild["childData"] = self.children[0]["childData"]
            self.innerChild["apps"] = self.children[0]["apps"]
            self.buildHasChildrenUi()
        else:
            self.buildHasNoChild()
