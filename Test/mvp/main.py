import eel
from backend.PlataformaWebAFIP import PlataformaWebAFIP
from backend.MOA_Reingenieria import MOA_Reingenieria

eel.init('Test/mvp/frontend')


@eel.expose
def Login(usuario, clave) -> str:
    return str(PlataformaWebAFIP().LoginAFIP(usuario=usuario, clave=clave))


@eel.expose
def SearchCia(usuario, clave):
    res = MOA_Reingenieria().ListadoCompania(
        usuario=usuario, clave=clave)
    return [str(res), res.obtenerListadoCompania()]


eel.start('index.html')
