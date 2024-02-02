# >>>  Web Driver Manager   <<<
# ------ Gabriel Bellome ------
# ------     12.2023     ------
#
# v1.0
#
# Toda acción relacionada a la conexión son el sistema AFIP Web

# IMPORTACIONES ----------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

import time


# CLASES -----------------------------------------------------------------


class webDriverClass:
    def iniciarConexion(self):
        """ 
            Creo una instancia de Google Chrome con los {options} declarados.
        """
        driver = webdriver.Chrome(
            service=Service(),
            options=self.setearChromeOptions(True)
        )

        self.setDriver(driver=driver)

    def setearChromeOptions(self, visible):
        """
            Seteo los parametros del {webdriver.Chrome}. En caso de visible = True, se mostrará la instancia generada.
        """

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])

        if visible:
            chrome_options.add_argument("--start-maximized")
        else:
            chrome_options.add_argument("--headless=new")

        return chrome_options

    def setDriver(self, driver) -> None:
        self.driver = driver

    def terminarConexion(self):
        return self.driver.close()

    def navegarPagina(self, url):
        self.driver.get(url)

    def esperarElemento(self, metodoBusqueda, claveBusqueda, tiempoEspera=10):
        return WebDriverWait(self.driver, tiempoEspera).until(
            EC.presence_of_element_located(
                (metodoBusqueda, claveBusqueda)
            )
        )

    def esperarElementoClickeable(self, metodoBusqueda, claveBusqueda, tiempoEspera=10):
        return WebDriverWait(self.driver, tiempoEspera).until(
            EC.element_to_be_clickable(
                (metodoBusqueda, claveBusqueda)
            )
        )

    def buscarElemento(self, metodoBusqueda, claveBusqueda):
        self.esperarElemento(metodoBusqueda, claveBusqueda)
        return self.driver.find_element(metodoBusqueda, claveBusqueda)

    def buscarElementos(self, metodoBusqueda, claveBusqueda):
        return self.driver.find_elements(metodoBusqueda, claveBusqueda)

    def setearAtributo(self, metodoBusqueda, claveBusqueda, nombreAtributo, valorAtributo):
        self.driver.execute_script(
            'arguments[0].setAttribute(arguments[1], arguments[2])',
            self.buscarElemento(metodoBusqueda, claveBusqueda),
            nombreAtributo,
            valorAtributo
        )

    def setearValorElemento(self, metodoBusqueda, claveBusqueda, valorAtributo, tiempoEspera=0):
        self.buscarElemento(
            metodoBusqueda, claveBusqueda
        ).send_keys(valorAtributo)
        time.sleep(tiempoEspera)

    def obtenerAtributo(self, metodoBusqueda, claveBusqueda, valorAtributo):
        return self.driver.execute_script(
            'arguments[0].getAttribute(arguments[1])',
            self.buscarElemento(metodoBusqueda, claveBusqueda),
            valorAtributo
        )

    def obtenerTexto(self, metodoBusqueda, claveBusqueda):
        return self.driver.execute_script(
            'arguments[0].innerText',
            self.buscarElemento(metodoBusqueda, claveBusqueda)
        )

    def obtenerDriver(self):
        return self.driver

    def clickElemento(self, metodoBusqueda, claveBusqueda):
        self.driver.execute_script(
            'arguments[0].click()',
            self.buscarElemento(metodoBusqueda, claveBusqueda)
        )

    def cambiarVentana(self, indexVentana):
        if type(indexVentana) == int:
            self.driver.switch_to.window(
                self.driver.window_handles[indexVentana]
            )

        if type(indexVentana) == str:
            self.driver.switch_to.window(indexVentana)
