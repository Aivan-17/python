from routeros_api import RouterOsApiPool, login

# Configura los detalles de tu conexión
router_ip = '192.168.88.1'  # Dirección IP de tu router MikroTik
router_username = 'admin'  # Nombre de usuario para iniciar sesión
router_password = 'contraseña'  # Contraseña para iniciar sesión

# Crea una conexión con el router
with RouterOsApiPool(
    host=router_ip,
    username=router_username,
    password=router_password,
    port=8728,  # Puerto por defecto de la API de MikroTik
    plaintext_login=True,  # Usa True si deseas iniciar sesión sin SSL
) as api:

    # Crea un cliente API
    client = api.get_api()

    # Realiza algunas operaciones básicas
    # Por ejemplo, obtén la lista de interfaces
    interfaces = client.get_resource('/interface').get()

    # Imprime la información de las interfaces
    for interface in interfaces:
        print(f"Nombre: {interface['name']}, Tipo: {interface['type']}")

    # Puedes agregar más operaciones aquí, como configurar o verificar configuraciones
    # ...

