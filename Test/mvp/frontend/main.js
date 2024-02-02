const form = document.querySelector('form')
const mensaje = document.querySelector('#Message')

const ProbarConexion = document.querySelector('#ProbarConexion')
const BuscarCompanias = document.querySelector('#BuscarCompanias')

const Usuario = form.elements['User']
const Contrasena = form.elements['Password']
const Compania = form.elements['Company']
/* const Desde = form.elements['Desde']
const Hasta = form.elements['Hasta'] */

ProbarConexion.addEventListener('click', async (event) => {
  event.preventDefault()

  console.log('Ocupado...')

  mensaje.value += 'Iniciando conexión...' + '\n'

  mensaje.value += (await eel.Login(Usuario.value, Contrasena.value)()) + '\n'

  console.log('Libre')
})

BuscarCompanias.addEventListener('click', async (event) => {
  event.preventDefault()

  console.log('Ocupado...')

  mensaje.value += 'Buscando companias...' + '\n'

  listaCompania = await eel.SearchCia(Usuario.value, Contrasena.value)() // '[{CUIT, NOMBRE}, {CUIT, NOMBRE}, {CUIT, NOMBRE}]'

  mensaje.value += listaCompania[0]

  Compania.innerHTML = listaCompania[1].map(({ CUIT, NOMBRE }) => {
    return `<option value='${CUIT}'>${NOMBRE}</option>`
  })

  console.log('Libre')
})
