from flet import *
import requests


class LoginControl:
    def __init__(self, page):
        self.baseUrl = "http://127.0.0.1:8000"
        self.page = page

    def loginRequest(self, userName, password):
        body = {"username": userName, "password": password}
        try:
            response = requests.post(url=f"{self.baseUrl}/login/", data=body)
            json = response.json()
            if response.status_code == 200:
                self.page.client_storage.set("access", json['access'])
                self.page.client_storage.set("refresh",json['refresh'])
                return [True, "تم تسجيل الدخول بنجاح"]
            else:
                return [False, json["non_field_errors"][0]]
        except requests.exceptions.Timeout:
            return [False, "اتصال الانترنت بطئ"]
        except requests.exceptions.ConnectionError:
            return [False, "حدث خطأ في الاتصال بالخادم. تحقق من اتصالك بالإنترنت."]

class Login(View):
    # Constructor: Initializes the login view and sets up the login controls
    def __init__(self, route , page):
        super().__init__(
            route=route
        )  # Calls the constructor of the parent class (View)
        self.loginController = LoginControl(page)  # Initializes the login controller
        self.rtl = True
        self.scroll = ScrollMode.AUTO
        # Creates a username text field with styling and validation options
        self.userNameTextBox = TextField(
            label="اســـم المــستخدم",  # Label in Arabic
            border_radius=border_radius.all(22),  # Rounded borders for the text field
            border_color="#171335",  # Border color
            text_style=TextStyle(
                size=15, font_family="ElMessiri"
            ),  # Text style for input
            label_style=TextStyle(
                size=18, font_family="ElMessiri"
            ),  # Text style for label
        )

        # Creates a password text field with options to reveal password and styling
        self.passwordTextBox = TextField(
            label="كــلمة المــرور",  # Label in Arabic
            password=True,  # Indicates this is a password field
            can_reveal_password=True,  # Option to reveal password
            border_radius=border_radius.all(22),  # Rounded borders for the text field
            border_color="#171335",  # Border color
            text_style=TextStyle(
                size=15, font_family="ElMessiri"
            ),  # Text style for input
            label_style=TextStyle(
                size=18, font_family="ElMessiri"
            ),  # Text style for label
        )

        # A Snackbar to show an error message regarding internet connection
        self.snack_bar = SnackBar(
            content=Text("الرجاء التأكد من اتصال الانترنت لديك"),  # Message in Arabic
            action="Alright!",  # Snackbar action button
        )

        # Initially display the loader or the login UI depending on loading state
        self.content =  self.loginUi()
        # Add the content to the view's controls
        self.controls.append(self.content)

    # Function to generate the login form UI with input fields and login button
    def loginUi(self):
        self.scroll = ScrollMode.AUTO
        return ResponsiveRow(
            controls=[
                Row(
                    controls=[
                        # Back button to navigate to the previous page
                        IconButton(
                            icon=icons.ARROW_BACK,
                            on_click=lambda x: self.page.go("/"),
                        )
                    ],
                    expand=False,
                    alignment=MainAxisAlignment.START,
                ),
                Column(
                    controls=[
                        # Logo image displayed at the top of the login screen
                        ResponsiveRow(
                            controls=[
                                Image(
                                    src="/images/logo.png",  # Logo image source
                                    fit=ImageFit.COVER,  # Image fit type
                                    border_radius=border_radius.all(
                                        20.0
                                    ),  # Rounded corners for the image
                                    col={
                                        "xs": 10,
                                        "sm": 10,
                                        "md": 7,
                                        "lg": 5,
                                        "xl": 5,
                                    },
                                ),
                            ],
                            expand=False,
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        # Title text displayed on top
                        Text(
                            "وصلة",  # Title in Arabic
                            size=30,
                            weight=FontWeight.BOLD,
                            font_family="ElMessiri",
                        ),
                        Container(height=10),  # Spacer between elements
                        self.userNameTextBox,  # Username text box
                        Container(height=10),  # Spacer between elements
                        self.passwordTextBox,  # Password text box
                        Container(height=20),  # Spacer between elements
                        ResponsiveRow(
                            controls=[
                                # Login button to trigger login event
                                ElevatedButton(
                                    "تسجيل الدخول",  # Button label in Arabic
                                    style=ButtonStyle(
                                        shape=RoundedRectangleBorder(
                                            radius=22
                                        ),  # Rounded button corners
                                        bgcolor="#171335",  # Button background color
                                        color="#ffffff",  # Button text color
                                        text_style=TextStyle(
                                            size=15,
                                            weight=FontWeight.BOLD,
                                            font_family="ElMessiri",  # Text style for button text
                                        ),
                                        padding=5,  # Padding for the button
                                    ),
                                    on_click=lambda e: self.LoginEvent(),  # Trigger LoginEvent when clicked
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

    # Function to generate and return the loader UI (Progress Ring)
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

    # Function to handle the login event when the user clicks the login button
    def LoginEvent(self):
        if not self.userNameTextBox.value:  # Check if username is empty
            self.userNameTextBox.error = Text(
                "الرجاء ادخال اسم المستخدم"
            )  # Display error for empty username
            self.update()  # Update the view to show the error
        elif not self.passwordTextBox.value:  # Check if password is empty
            self.passwordTextBox.error = Text(
                "الرجاء ادخال كلمة المرور "
            )  # Display error for empty password
            self.update()  # Update the view to show the error
        else:
            self.userNameTextBox.error = (
                None  # Clear any existing error on the username field
            )
            self.passwordTextBox.error = (
                None  # Clear any existing error on the password field
            )
            self.isLoading = True  # Set loading state to True
            self.controls.clear()  # Clear the current controls from the view
            self.controls.append(self.loaderUi())  # Add the loader UI to show progress
            self.update()  # Update the view to display the loader
            # Simulate login request (authentication process)
            authState = self.loginController.loginRequest(
                self.userNameTextBox.value, self.passwordTextBox.value
            )
            if authState[
                0
            ]:  # If authentication is successful, navigate to the home page
                self.page.go("/home")
            else:  # If authentication fails, revert to the login UI
                self.controls.clear()  # Clear the controls again
                self.controls.append(self.loginUi())  # Add the login form UI back
                snack_bar = SnackBar(
                    content=Text(
                        f"{authState[1]}",
                        style=TextStyle(size=15, font_family="ElMessiri"),
                    ),
                    show_close_icon=True
                )
                self.page.open(snack_bar)
                self.update()  # Update the view to reflect the changes