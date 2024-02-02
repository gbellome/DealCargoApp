# >>>  MOA Reingenieria  <<<
# ----  Gabriel Bellome ----
# ----      12.2023     ----
#
# v1.0
#
# Toda acción relacionada con el aplicativo MOA Reingenieria de AFIP


# IMPORTACIONES ----------------------------------------------------------
from backend.PlataformaWebAFIP import PlataformaWebAFIP

from selenium.webdriver.common.by import By

import time

# CLASES -----------------------------------------------------------------


class MOA_Reingenieria(PlataformaWebAFIP):
    def __str__(self) -> str:
        return f'Mensaje: {self.mensaje}\n TiempoInicio: {self.getTiempoInicioStr()}\n TiempoFin: {self.getTiempoFinStr()}\n TiempoTotal: {int(self.getTiempoTotal())}s'

    def setNombreCompania(self, nameCompany: str) -> None:
        """ 
            Setea el nombre de la compania a revisar.
        """

        self.compania = nameCompany

    def setTipoAgente(self, typeAgent: str) -> None:
        """ 
            Setea el tipo de agente de la compania a revisar.
        """

        self.agente = typeAgent

    def setRol(self, rol: str) -> None:
        """ 
            Setea el rol que cumple la compania a revisar.
        """

        self.rol = rol

    def setListadoCompania(self, listado: list) -> None:
        self.listadoCompania = listado

    def obtenerListadoCompania(self) -> list:
        return self.listadoCompania

    def getListCompany(self) -> None:
        """ 
            Devuelve un listado de las companias delegadas o marca con error el objeto.
        """

        # Seteo las constantes
        SELECT_CUIT_COMPANIA = 'div-empresa'
        ERROR_LISTA_COMPANIA = 'No se pudieron obtener las companias delegadas.'

        # Muestro por consola
        print(f'{self.getTiempoActualStr()}Busco las companias')

        try:
            self.esperarElemento(
                By.CLASS_NAME,
                SELECT_CUIT_COMPANIA
            )
            time.sleep(1)

            ELEM_SELECT_CUIT_COMPANIA = self.driver.find_element(
                By.CLASS_NAME,
                SELECT_CUIT_COMPANIA
            ).find_element(
                By.TAG_NAME,
                'select'
            )
            print(f'{self.getTiempoActualStr()}Desplegable encontrado')

            LISTA_OPTIONS = ELEM_SELECT_CUIT_COMPANIA.find_elements(
                By.TAG_NAME,
                'option'
            )
            print(f'{self.getTiempoActualStr()}Opciones encontradas')

            listaCUIT = []
            for compania in LISTA_OPTIONS:
                listaCUIT.append({
                    'CUIT': compania.get_attribute('value'),
                    'NOMBRE': compania.text
                })
            print(f'{self.getTiempoActualStr()}lista cargada')

            self.setListadoCompania(listaCUIT)

        except:
            self.setError(error=True)
            self.setMensaje(message=ERROR_LISTA_COMPANIA)

    def ListadoCompania(self, usuario: str, clave: str):

        self.LoginAFIP(usuario=usuario, clave=clave)
        self.OpenApplication(nombreAplicacion='MOA – Reingenieria')
        self.getListCompany()
        self.finishTimer()
        self.successProcess(message='Se recogieron todas las companias')

        return self


# FUNCIONES A EXPORTAR ---------------------------------------------------


def ConexionSIM():
    pass


""" def ListadoCompania(usuario: str, clave: str):

    print(f'[ListadoCompania] (usuario: {usuario}), clave: {clave})')

    cn = MOA_Reingenieria()
    cnn = PlataformaWebAFIP.LoginAFIP(usuario=usuario, clave=clave)
    cn.getListCompany()

    return cn """


def RelevamientoDeclaraciones():
    pass


