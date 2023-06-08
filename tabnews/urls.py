"""
URL configuration for tabnews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# MARKDOWN
from markdownx import urls as markdownx
# TABNEWS
from tabnews import views
# POSTS
from apps.posts.views import (NewPostView,
                              PostDetailView)
# ACCOUNTS
from apps.accounts.views import (LoginView,
                                 NewAccountView,
                                 LogoutView,
                                 new_account_active,
                                 RecoverPasswordView,
                                 NotifyEmailView,
                                 recover_password_decode,
                                 ChangePasswordView,
                                 )


# INCLUDE
urlpatterns = [

    path('perfil/', include('apps.accounts.urls')),
    path('posts/', include('apps.posts.urls')),
    path('markdownx/', include(markdownx)),

]


# ACCOUNT PATHS
urlpatterns += {
    path('login/', LoginView.as_view(), name="login"),
    path('sair/', LogoutView.as_view(), name="logout"),
    path('cadastrar/', NewAccountView.as_view(), name="signup"),
    path('cadastrar/<uidb64>/<token>/', new_account_active, name="signup_active"),
    path('cadastro/recuperar/', RecoverPasswordView.as_view(), name="recover"),
    path('cadastro/recuperar/confirmar/',
         NotifyEmailView.as_view(), name="email_notify"),
    path('cadastro/recuperar/senha/decode/<uidb64>/<token>/',
         recover_password_decode, name="recover_decode"),
    path('cadastro/recuperar/senha/validado/',
         ChangePasswordView.as_view(), name="change_password"),
}

# HOME
urlpatterns += {
    path('', views.IndexView.as_view(), name='index'),
}

# POSTS

urlpatterns += {
    path('publicar/', NewPostView.as_view(), name="new_post"),
    path('<slug:user_slug>/<slug:post_slug>/',
         PostDetailView.as_view(), name="post_detail"),
}

# ADMIN
urlpatterns += [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
