from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle, RoundedRectangle, Ellipse


# Ajustamos tamaño de la ventana
Window.size = (400, 600)

# Colores tema oscuro personalizados
backgroundColor = (1, 0.772, 0.149, 1)  # Fondo Amarillo
backgroundColor1 = (1, 1, 1, 1)         # Fondo Blanco
backgroundColor2 = (1, 0.922, 0.710, 1) #Color beesh
textColor = (1, 1, 1, 1)                # Texto blanco
textColor1 = (0, 0, 0, 1)               # Texto Negro
MainButonColor = (0, 0, 0, 1)           # Color Negro del botón
MainButonColor1 = (1, 1, 1, 1)          # Color Blanco del botón
AlertButonColor = (1, 0.4, 0.4, 1)      # Rojo para botón de salir
SecondButonColor = (0.5, 0.5, 0.5, 1)  # Gris para volver

# Usuarios válidos
usuarios = {
    "MicaelaJuares": "Mica",
    "Holi": "0987"
}

# Para redondear botones
def redondear_boton(boton, color):
    with boton.canvas.before:
        Color(*color)
        boton.bg_rect = RoundedRectangle(size=boton.size, pos=boton.pos, radius=[10])
    boton.bind(size=lambda *x: setattr(boton.bg_rect, 'size', boton.size))
    boton.bind(pos=lambda *x: setattr(boton.bg_rect, 'pos', boton.pos))
    boton.background_normal = ''
    boton.background_down = ''
    boton.background_color = (0, 0, 0, 0)


