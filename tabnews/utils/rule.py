from django.http import HttpResponseRedirect

from apps.accounts.models import Account
from apps.posts.models import Post


class HTTPResponseHXRedirect(HttpResponseRedirect):
    """
    REDIRECIONAMENTO DE HTMX

    Args:
        HTTPResponseHXRedirect(redirect_to=reverse_lazy('index'))
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


def add_point(cls):
    def wrapper(request, *args, **kwargs):
        user = Account.objects.get(email=request.user.email)
        tab_coins_add_percent = round((user.tab_coins / 100) * 5, 0)
        if len(request.POST['description']) <= 100:
            return cls(request, *args, **kwargs)
        else:
            if tab_coins_add_percent < 10:
                user.tab_coins += 1
                user.save()
            elif tab_coins_add_percent >= 10 and tab_coins_add_percent < 20:
                user.tab_coins += 2
                user.save()
            elif tab_coins_add_percent >= 20 and tab_coins_add_percent < 30:
                user.tab_coins += 3
                user.save()
            elif tab_coins_add_percent >= 30 and tab_coins_add_percent < 70:
                user.tab_coins += 4
                user.save()
            elif tab_coins_add_percent >= 40 and tab_coins_add_percent < 50:
                user.tab_coins += 5
            else:
                user.tab_coins += 6
                user.save()

        return cls(request, *args, **kwargs)
    return wrapper


def give_like(cls):
    def wrapper(request, *args, **kwargs):
        user = Account.objects.get(email=request.user.email)
        user.tab_coins -= 2
        user.tab_cash += 1
        user.save()
        return cls(request, *args, **kwargs)
    return wrapper
