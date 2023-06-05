# tabnews-django
Olá, bem vindo ao TabNews Django, com intuíto de aprendizo, comecei esse projeto para refazer o TabNews.
Estou fazendo o curso do [Filipe Dechamps](https://filipedeschamps.com.br/)
Iniciei esse projeto no dia 04/05/2023.

> Utilizarei no projeto Django,HTMX,JQuery, TailwindCss.


## Utilização

Para iniciar a utilização do projeto você necessita criar um email SMTP , caso não tenham um, use a do google, é gratuito.

.env
```.env
SECRET_KEY=
DEBUG=True

EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_USE_SSL=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Utilizando o terminal da sua escolha.

```npm
npm install
npm run dev
```



```Bash
python -m virtualenv env
source env/Script/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Configurações

### tailwind.config.js
```JavaScript
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./**/*.html",
    "./templates/*.html",
    "./templates/**/*.html",
    "./templates/**/**/*.html",
    "**/**/*.html",
    "**/**/forms.py",
    "tabnews/static/js/custom.js"
  ],
  theme: {
    extend: {
      colors: {
          'dark': 'rgb(22, 27, 34)',
          'darkMode': '#0d1117',
          'darkButton': 'rgb(48, 54, 61)',
          'darkInput': 'rgb(1, 4, 9)',
      }
    },
  },
  plugins: [],
}
```

### settings.py

```Python
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


Primeira vez que deixo um rep com algo que fiz aberto, queria muito a ajuda de todos.
