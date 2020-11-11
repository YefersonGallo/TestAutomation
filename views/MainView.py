from datetime import datetime
from models import User

class MainView:

    def __init__(self):
        print("Sistema de Automatización de Pruebas")
        self.name = input("Ingrese el nombre del tester:")
        self.emailTest = input("Ingrese el correo del tester:")
        self.serverTest = input("Ingrese el servidor en donde se harán pruebas:")
        self.user = User.Tester(self.name, self.emailTest, datetime.now(), self.serverTest)

    def show_menu(self):
        print("A continuación se muetsran opciones de como desea iniciar las pruebas")
        print("1. Usuario Nuevo")
        print("2. Usuario Antiguo")
        print("3. Usuario Asociado")
        return input("Ingrese la opción con la que va a ingresar:")

    def create_user(self):
        print("Ingrese los datos para crear un nuevo usuario")
        name = input("Ingrese el nombre del usuario nuevo")
        email = input("Ingrese el correo del usuario nuevo")
        password = input("Ingrese la contraseña del usuario nuevo")
        return name, email, password

    def create_process_rama(self):
        print("Ingrese los datos para crear un proceso correcto en Monolegal Rama Judicial")
        city = input("Ingrese el nombre de la ciudad:")
        coporation = input("Ingrese el nombre de la corporación:")
        num_process = input("Ingrese el número de proceso:")
        return city, coporation, num_process
    



view = MainView()
print(view.create_process_rama())