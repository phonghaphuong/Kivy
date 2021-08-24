from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


class WidgetsExample(GridLayout): #Thiết kế các chức năng khác trên Widgets sử sụng GridLayout
    my_text = StringProperty("1")
    text_input_str = StringProperty("Foo")
    count = 1
    count_enable = BooleanProperty(False)
    slider_value_txt = StringProperty("value")

    def on_button_click(self):
        print("Button clicked")
        if self.count_enable:
            self.count += 1
            self.my_text = (str(self.count))

    def on_toggle_button_state(self, widget):
        print("Button State " + widget.state)
        if widget.state == "normal":
            widget.text="OFF"
            self.count_enable = False
        else:
            widget.text="ON"
            self.count_enable = True

    def on_switch_active(self, widget):
        print("switch:" + str(widget.active))

    def on_slider_value(self, widget):
        print("Slider: "+ str(int(widget.value)))
        self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text



#class GridLayoutExample(GridLayout):
#    pass
# Khai báo lớp class tại file PY tương đương khai báo ở KV <GridLayoutExample@GridLayout>:


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    """
    #Đây là kiểu trình bày trực tiếp với Code python
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b3)
        self.add_widget(b2)
"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(1, 0, 1)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=2)
            self.rect = Rectangle(pos=(700, 200), size=(150,100))

    def on_button_a_click(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.ball = Ellipse(poss=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        #print("on size: " + str(self.width) + " , " + str(self.height))
        self.ball.pos = self.center_x - self.ball_size/2, self.center_y-self.ball_size/2

    def update(self, dt):
        #print("update")
        x, y = self.ball.pos
        x += self.vx
        y += self.vy
        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = - self.vy
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = - self.vx

        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = - self.vx

        self.ball.pos = (x, y)


class CanvasExample6(Widget):
    pass


class CanvasExample7(BoxLayout):
    pass


TheLabApp().run()