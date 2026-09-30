from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle


class Card(BoxLayout):
    def __init__(self, title, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=dp(8),
            padding=dp(15),
            size_hint_y=None,
            height=dp(190),
            **kwargs
        )

        with self.canvas.before:
            Color(0.08, 0.09, 0.12, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(15)]
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

        self.add_widget(Label(
            text=title,
            font_size="20sp",
            bold=True,
            size_hint_y=None,
            height=dp(35)
        ))

        self.temp = Label(
            text="185.4 °C",
            font_size="30sp",
            bold=True
        )
        self.add_widget(self.temp)

        row = BoxLayout(
            spacing=dp(10),
            size_hint_y=None,
            height=dp(45)
        )

        self.slider = Slider(
            min=0,
            max=100,
            value=70
        )

        self.power = Label(
            text="70 %",
            size_hint_x=None,
            width=dp(60)
        )

        self.slider.bind(
            value=self.change_power
        )

        row.add_widget(self.slider)
        row.add_widget(self.power)

        self.add_widget(row)

        self.button = Button(
            text="ENCENDIDO",
            size_hint_y=None,
            height=dp(40)
        )

        self.button.bind(
            on_press=self.toggle
        )

        self.add_widget(self.button)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def change_power(self, instance, value):
        self.power.text = f"{int(value)} %"

    def toggle(self, instance):
        if instance.text == "ENCENDIDO":
            instance.text = "APAGADO"
        else:
            instance.text = "ENCENDIDO"


class StationApp(App):

    def build(self):

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        # Encabezado
        header = BoxLayout(
            size_hint_y=None,
            height=dp(70),
            orientation="vertical"
        )

        header.add_widget(Label(
            text="ESTACIÓN DE SOLDADURA",
            font_size="25sp",
            bold=True
        ))

        header.add_widget(Label(
            text="● PRUEBA DE INTERFAZ",
            font_size="14sp"
        ))

        root.add_widget(header)

        # Contenido desplazable
        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            padding=dp(3),
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        content.add_widget(
            Card("CAUTÍN PRINCIPAL")
        )

        content.add_widget(
            Card("PLANCHA SMD")
        )

        content.add_widget(
            Card("PISTOLA DE AIRE")
        )

        # Parada de emergencia
        emergency = Button(
            text="🛑 PARADA DE EMERGENCIA",
            size_hint_y=None,
            height=dp(65),
            font_size="18sp",
            bold=True
        )

        content.add_widget(emergency)

        scroll.add_widget(content)
        root.add_widget(scroll)

        return root


if __name__ == "__main__":
    StationApp().run()
