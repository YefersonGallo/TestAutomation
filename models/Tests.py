from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


class Test:
    def __init__(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("http://pruebas.monolegal.co/")

    def create_user(self, name, email, password):
        driver = self.driver
        driver.find_element_by_xpath("//a[@href='https://pruebas.monolegal.co/registrate-de-inmediato']").click()
        driver.save_screenshot("Screenshot_Singup.png")
        driver.find_element_by_name("NombreApellidos").send_keys(name)
        driver.find_element_by_name("Email").send_keys(email)
        driver.find_element_by_name("PasswordRegister").send_keys(password)
        driver.find_element_by_xpath("//label[@for='acepto']").click()
        driver.find_element_by_id("btnRegistro").click()

    def login(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[text()='Iniciar sesión']").click()
        # driver.find_element_by_name("UserName").send_keys("jotiwaw592@tibui.com")
        # driver.find_element_by_name("Password").send_keys("test1234")
        driver.find_element_by_name("UserName").send_keys("demomintic@gmail.com ")
        driver.find_element_by_name("Password").send_keys("monolegaldemo")
        # driver.find_element_by_name("UserName").send_keys(email)
        # driver.find_element_by_name("Password").send_keys(password)
        driver.find_element_by_xpath("//div[@class='btn-login']").find_element_by_xpath(
            "//button[@type='submit']").click()

    def show_tutorial(self):
        self.login()
        driver = self.driver
        if len(driver.find_elements_by_id('tutorial-conozco')) != 0:
            return True
        return False

    def create_process(self):
        self.login()
        driver = self.driver
        driver.implicitly_wait(5)
        select_element = driver.find_element_by_id("Ciudad")
        select_object = Select(select_element)
        select_object.select_by_visible_text("Bogotá")
        select_element = driver.find_element_by_id("Corporaciones")
        select_object = Select(select_element)
        select_object.select_by_visible_text("JUZGADOS LABORALES DEL CIRCUITO DE BOGOTA ")
        driver.find_element_by_name("NumProceso").send_keys("11001310500520010034000")
        driver.find_element_by_xpath("//button[text()='Añadir']").click()

    def red_ball_new_process(self):
        self.login()
        driver = self.driver
        driver.implicitly_wait(5)
        print(driver.find_element_by_xpath(
            '//li[@data-bind="visible: FlagMostrarNotificacionesPendientes"]/a[@class="js-nav"]/span[@class="jewelCount"]').text == '')
        print(driver.find_element_by_xpath(
            '//li[@data-bind="visible: FlagMostrarNotificacionesPendientes"]/a[@class="js-nav"]/span[@class="jewelCount"]').text)
        driver.find_element_by_xpath('//a[@data-bind="click: $root.MostrarNotificaciones"]').click()
        print(driver.find_element_by_xpath(
            '//li[@data-bind="visible: FlagMostrarNotificacionesPendientes"]/a[@class="js-nav"]/span[@class="jewelCount"]').text != 0)

    def yellow_notification(self):
        self.login()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//a[@data-bind="click: $root.MostrarNotificaciones"]').click()
        print(driver.find_element_by_class_name("recordatorio novisto").value_of_css_property('background-color'))

    def button_do_it_now(self):
        self.login()
        driver = self.driver
        driver.find_element_by_id("btnHazloExtensionInterno").click()

    def search_add_rama_judicial(self):
        self.login()
        driver = self.driver
        driver.find_elements_by_id("btnAñadeRamaInterno").click()

    def download_report(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath('//a/img[@title="Descargar Informe"]').click()

    def create_process_error(self):
        self.login()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//select[@name="Ciudad"]/option[text()="APARTADO"]').click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath(
            '//select[@name="Corporaciones"]/option[@value="dfc38a08-d387-4109-9a53-c07c5feecd3c"]').click()
        driver.find_element_by_name("NumProceso").send_keys("12345682946392273942730")
        driver.find_element_by_xpath("//button[text()='Añadir']").click()

    def add_label(self):
        self.login()
        driver = self.driver
        driver.find_element_by_id("11001310500520010034000").click()
        button = driver.find_element_by_xpath('//button[text()="Añadir Etiqueta"]')
        driver.execute_script("arguments[0].click();", button)
        driver.implicitly_wait(3)
        print(driver.find_element_by_id("etiquetaProcesoinput").is_displayed())
        driver.find_element_by_id("etiquetaProcesoinput").send_keys("Etiqueta")
        element = driver.find_element_by_xpath('//button[@data-bind="click: ConfirmarCambiarEtiqueta"]')
        driver.execute_script("arguments[0].click();", element)

    def create_comment(self):
        self.login()
        driver = self.driver
        driver.find_element_by_id("05001310500520140119800").click()
        time.sleep(3)
        driver.find_element_by_xpath('//img[@title="Comentarios"]').click()
        comments = driver.find_element_by_class_name("comentarios-contenedor")
        driver.find_element_by_id("txtComentario").send_keys("Comentario de prueba")
        element = comments.find_element_by_xpath("//div[@class='senviar']/button[text()='Ok']")
        driver.execute_script("arguments[0].click();", element)

    def create_reminder_last_date(self):
        self.login()
        driver = self.driver
        driver.find_element_by_id("05001310500520140119800").click()
        driver.implicitly_wait(5)
        driver.find_element_by_id("txtComentario2").send_keys("RecordatorioPasado")
        driver.find_element_by_xpath('//button[@data-value="otro"]').click()
        driver.find_element_by_xpath('//input[@data-bind="datepicker: FechaRecordatorio"]').click()
        driver.find_element_by_class_name("prev").click()
        driver.find_element_by_xpath('//td[@class="day"]').click()
        comments = driver.find_element_by_class_name("comentarios-contenedor")
        element = comments.find_element_by_xpath("//div[@class='senviar']/button[text()='Ok']")
        driver.execute_script("arguments[0].click();", element)

    def create_reminder_future_date(self):
        self.login()
        driver = self.driver
        driver.find_element_by_id("05001310500520140119800").click()
        driver.implicitly_wait(5)
        print(len(driver.find_elements_by_xpath('//img[@src="/Content/appland/images/alarma.png"]')))
        driver.find_element_by_id("txtComentario2").send_keys("RecordatorioFuturo")
        driver.find_element_by_xpath('//button[@data-value="1"]').click()
        comments = driver.find_element_by_class_name("comentarios-contenedor")
        element = comments.find_element_by_xpath("//div[@class='senviar']/button[text()='Ok']")
        driver.execute_script("arguments[0].click();", element)
        print(len(driver.find_elements_by_xpath('//img[@src="/Content/appland/images/alarma.png"]')))

    def delete_reminder_from_reminders(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath('//a[@data-bind="click: $root.MostrarRecordatorios"]').click()
        reminders = driver.find_elements_by_xpath('//div[@class="recordatorio recordatorio_futuro"]')
        len(reminders)

    def create_report(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath("//span[text()='Crear Mi Informe']").click()
        source_element = driver.find_element_by_id("ultimoComentario")
        dest_element = driver.find_element_by_id("sortable1")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("ultimas5Actuaciones")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("ultimaActuacion")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("planConsulta")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("ponente")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("ultimoPantallazo")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("etiqueta")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("ubicacionExpediente")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        source_element = driver.find_element_by_id("Contenido")
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
        select_element = driver.find_element_by_id("OrdenarPor")
        select_object = Select(select_element)
        select_object.select_by_visible_text("Ordenar por termino más cercano")
        select_element = driver.find_element_by_id("FiltrarPor")
        select_object = Select(select_element)
        select_object.select_by_visible_text("Todos los procesos")
        driver.find_element_by_id("RepetirDomingo").click()
        driver.find_element_by_id("Nombre").send_keys("Prueba informe personalizado")
        driver.find_element_by_id("Descripcion").send_keys("Prueba informe personalizado")
        driver.find_element_by_id("CorreosAdicionales").send_keys("diego@monolegal.co,ivan@monolegal.co")
        driver.find_element_by_id("settings_save").click()

    def upload_document(self):
        import os
        self.login()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_id("11001310500520010034000").click()
        time.sleep(5)
        driver.find_element_by_xpath('//img[@title="Documentos"]').click()
        driver.find_element_by_xpath("//button[text()='Subir']").click()
        driver.find_element_by_id("filedocumentos").send_keys(os.path.abspath("../docs/637401236725000860.pdf"))
        driver.find_element_by_xpath("//button[@data-bind='click: $root.EnviarDocumento']").click()

    def change_name_document(self):
        self.login()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_id("11001310500520010034000").click()
        time.sleep(5)
        driver.find_element_by_xpath('//img[@title="Documentos"]').click()
        driver.find_element_by_class_name("proceso-cabecera").click()
        time.sleep(5)
        driver.find_element_by_xpath('//button[text()="Cambiar Nombre"]').click()
        old_name = driver.find_element_by_id("nombredoctinput").get_attribute("value")
        driver.find_element_by_id("nombredoctinput").clear()
        driver.find_element_by_id("nombredoctinput").send_keys("New_Name_Doc.pdf")
        driver.find_element_by_xpath('//button[@data-bind="click: $root.ConfirmarCambiarNombreDocumento"]').click()
        driver.find_element_by_xpath('//button[text()="Descargar"]').click()
        driver.find_element_by_xpath('//button[text()="Cerrar"]').click()
        time.sleep(60)
        driver.find_element_by_xpath('//a[@data-bind="click: $root.MostrarNotificaciones"]').click()
        notifications = driver.find_element_by_id("stream-notificaciones-id")
        print(notifications.find_element_by_class_name(
            "cuerpo_notificacion").text == 'Ha cambiado el nombre "' + old_name + '" por "' + new_name + '"')

    def delete_doc(self):
        self.login()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_id("11001310500520010034000").click()
        time.sleep(5)
        driver.find_element_by_xpath('//img[@title="Documentos"]').click()
        driver.find_element_by_xpath(
            '//div[@class="proceso-cabecera"]/span/a[@data-bind="click:$root.MostrarDocumento, text:Nombre"]').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//button[@data-bind="click: $root.BorrarDocument"]').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//button[@data-bind="click: $root.EliminarDocumento"]').click()
        # time.sleep(60)
        # driver.find_element_by_xpath('//a[@data-bind="click: $root.MostrarNotificaciones"]').click()
        # notifications = driver.find_element_by_id("stream-notificaciones-id")
        # print(notifications.find_element_by_xpath("//div[@class='proceso-cabecera']/span").text)

    def change_days(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath('//a[text()="Pagina de Perfil"]').click()
        driver.find_element_by_xpath('//div[@data-bind="with: PlanPorDefecto"]').click()
        driver.find_element_by_id("2diasMaJu").click()
        time.sleep(5)
        driver.find_element_by_xpath('//button[text()="Cambiar el plan"]').click()

    def add_associated(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath('//a[text()="Pagina de Perfil"]').click()
        driver.find_element_by_id("anadirusuario").click()
        driver.find_element_by_id("NombreApellidos").send_keys("Fundadores")
        driver.find_element_by_id("Email").send_keys("founders@monolegal.co")
        driver.find_element_by_id("settings_save").click()

    def add_billing_information(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath('//a[text()="Pagina de Perfil"]').click()
        driver.find_element_by_id("Abogado_Nit").clear()
        driver.find_element_by_id("Abogado_Direccion").clear()
        driver.find_element_by_id("Abogado_Ciudad").clear()
        driver.find_element_by_id("Abogado_Departamento").clear()
        driver.find_element_by_id("Abogado_Telefono").clear()
        driver.find_element_by_id("Abogado_Nit").send_keys("9008180141")
        driver.find_element_by_id("Abogado_Direccion").send_keys("Av Norte # 47 A 40 Lc 101")
        driver.find_element_by_id("Abogado_Ciudad").send_keys("Tunja")
        driver.find_element_by_id("Abogado_Departamento").send_keys("Boyacá")
        driver.find_element_by_id("Abogado_Telefono").send_keys("3162458413")
        driver.find_element_by_id("settings_save").click()

    def go_TYBA(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath("//a[text()='TYBA']").click()
        print(len(driver.find_elements_by_xpath('//div[@class="stream home-stream"]/ol[@class="stream-items"]')) == 0)

    def go_RamaJudicial(self):
        self.login()
        driver = self.driver
        driver.find_element_by_xpath("//a[text()='TYBA']").click()
        driver.find_element_by_xpath("//a[text()='Rama Judicial']").click()


test = Test()
test.delete_reminder_from_reminders()
