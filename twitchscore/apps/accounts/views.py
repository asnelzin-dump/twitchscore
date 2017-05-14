from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as login_user

from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView


# def anonymous_only(view_func):
#     actual_decorator = user_passes_test(
#         lambda u: not u.is_authenticated(),
#         redirect_url=lambda u: u.get_redirect_url_if_logged(),
#
#     )


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    @method_decorator(csrf_protect)
    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login_user(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.REQUEST.get('next', '')
        if not url or not is_safe_url(url=url, host=self.request.get_host()):
            url = '/'
        return url

login = LoginView.as_view()