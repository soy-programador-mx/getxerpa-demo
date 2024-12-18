# getxerpa

Prueba técnica

## Pasos necesarios para ejecutar proyecto

1. Clonar repositorio

```bash
git clone ssh://git@gitea/soy-programador/getxperta.git
```

2. Entrar al directorio del repositorio clonado

```bash
cd getxperta 
```

3. Correr docker compose

En caso de que el puerto ya esté usado por otro servicio, favor de modificarlo en el archivo docker-compose.yml

```bash
docker compose up -d
```

4. Ejecutar migraciones

```bash
docker compose exec drfgetexperta python manage.py migrate
```

5. Cargar data de ejemplo

* Crear usuario admin de la aplicación

```bash
docker compose exec drfgetexperta python manage.py createsuperuser
```

* Se pueden cargar los CSV de la carpeta ```sample-data``` desde la URL ```http://[server]/admin/``` (cambiar server por localhost si docker está instalado en su pc).  

* Se deben cargar en el siguiente orden:

    - Categories
    - Merchants
    - Keywords

6. La API está disponible en la URL

http://[server]:8010