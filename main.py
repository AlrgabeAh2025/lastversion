import flet as ft
from PIL import ImageGrab

def capture_screen(page):
    # التقاط لقطة الشاشة
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    page.add(ft.Text("Screenshot saved as screenshot.png"))

def main(page):
    page.title = "Capture Screen Example"
    page.add(ft.ElevatedButton("Capture Screen", on_click=lambda e: capture_screen(page)))

ft.app(target=main)