# Pantalla de bienvenida
class BienvenidaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        layout.add_widget(Label(text="¡Bienvenido a Parking-SV!", font_size=30, size_hint=(1, 0.1), color=textColor))
        layout.add_widget(Image(source='circulo2.jfif', size_hint=(0.1, 0.2), allow_stretch=True))
        layout.add_widget(Image(source='Logo2.png', size_hint=(1, 1), allow_stretch=True))
        layout.add_widget(Image(source='Circulo1.jfif', size_hint=(2, 0.15), allow_stretch=True))
        layout.add_widget(Label(text="Parquea sin estrés, llega a tiempo con Parking-SV", font_size=20, size_hint=(1, 0.1), color=textColor1, text_size=(340, None)))

        btn_ingresar = Button(
            text="Ingresar Ahora",
            size_hint=(1, 0.1),
            font_size=20,
            color=textColor
        )
        redondear_boton(btn_ingresar, MainButonColor)
        btn_ingresar.bind(on_press=self.ir_a_login)

        layout.add_widget(btn_ingresar)
        self.add_widget(layout)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def ir_a_login(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'login'

# Pantalla de login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        self.layout.add_widget(Label(text="Iniciar sesión", font_size=30, size_hint=(1, 0.2), color=textColor))
        self.layout.add_widget(Image(source='Logo2.png', size_hint=(1, 0.5), allow_stretch=True))
        self.layout.add_widget(Label(text="Bienvenido a Parking-SV", font_size=20, size_hint=(1, 0.2), color=textColor))

        self.usuario = TextInput(
            hint_text="Usuario",
            multiline=False,
            size_hint=(1, 0.2),
            font_size=18,
            foreground_color=textColor1,
            background_color=(1, 1, 1, 1),
            cursor_color=textColor1
        )
        self.clave = TextInput(
            hint_text="Contraseña",
            password=True,
            multiline=False,
            size_hint=(1, 0.2),
            font_size=18,
            foreground_color=textColor1,
            background_color=(1, 1, 1, 1),
            cursor_color=textColor1
        )

        btn_mostrar = Button(
            text="👁 Mostrar contraseña",
            size_hint=(1, None),
            height=40,
            color=textColor1
        )

        btn_mostrar.bind(on_press=self.mostrar_contrasena)
        self.layout.add_widget(btn_mostrar)
        self.layout.add_widget(self.usuario)
        self.layout.add_widget(self.clave)

        btn_ingresar = Button(
            text="Ingresar",
            size_hint=(1, None),
            height=45,
            font_size=20,
            color=textColor
        )
        redondear_boton(btn_ingresar, MainButonColor)
        btn_ingresar.bind(on_press=self.validar_login)

        btn_register = Button(
            text="Registrate ahora!",
            size_hint=(1, 0.2),
            font_size=16,
            color=textColor
        )
        redondear_boton(btn_register, SecondButonColor)
        btn_register.bind(on_press=self.ir_a_register)

        btn_volver = Button(
            text="Volver",
            size_hint=(1, 0.2),
            font_size=16,
            color=textColor
        )
        redondear_boton(btn_volver, SecondButonColor)
        btn_volver.bind(on_press=self.volver)

        self.layout.add_widget(btn_ingresar)
        self.layout.add_widget(btn_register)
        self.layout.add_widget(btn_volver)

        self.add_widget(self.layout)

    def mostrar_contrasena(self, instance):
        self.clave.password = not self.clave.password
        if self.clave.password:
            instance.text = "👁 Mostrar contraseña"
        else:   
            instance.text = "🙈 Ocultar contraseña"

    def ir_a_register(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'register'

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def validar_login(self, instance):
        user = self.usuario.text.strip()
        pwd = self.clave.text.strip()
        if user in usuarios and usuarios[user] == pwd:
            self.manager.get_screen('inicio').usuario = user
            self.manager.transition.direction = 'left'
            self.manager.current = 'inicio'
            self.usuario.text = ''
            self.clave.text = ''
        else:
            Popup(title="Error",
                  content=Label(text="Usuario o contraseña incorrectos."),
                  size_hint=(0.6, 0.3)).open()

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'bienvenida'
        
#Pantalla de Registrarte
class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0.772, 0.149, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._actualizar_rect, pos=self._actualizar_rect)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        # Encabezado
        header = BoxLayout(size_hint=(1, 0.1), padding=10)
        label = Label(text='[b] Registrarse[/b]', markup=True, font_size=32, color=(0, 0, 0, 1))
        header.add_widget(label)
        layout.add_widget(header)

        layout.add_widget(Image(source='Logo2.png', size_hint=(1, 1)))
        layout.add_widget(Label(text="Bienvenido a Parking-SV", font_size=25, size_hint=(1, 0.1), color=(1, 1, 1, 1)))

        # Campos
        name_input = TextInput(hint_text='Nombre', size_hint=(1, 0.4), multiline=False, background_color=(1, 1, 1, 1), font_size=18)
        email_input = TextInput(hint_text='Fecha de nacimiento', size_hint=(1, 0.4), multiline=False, background_color=(1, 1, 1, 1), font_size=18)
        password_input = TextInput(hint_text='Correo', size_hint=(1, 0.4), multiline=False, password=True, background_color=(1, 1, 1, 1), font_size=18)
        confirm_input = TextInput(hint_text='Contraseña', size_hint=(1, 0.4), multiline=False, password=True, background_color=(1, 1, 1, 1), font_size=18)

        layout.add_widget(name_input)
        layout.add_widget(email_input)
        layout.add_widget(password_input)
        layout.add_widget(confirm_input)

        # Botón final
        login_button = Button(text='Registrarse', background_color=(0.1, 0.1, 0.1, 1), color=(1, 1, 1, 1), size_hint=(1, 0.4), font_size=18)
        layout.add_widget(login_button)

        volver_button = Button(text='Volver', background_color=(0.1, 0.1, 0.1, 1), color=(1, 1, 1, 1), size_hint=(1, 0.4), font_size=18)
        volver_button.bind(on_press=self.ir_a_login)
        layout.add_widget(volver_button)
        
        
        self.add_widget(layout)

    def _actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
    
    def ir_a_login(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'

    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'


# Pantalla Homepage
class InicioScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu_abierto = False
        self.root_layout = FloatLayout()  # Nuevo contenedor principal

        # Fondo y canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)  # backgroundColor1
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # ------------ LAYOUT ORIGINAL (NO CAMBIADO) ------------
        main_layout = BoxLayout(orientation='vertical')

        main_layout.add_widget(self._crear_top_bar())

        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', size_hint_y=None, padding=20, spacing=20)
        content.bind(minimum_height=content.setter('height'))

        content.add_widget(Label(text="Parking-SV", font_size=32, color=(0, 0, 0, 1), size_hint_y=None, height=50))
        content.add_widget(Label(text="[b]Todos nos enfrentamos a esta problemática[/b]\nEn El Salvador y en el mundo.",
                                 markup=True, font_size=20, halign="center", size_hint_y=None, height=80,
                                 color=(0, 0, 0, 1), text_size=(340, None)))
        content.add_widget(Image(source='Trafico.jfif', size_hint_y=None, height=200))

        content.add_widget(Label(
            text="Cada día, miles de nosotros perdemos tiempo, dinero y energía buscando parqueo. "
                 "El tráfico y la falta de información dificultan estacionarse con eficiencia. "
                 "\nParking SV nace como una solución rápida y confiable para encontrar espacios disponibles, "
                 "sin estrés ni pérdidas de tiempo.",
            font_size=16,font_name="Inter_18pt-Italic.ttf", halign="center", size_hint_y=None, height=120, color=(0.2, 0.2, 0.2, 1), text_size=(340, None)
        ))

        btn1 = Button(text="¡Empezar ya!", size_hint_y=None, height=50, color=(1, 1, 1, 1))
        redondear_boton(btn1, (0, 0, 0, 1))
        btn2 = Button(text="¡Publicar mi espacio ya!", size_hint_y=None, height=50, color=(1, 1, 1, 1))
        redondear_boton(btn2, (0, 0, 0, 1))
        content.add_widget(btn1)
        content.add_widget(btn2)

        content.add_widget(Label(text="[b]¡Parking SV tiene la solución![/b]", markup=True, font_size=20,
                                 size_hint_y=None, height=40, color=(0, 0, 0, 1)))
        content.add_widget(Label(
            text="Parking SV es la solución inteligente, rápida y local para conectar personas que necesitan parqueo "
                 "con quienes tienen un espacio disponible. Sin complicaciones, sin perder tiempo, todo en minutos y sin estrés.",
            font_size=16,font_name="Inter_18pt-Italic.ttf", size_hint_y=None, height=100, color=(0.2, 0.2, 0.2, 1), text_size=(340, None)
        ))

        content.add_widget(Image(source='Mapa.jfif', size_hint_y=None, height=180))

        content.add_widget(Label(text="[b]¿Cómo funciona?[/b]", markup=True, font_size=20,
                                 size_hint_y=None, height=40, color=(0, 0, 0, 1)))
        pasos = [
            "Explorá el mapa en tiempo real",
            "Encontrá parqueos cerca de tu destino",
            "Verificá la reputación del dueño",
            "Seleccioná un parqueo, mira el mapa o usa Waze, ¡y listo!"
        ]
        for paso in pasos:
            content.add_widget(Label(text=paso, font_size=16,font_name="Inter_18pt-Italic.ttf", size_hint_y=None, height=30,
                                     color=(0, 0, 0, 1), text_size=(340, None)))

        content.add_widget(Image(source='Video.jfif', size_hint_y=None, height=180))

        content.add_widget(Label(text="[b]¿Por qué Parking SV?[/b]", markup=True, font_size=20,
                                 size_hint_y=None, height=40, color=(0, 0, 0, 1)))
        razones = [
            "Hecha por salvadoreños, para salvadoreños. Sin comisiones ni apps complicadas.",
            "Comunidad verificada. Ahorro de tiempo y dinero."
        ]
        for razon in razones:
            content.add_widget(Label(text=razon, font_size=16,font_name="Inter_18pt-Italic.ttf", size_hint_y=None, height=50,
                                     color=(0, 0, 0, 1), text_size=(340, None)))

        content.add_widget(Image(source='Team.jfif', size_hint_y=None, height=180))
        content.add_widget(Image(source='Piedepag.jfif', size_hint_y=None, height=400))

        content.add_widget(Label(text="© 2025 Parking SV", font_size=14, size_hint_y=None, height=30,
                                 color=(0, 0, 0, 1)))

        scroll.add_widget(content)
        main_layout.add_widget(scroll)

        self.root_layout.add_widget(main_layout)

        # Menú lateral 
        self.menu = MenuLateral(screen_manager=None)
        self.menu.pos_hint = {'x': -0.8}
        self.root_layout.add_widget(self.menu)

        #Button para abrir el menu lateral
        btn_menu = Button(
            text='☰',
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, Window.height - 60),
            background_normal='',
            background_color=(0, 0, 0, 1),
            color=(1, 1, 1, 1),
            font_size=24
        )
        btn_menu.bind(on_press=self.toggle_menu)
        self.root_layout.add_widget(btn_menu)

        self.add_widget(self.root_layout)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def toggle_menu(self, instance):
        anim = Animation(pos_hint={'x': 0 if not self.menu_abierto else -0.8}, d=0.3)
        anim.start(self.menu)
        self.menu_abierto = not self.menu_abierto

    def on_enter(self):
        self.menu.screen_manager = self.manager 

    def _crear_top_bar(self):
        top_bar = BoxLayout(size_hint_y=None, height=50, orientation='horizontal', padding=[10, 5], spacing=10)
        with top_bar.canvas.before:
            Color(1, 0.772, 0.149, 1)
            rect = Rectangle(size=top_bar.size, pos=top_bar.pos)

        def _update_rect(instance, value):
            rect.pos = instance.pos
            rect.size = instance.size

        top_bar.bind(size=_update_rect, pos=_update_rect)

        top_bar.add_widget(Label(
            text='[b]Inicio[/b]',
            markup=True,
            font_size='20sp',
            font_name="Lato-BlackItalic.ttf",
            color=[0, 0, 0, 1]
        ))

        return top_bar


#Pantalla de Mi Cuenta
class MiCuentaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_abierto = False
        self.root_layout = FloatLayout()

        with self.canvas.before:
            Color(*backgroundColor1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        main_layout = BoxLayout(orientation='vertical')

        main_layout.add_widget(self._crear_top_bar())

        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', size_hint_y=None, padding=20, spacing=20)
        content.bind(minimum_height=content.setter('height'))

        content.add_widget(Label(
                text="[b]Mis Datos[/b]", markup=True, font_size=27,
                                 size_hint_y=None, height=40, color=(0, 0, 0, 1)))
        
        info_box = BoxLayout(orientation='horizontal', size_hint_y=None, spacing=10)
        photo = Image(source='Perfil.jpg', size_hint=(None, None), size=(150, 200))

        info = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        info.bind(minimum_height=info.setter('height'))

        datos = [
            ('Nombre completo:', 'Andre Carolina Rivas Orellana'),
            ('Número de teléfono:', '7690-2330'),
            ('Correo electrónico:', 'andre.rivas@adoc.superate.org.sv'),
            ('Contraseña:', '********')
        ]

        for titulo, detalle in datos:
            info.add_widget(AutoHeightLabel(
                text=f'[b]{titulo}[/b]\n{detalle}',
                markup=True,
                halign='left',
                valign='middle',
                color=[0, 0, 0, 1]
            ))

        info_box.add_widget(photo)
        info_box.add_widget(info)

        def actualizar_altura_info_box(*args):
            info_box.height = max(photo.height, info.height) + 20

        photo.bind(height=actualizar_altura_info_box)
        info.bind(height=actualizar_altura_info_box)

        content.add_widget(info_box)

        content.add_widget(Label(text='[b]Vehículos/s de Transporte[/b]', markup=True, font_size=27,
                                 size_hint_y=None, height=40, color=(0, 0, 0, 1)))
        
        table = GridLayout(cols=2, spacing=5, size_hint_y=None)
        table.bind(minimum_height=table.setter('height'))

        def make_label(text, bold=False):
            return AutoHeightLabel(
                text=f'[b]{text}[/b]' if bold else text,
                markup=True,
                color=[0, 0, 0, 1],
                halign='left',
                valign='middle'
            )

        table.add_widget(make_label('Actualmente conduces:', bold=True))
        table.add_widget(make_label('Tu ubicación (para mejor recomendaciones):', bold=True))
        table.add_widget(make_label('Kia 360\nMoto serpiente\nCamión de carga'))
        table.add_widget(make_label('Zona central, San Salvador\nSan Salvador este, polígono 10'))

        content.add_widget(table)
        # Botones (ejemplo)
        btn1 = Button(text='Editar información', size_hint_y=None, height=50, color=textColor)
        redondear_boton(btn1, MainButonColor)
        btn2 = Button(text='Cerrar sesión', size_hint_y=None, height=50, color=textColor)
        redondear_boton(btn2, MainButonColor)
        content.add_widget(btn1)
        content.add_widget(btn2)

        # Footer
        content.add_widget(Label(text='© 2025 Parking SV', font_size=14, size_hint_y=None, height=30, color=(0, 0, 0, 1)))

        scroll.add_widget(content)
        main_layout.add_widget(scroll)


        # Agregar tu layout sin modificarlo al contenedor flotante
        self.root_layout.add_widget(main_layout)

        # Menú lateral
        self.menu = MenuLateral(screen_manager=None)
        self.menu.pos_hint = {'x': -0.8}
        self.root_layout.add_widget(self.menu)

        # Button para el menu lateral
        btn_menu = Button(
            text='☰',
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, Window.height - 60),
            background_normal='',
            background_color=(0, 0, 0, 1),
            color=(1, 1, 1, 1),
            font_size=24
        )
        btn_menu.bind(on_press=self.toggle_menu)
        self.root_layout.add_widget(btn_menu)

        self.add_widget(self.root_layout)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def toggle_menu(self, instance):
        anim = Animation(pos_hint={'x': 0 if not self.menu_abierto else -0.8}, d=0.3)
        anim.start(self.menu)
        self.menu_abierto = not self.menu_abierto

    def on_enter(self):
        self.menu.screen_manager = self.manager

    def _crear_top_bar(self):
        top_bar = BoxLayout(size_hint_y=None, height=50, orientation='horizontal', padding=[10, 5], spacing=10)

        with top_bar.canvas.before:
            Color(*backgroundColor)
            rect = Rectangle(size=top_bar.size, pos=top_bar.pos)

        def _update_rect(instance, value):
            rect.pos = instance.pos
            rect.size = instance.size

        top_bar.bind(size=_update_rect, pos=_update_rect)

        top_bar.add_widget(Label(
            text='[b]Mi cuenta[/b]',
            markup=True,
            font_size='20sp',
            color=[0, 0, 0, 1]
        ))

        return top_bar


#Clase de AutoHeightLabel para ayudar a la la pantalla "Mi Cuenta"
class AutoHeightLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.bind(texture_size=self.update_height)
        self.text_size = (self.width, None)
        self.bind(width=self.update_text_size)

    def update_height(self, *args):
        self.height = self.texture_size[1]

    def update_text_size(self, instance, width):
        self.text_size = (width, None)

#Pantalla de Contactanos
class ContactanosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_abierto = False
        self.root_layout = FloatLayout()

        # Fondo base (canvas)
        with self.canvas.before:
            Color(*backgroundColor2)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        fondo_layout = FloatLayout()

        # Imagen de fondo
        imagen_fondo = Image(
            source='contactanos.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        fondo_layout.add_widget(imagen_fondo)
    
        main_layout = BoxLayout(orientation='vertical')

        fondo_layout.add_widget(main_layout)  

        self.root_layout.add_widget(fondo_layout)

        #Menu 
        self.menu = MenuLateral(screen_manager=None)
        self.menu.pos_hint = {'x': -0.8}
        self.root_layout.add_widget(self.menu)

        #Button del menu lateral
        btn_menu = Button(
            text='☰',
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, Window.height - 60),
            background_normal='',
            background_color=(0, 0, 0, 1),
            color=(1, 1, 1, 1),
            font_size=24
        )
        btn_menu.bind(on_press=self.toggle_menu)
        self.root_layout.add_widget(btn_menu)

        self.add_widget(self.root_layout)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def toggle_menu(self, instance):
        anim = Animation(pos_hint={'x': 0 if not self.menu_abierto else -0.8}, d=0.3)
        anim.start(self.menu)
        self.menu_abierto = not self.menu_abierto

    def on_enter(self):
        self.menu.screen_manager = self.manager
    

#Clase para crear donde estara cada parqueo en la pantalla de parqueos
class ParkingCard(BoxLayout):
    def __init__(self, name, hours, image_path, callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = 250
        self.padding = 5
        self.spacing = 5
        self.callback = callback
        self.parking_info = {'name': name, 'hours': hours, 'image': image_path}

        with self.canvas.before:
            Color(1, 0.83, 0, 1)  # amarillo
            self.rect = RoundedRectangle(radius=[15])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.add_widget(Image(source=image_path, size_hint_y=0.6))
        self.add_widget(Label(text=name, size_hint_y=0.15, color=(0, 0, 0, 1)))
        self.add_widget(Label(text=hours, size_hint_y=0.1, color=(0, 0, 0, 1)))

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.callback(self.parking_info)
            return True
        return super().on_touch_down(touch)

#Pantala de Parqueos
class ParqueosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_abierto = False  
        self.root_layout = FloatLayout()

        with self.canvas.before:
            Color(*backgroundColor1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        main_layout = BoxLayout(orientation='vertical')

        main_layout.add_widget(self._crear_top_bar())

        #Barra de busqueda
        search_layout = BoxLayout(size_hint_y=None, height=50, padding=10, spacing=10)
        search_box = TextInput(
            hint_text='¡Busca tu parqueo acá!',
            size_hint=(1, 1),
            multiline=False,
            background_normal='',
            background_color=(0.95, 0.95, 0.95, 1),
            padding_y=(12, 12),
            foreground_color=(0, 0, 0, 1)
        )
        search_layout.add_widget(Label(text='🔍', size_hint_x=None, width=30, font_size=18, color=(0, 0, 0, 1)))
        search_layout.add_widget(search_box)
        main_layout.add_widget(search_layout)

        main_layout.add_widget(Label(
            text='Parqueos disponibles',
            size_hint_y=None, height=30, font_size=16, color=(0, 0, 0, 1)
        ))

        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=10, padding=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        parqueos = [
            {'name': "Parqueo La Unión", 'hours': "9:00 AM - 9:00 PM", 'image': "Ejemplo.jfif"},
            {'name': "Parqueo Central", 'hours': "8:00 AM - 8:00 PM", 'image': "Ejemplo.jfif"},
            {'name': "Parqueo Norte", 'hours': "7:00 AM - 10:00 PM", 'image': "Ejemplo.jfif"},
            {'name': "Parqueo Sur", 'hours': "9:00 AM - 7:00 PM", 'image': "Ejemplo.jfif"},
            {'name': "Parqueo Este", 'hours': "9:00 AM - 8:00 PM", 'image': "Ejemplo.jfif"}
        ]

        for parqueo in parqueos:
            card = ParkingCard(
                name=parqueo['name'],
                hours=parqueo['hours'],
                image_path=parqueo['image'],
                callback=self.ver_mas_info
            )
            grid.add_widget(card)

        scroll.add_widget(grid)
        main_layout.add_widget(scroll)

        self.root_layout.add_widget(main_layout)

        #Menu
        self.menu = MenuLateral(screen_manager=None)
        self.menu.pos_hint = {'x': -0.8}
        self.root_layout.add_widget(self.menu)

        #Button para el menu lateral
        btn_menu = Button(
            text='☰',
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, Window.height - 60),
            background_normal='',
            background_color=(0, 0, 0, 1),
            color=(1, 1, 1, 1),
            font_size=24
        )
        btn_menu.bind(on_press=self.toggle_menu)
        self.root_layout.add_widget(btn_menu)

        self.add_widget(self.root_layout)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def ver_mas_info(self, parking_info):
        info_screen = self.manager.get_screen('info')
        info_screen.update_info(parking_info)
        self.manager.current = 'info'

    def _crear_top_bar(self):
        top_bar = BoxLayout(size_hint_y=None, height=50, orientation='horizontal', padding=[10, 5], spacing=10)

        with top_bar.canvas.before:
            Color(*backgroundColor)
            rect = Rectangle(size=top_bar.size, pos=top_bar.pos)

        def _update_rect(instance, value):
            rect.pos = instance.pos
            rect.size = instance.size

        top_bar.bind(size=_update_rect, pos=_update_rect)

        top_bar.add_widget(Label(
            text='[b]Parqueos[/b]',
            markup=True,
            font_size='20sp',
            color=[0, 0, 0, 1]
        ))

        return top_bar

    def toggle_menu(self, instance):
        anim = Animation(pos_hint={'x': 0 if not self.menu_abierto else -0.8}, d=0.3)
        anim.start(self.menu)
        self.menu_abierto = not self.menu_abierto

    def on_enter(self):
        self.menu.screen_manager = self.manager


#Pantalla de Informacion de Parqueos
class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title_label = Label(text='', font_size=20)
        self.details_label = Label(text='', font_size=14)
        self.image = Image(source='')  # imagen que cambia

        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.details_label)
        self.layout.add_widget(self.image)

        btn_volver = Button(text='Volver', size_hint=(None, None), size=(200, 50))
        btn_volver.bind(on_release=self.volver)
        self.layout.add_widget(btn_volver)

        self.add_widget(self.layout)

    def update_info(self, parking_info):
        self.title_label.text = parking_info['name']
        self.details_label.text = f"Horario: {parking_info['hours']}"
        self.image.source = parking_info['image']

    def volver(self, instance):
        self.manager.current = 'main'


# Clare circular image para darle una forma circular al menu
class CircularImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.allow_stretch = True
        self.keep_ratio = True

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.border_circle = Ellipse(pos=self.pos, size=self.size)

        self.bind(pos=self.update_circle, size=self.update_circle)

    def update_circle(self, *args):
        self.border_circle.pos = self.pos
        self.border_circle.size = self.size

#Clase del menu lateral para todas las pantallas
class MenuLateral(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.orientation = 'vertical'
        self.size_hint_x = 0.8
        self.spacing = 12
        self.padding = [20, 40, 20, 20]
        self.pos_hint = {'x': -0.8}

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg = RoundedRectangle(radius=[20, 0, 0, 20], pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)

        # Imagen que cuando le das click te dirige a la pantalla de mi cuenta
        img = CircularImage(source='perfil.jpg')
        img.bind(on_touch_down=self.ir_a_micuenta_si_click)
        self.add_widget(img)

        self.add_widget(Label(text='[b]Andrea Rivas[/b]', markup=True, font_size=18, color=(0, 0, 0, 1), size_hint_y=None, height=30))
        self.add_widget(Label(text='andrea.rivas2026@adoc.superate.org.sv', font_size=14, color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=20))
        self.add_separator()

        botones = [
            ("Inicio", lambda x: self.cambiar_pantalla('inicio')),
            ("Parqueos", lambda x: self.cambiar_pantalla('parqueos')),
            ("Notificaciones", lambda x: self.cambiar_pantalla('notificaciones')),
            ("Contáctanos", lambda x: self.cambiar_pantalla('contactanos')),
            ("Guardados", lambda x: self.cambiar_pantalla('guardados')),
        ]
        for texto, accion in botones:
            self.add_widget(self.create_button(texto, accion))
            self.add_separator()

        self.add_widget(self.create_button("Cerrar sesión", self.salir, color=(1, 0, 0, 1)))

    def ir_a_micuenta_si_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            if self.screen_manager:
                self.screen_manager.current = 'micuenta'

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def create_button(self, texto, accion, color=(0, 0, 0, 1)):
        btn = Button(
            text=texto,
            size_hint_y=None,
            height=40,
            background_normal='',
            background_color=(0.95, 0.95, 0.95, 0.8),
            color=color,
            font_size=16
        )
        btn.bind(on_press=accion)
        return btn

    def add_separator(self):
        with self.canvas:
            Color(0.85, 0.85, 0.85, 1)
            from kivy.graphics import Line
            Line(points=[self.x + 10, self.y, self.x + self.width - 10, self.y], width=1)

    def cambiar_pantalla(self, nombre_pantalla):
        self.screen_manager.current = nombre_pantalla

    def salir(self, instance):
        self.screen_manager.current = 'bienvenida'
        

#Calse pantalla con menu
class PantallaConMenu(Screen):
    def __init__(self, screen_manager, nombre, contenido_texto, **kwargs):
        super().__init__(name=nombre, **kwargs)
        self.menu_abierto = False
        root = FloatLayout()

        self.menu = MenuLateral(screen_manager)
        root.add_widget(self.menu)

        btn_menu = Button(
            text='☰',
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, Window.height - 60),
            background_normal='',
            background_color=(0, 0, 0, 1),
            color=(1, 1, 1, 1),
            font_size=24
        )
        btn_menu.bind(on_press=self.toggle_menu)
        root.add_widget(btn_menu)

        etiqueta = Label(text=contenido_texto, font_size=24, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        root.add_widget(etiqueta)

        self.add_widget(root)

    def toggle_menu(self, instance):
        anim = Animation(pos_hint={'x': 0 if not self.menu_abierto else -0.8}, d=0.3)
        anim.start(self. menu)
        self.menu_abierto = not self.menu_abierto


# App principal
class LoginApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition(duration=0.3))
        sm.add_widget(BienvenidaScreen(name='bienvenida'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(InicioScreen(name='inicio'))
        sm.add_widget(ContactanosScreen(name='contactanos'))
        sm.add_widget(ParqueosScreen(name='parqueos'))
        sm.add_widget(MiCuentaScreen(name='micuenta'))
        sm.add_widget(InfoScreen(name='info'))
        sm.add_widget(PantallaConMenu(sm, 'notificaciones', 'Tus Notificaciones'))
        sm.add_widget(PantallaConMenu(sm, 'guardados', 'Tus elementos guardados'))

        return sm

if __name__ == "__main__":
    LoginApp().run()