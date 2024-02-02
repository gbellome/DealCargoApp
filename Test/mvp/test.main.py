""" ESTE ARCHIVO ES PARA PROBAR LAS FUNCIONALIDADES SOLO EN EL PLANO BACKEND - PYTHON """

from backend.PlataformaWebAFIP import LoginAFIP, OpenApplication
from backend.MOA_Reingenieria import ListadoCompania
from backend.WebDriver import webDriverClass as webDriver


def Main():

    # Creo la instancia de Google Chrome
    driver = webDriver(visible=True)

    (driver, cn) = LoginAFIP(
        driver=driver,
        usuario='27389164971',
        clave='Antonella2023'
    )

    aviso(cn)

    (driver, resultado) = OpenApplication(
        driver=driver,
        nombreAplicacion='MOA – Reingenieria'
    )

    aviso(resultado)

    listado = ListadoCompania(
        driver=driver
    )

    aviso(listado)

    # resultado = DeclaracionesImportacion(resultado, ['30681781699-POLY CLIP SYSTEM S A', 'IMEX-IMEX-IMPORTADOR/EXPORT.', 'IMEX-Rol Importador Exportador'])


def aviso(res):
    if res.error:
        res.finishConnection()
        input(res.mensaje)
    else:
        print(f"mensaje: {res.mensaje}")


Main()
