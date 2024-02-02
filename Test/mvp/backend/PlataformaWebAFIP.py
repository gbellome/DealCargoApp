# >>> PlataformaWebAFIP AFIP <<<
# ------ Gabriel Bellome ------
# ------     12.2023     ------
#
# v1.0
#
# Toda acción relacionada a la conexión son el sistema AFIP Web

# IMPORTACIONES ----------------------------------------------------------
from backend.WebDriver import webDriverClass

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from datetime import datetime, timedelta
import time


# CLASES -----------------------------------------------------------------
class PlataformaWebAFIP(webDriverClass):
    def __str__(self) -> str:
        return f'Mensaje: {self.mensaje}\nTiempoInicio: {self.getTiempoInicioStr()}\nTiempoFin: {self.getTiempoFinStr()}\nTiempoTotal: {int(self.getTiempoTotal())}s'

    def setTiempoInicio(self, inicio: datetime) -> None:
        self.inicio = inicio

    def setTiempoFin(self, fin: datetime) -> None:
        self.fin = fin

    def setError(self, error: bool) -> None:
        self.error = error

    def setMensaje(self, mensaje: str) -> None:
        self.mensaje = mensaje

    def setVisible(self, visible: bool) -> None:
        self.visible = visible

    def setUser(self, user: str) -> None:
        self.user = user

    def setPassword(self, password: str) -> None:
        self.password = password

    def getTiempoInicioStr(self) -> str:
        return self.inicio.strftime("%d/%m/%Y %H:%M:%S")

    def getTiempoFinStr(self) -> str:
        return self.fin.strftime("%d/%m/%Y %H:%M:%S")

    def getTiempoTotal(self) -> str:
        return (self.fin - self.inicio) / timedelta(seconds=1)

    def getTiempoActualStr(self) -> str:
        return f'({datetime.now().strftime("%d/%m/%Y %H:%M:%S")}) '

    def initConnection(self) -> any:
        """ 
            Creo una instancia de Google Chrome con los {options} declarados.
        """
        self.setError(error=False)
        print(f'{self.getTiempoActualStr()}Proceso iniciando')
        return self.iniciarConexion()

    def finishConnection(self) -> any:
        """  
            Cierro la instancia de Google Chrome.
        """
        return self.terminarConexion()

    def initTimer(self) -> None:
        """ 
            Inicio un contador de tiempo.
        """
        self.setTiempoInicio(inicio=datetime.now())

    def finishTimer(self) -> None:
        """ 
            Detengo el contador de tiempo.
        """
        self.setTiempoFin(fin=datetime.now())

    def navigateAFIP(self) -> None:
        """ 
            Navego hasta la pagina principal AFIP.
        """

        self.navegarPagina(
            f"https://auth.afip.gob.ar/contribuyente_/login.xhtml"
        )
        print(f'{self.getTiempoActualStr()}Se navego hacia la pagina de AFIP')

    def inputUser(self, user: str) -> None:
        """ 
        Ingreso el usuario recibido y apreto el boton siguiente. En caso de encontrar error, devuelvo un string.
        """

        if self.error:
            return

        # Seteo las constantes
        INPUTBOX_USUARIO = "F1:username"
        BOTON_SIGUIENTE = "F1:btnSiguiente"

        # Ingreso el usuario
        self.setUser(user=user)
        self.setearAtributo(
            By.ID,
            INPUTBOX_USUARIO,
            'value',
            self.user
        )

        # Apreto el boton de siguiente
        self.clickElemento(By.ID, BOTON_SIGUIENTE)

        # Muestro por consola
        print(f'{self.getTiempoActualStr()}Se ingreso el usuario {user}')

    def inputPassword(self, password: str) -> None:
        """ 
        Ingreso la clave recibida y apreto en boton ingresar. En caso de encontrar error, devuelvo un string.
        """

        if self.error:
            return

        # Seteo las constantes
        INPUTBOX_CLAVE = "F1:password"
        BOTON_INGRESAR = "F1:btnIngresar"

        # Ingreso la contraseña
        self.setPassword(password=password)
        self.setearAtributo(
            By.ID,
            INPUTBOX_CLAVE,
            'value',
            self.password
        )

        # Apreto el boton de ingresar
        self.clickElemento(By.ID, BOTON_INGRESAR)

        # Muestro por consola
        print(f'{self.getTiempoActualStr()}Se ingreso la clave {password}')

        # Compruebo de que no haya habido algun error
        # self.isUserWrong()
        # self.isPassWrong()
        # self.isChangePassword()

    def searchApplication(self, nameApplication: str) -> None:
        """ 
            Busco el aplicativo mencionado e ingreso.
        """

        # Seteo las constantes
        INPUTBOX_BUSCAR_APLICATIVO = 'buscadorInput'
        MENSAJE_ERROR_APLICATIVO = 'No se encontró el aplicativo.'

        # Muestro por consola
        print(f'{self.getTiempoActualStr()}Busco el aplicativo')

        # Busco el aplicativo
        try:
            self.clickElemento(
                By.ID,
                INPUTBOX_BUSCAR_APLICATIVO
            )
            self.setearValorElemento(
                By.ID,
                INPUTBOX_BUSCAR_APLICATIVO,
                nameApplication,
                2
            )
            self.setearValorElemento(
                By.ID,
                INPUTBOX_BUSCAR_APLICATIVO,
                Keys.TAB,
                2
            )
        except:
            self.setError(error=True)
            self.setMensaje(mensaje=MENSAJE_ERROR_APLICATIVO)

    def switchWindow(self) -> None:
        """ 
            Realizo el cambio de pestaña.
        """

        # Seteo las constantes
        MENSAJE_ERROR_CAMBIO_VENTANA = 'No se encontró una segunda ventana en Google Chrome.'
        # Cambio de pestaña
        try:
            self.cambiarVentana(1)
        except:
            self.setError(error=True)
            self.setMensaje(mensaje=MENSAJE_ERROR_CAMBIO_VENTANA)

    def isUserWrong(self) -> None:
        """ 
            Compruebo si el usuario es correcto.
        """

        # Seteo las constantes
        ID_MENSAJE_ERROR = "F1\\\\:msg"
        MENSAJE_ERROR_USUARIO = "Número de CUIL/CUIT incorrecto"
        ERROR_FALLO_USUARIO = "El usuario no es correcto."

        try:
            # Muestro por consola
            print(f'{self.getTiempoActualStr()}En <{ID_MENSAJE_ERROR}> dice:')
            print(self.obtenerTexto(By.ID, ID_MENSAJE_ERROR))
            # Obtener el span que diga que el usuario fallo
            if self.obtenerTexto(By.ID, ID_MENSAJE_ERROR) == MENSAJE_ERROR_USUARIO:
                self.setError(error=True)
                self.setMensaje(mensaje=ERROR_FALLO_USUARIO)

        except:
            return

    def isPassWrong(self) -> None:
        """ 
            Compruebo si la contraseña es correcta.
        """

        # Seteo las constantes
        ID_MENSAJE_ERROR = "F1\\\\:msg"
        MENSAJE_ERROR_CLAVE = "Clave o usuario incorrecto"
        ERROR_FALLO_CLAVE = "La clave no es correcta."

        try:
            # Obtener el span que diga que la clave fallo
            if self.obtenerTexto(By.ID, ID_MENSAJE_ERROR) == MENSAJE_ERROR_CLAVE:
                self.setError(error=True)
                self.setMensaje(mensaje=ERROR_FALLO_CLAVE)

        except:
            return

    def isChangePassword(self) -> None:
        """ 
            Compruebo si se solicita un cambio de contraseña.
        """

        # Seteo las constantes
        ERROR_CAMBIO_CLAVE = "Se solicita cambiar de clave. Hacelo y después volve a intentarlo."

        try:
            titulosH4 = self.buscarElementos(By.TAG_NAME, 'H4')
            for titulo in titulosH4:
                if titulo.get_attribute('innerText') == 'CAMBIAR CLAVE FISCAL':
                    self.setError(error=True)
                    self.setMensaje(mensaje=ERROR_CAMBIO_CLAVE)

        except:
            return

    def successProcess(self, message: str) -> None:
        """
            Marca como completado el proceso y muestra el mensaje.
        """
        self.setError(error=False)
        self.setMensaje(mensaje=message)

    def LoginAFIP(self, usuario: str, clave: str):
        '''
        Realiza el ingreso al sistema de AFIP a traves de Clave Fiscal.

                Parametros:
                        usuario (string): Usuario Clave Fiscal
                        clave (string): Contraseña Clave Fiscal

                Retorno:
                        resultado (obj): Objeto con información del proceso
        '''

        self.initConnection()
        self.initTimer()

        self.navigateAFIP()
        self.inputUser(user=usuario)
        self.inputPassword(password=clave)

        self.finishTimer()
        self.successProcess(message='Ingreso correcto al sistema AFIP')

        # Muestro por consola
        print(f'{self.getTiempoActualStr()}Logeo terminado')

        return self

    def OpenApplication(self, nombreAplicacion: str):
        '''
        Busca el aplicativo nombrado e ingresa al mismo.

                Parametros:
                        nombreAplicacion (string): El nombre del aplicativo¿

                Retorno:
                        resultado (obj): Objeto con información del proceso
        '''

        self.searchApplication(nameApplication=nombreAplicacion)
        self.switchWindow()
        self.successProcess(
            message=f'Ingreso correcto al aplicativo {nombreAplicacion}'
        )

        return self
