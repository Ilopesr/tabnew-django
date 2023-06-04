# tabnew-django

Eai pessoal, apenas como aprendizado estou fazendo uma cópia do TabNews, só quem em django, espero ter a ajuda de vocês.
Utilizando Django,HTMX,JQuery e Tailwindcss eu quero recriar o tabnews enquanto vou fazer o curso.dev
Criei os milestones das etapas, a primeira está concluida, e a segunda precisa de um polimento, data 04/05/2023.

Primeiramente deve-se criar o arquivo .env, será necessário utilizar um email para as verificações de conta criada e troca de senha.
Pode utilizar o smtp gratuito do gmail, é o que eu uso.

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


```npm
npm install
npm run dev
```


open new terminal

```Bash
python -m virtualenv env
source env/Script/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Primeira vez que deixo um rep com algo que fiz aberto, queria muito a ajuda de todos.