# Listado de errores posibles
ERROR_NO_SE_ENCONTRO_BUSCADOR = "[ERROR] No se encontró el buscador de aplicativos"
ERROR_NO_SE_ABRIO_SEGUNDA_VENTANA = "[ERROR] No abrió la pestaña de MOA REINGENIERIA"
ERROR_OBTENCION_COMPANIAS = "[ERROR] No se pudieron obtener la lista de las companias"
ERROR_CARGA_SELECTOR_COMPANIA = "[ERROR] No se cargó correctamente la página de selector de compania"
ERROR_NOMBRE_COMPANIA = "[ERROR] No se encontró la compania mencionada"
ERROR_TIPO_DE_AGENTE = "[ERROR] No se encontró el tipo de agente mencionado"
ERROR_ROL = "[ERROR] No se encontró el rol mencionado"

""" # No es parte del mvp
def ObtenerListaCompanias(driver: webdriver.Chrome, guardar=True):
    # Obtengo los CUIT de las companias
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dga-conexion-externo-container')))

        ELEM_SELECT_CUIT_COMPANIA = driver.find_element(
            By.CLASS_NAME, 'div-empresa').find_element(By.TAG_NAME, 'select')
        LISTA_OPTIONS = ELEM_SELECT_CUIT_COMPANIA.find_elements(
            By.TAG_NAME, 'option')

        listaCUIT = []
        for compania in LISTA_OPTIONS:
            listaCUIT.append(compania.get_attribute('innerText'))

        if guardar:
            GuardarListaCompanias(listaCUIT)
        else:
            return listaCUIT

    except:
        return ERROR_OBTENCION_COMPANIAS
 """


""" def ConexionSIM(driver: webdriver.Chrome, nombreCompania, tipoAgente, rol):
    input('Todavia no pude programar esto, hacelo manual, y pone enter')
    return driver


def RelevamientoDeclaraciones(driver: webdriver.Chrome, desde: datetime.date, hasta: datetime.date, acumulado):

    # IngresarLasFechasSeteadas(periodo)
    fechaDesde = datetime.strftime(desde, "%Y-%m-%d %H:%M:%S")
    fechaHasta = datetime.strftime(hasta, "%Y-%m-%d %H:%M:%S")
    fechaDesdeMask = datetime.strftime(desde, "%d/%m/%Y")
    fechaHastaMask = datetime.strftime(hasta, "%d/%m/%Y")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'fechaOficDesde')))

    driver.execute_script(
        f"arguments[0].value = '{fechaDesde}'",
        driver.find_element(By.NAME, 'fechaOficDesde')
    )

    driver.execute_script(
        f"arguments[0].value = '{fechaHasta}'",
        driver.find_element(By.NAME, 'fechaOficHasta')
    )

    driver.execute_script(
        f"arguments[0].value = '{fechaDesdeMask}'",
        driver.find_element(By.NAME, 'fechaOficDesdeMask')
    )

    driver.execute_script(
        f"arguments[0].value = '{fechaHastaMask}'",
        driver.find_element(By.NAME, 'fechaOficHastaMask')
    )

    # BuscarDeclaraciones
    BOTON_BUSCAR = r"/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div[6]/button[1]"
    ELEM_BOTON_BUSCAR =
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, BOTON_BUSCAR)))

    ELEM_BOTON_BUSCAR.click()

    # MostrarTodasLasDeclaracionesQueSePueda
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'DataTables_Table_0_length')))
    driver.find_element(By.ID, 'DataTables_Table_0_length').find_element(
        By.TAG_NAME, 'select').send_keys(200)

    # Obtener lista de declaraciones
    try:
        driver.find_element(By.CLASS_NAME, "dataTables_empty")
    except:
        return

    # Mostrar avance al front

    # Recorro cada declaracion
    # Obtengo datos
    # Obtengo items
    # Guardo en un dF
    # Muestro avance al front

    # Navego a pantalla de declaraciones

    pass


def ObtenerPeriodos(desde: str, hasta: str):
    arraySalida = []
    fechaIndice = datetime.strptime(desde, '%d.%m.%y')
    while (fechaIndice <= datetime.strptime(hasta, '%d.%m.%y')):
        arraySalida.append(
            {
                'desde': fechaIndice,
                'hasta': fechaIndice +
                relativedelta(months=1) + relativedelta(days=-1)
            }
        )
        fechaIndice = fechaIndice + relativedelta(months=1)

    return arraySalida
 """
