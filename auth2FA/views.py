from django import forms
from django.forms import TextInput
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView, FormView

from .models import UserTwoFactorAuthData
from .services import user_two_factor_auth_data_create, user_two_factor_auth_data_get


class AdminSetupTwoFactorAuthView(TemplateView):
    template_name = "auth2FA/setup_2fa.html"

    def post(self, request):
        context = {}
        user = request.user

        try:
            two_factor_auth_data = user_two_factor_auth_data_create(user=user)
            otp_secret = two_factor_auth_data.otp_secret

            context["otp_secret"] = otp_secret
            context["qr_code"] = two_factor_auth_data.generate_qr_code(
                name=user.email
            )
        except ValidationError as exc:
            context["form_errors"] = exc.messages

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        try:
            two_factor_auth_data = user_two_factor_auth_data_get(user=user)
            otp_secret = two_factor_auth_data.otp_secret

            context["otp_secret"] = otp_secret
            context["qr_code"] = two_factor_auth_data.generate_qr_code(
                name=user.email
            )
        except ValidationError as exc:
            context["form_errors"] = exc.messages
        except AttributeError:
            context = {}

        return self.render_to_response(context)


class AdminConfirmTwoFactorAuthView(FormView):
    template_name = "auth2FA/confirm_2fa.html"
    success_url = reverse_lazy("admin:index")

    class Form(forms.Form):
        otp = forms.CharField(label="Entrer votre OTP", required=True, widget=TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Entrer votre OTP'}))

        def qr_code(self):
            return user_two_factor_auth_data_get(user=self.user).generate_qr_code(self.user.email)

        def get_account_email(self):
            return self.user.email

        def clean_otp(self):
            self.two_factor_auth_data = UserTwoFactorAuthData.objects.filter(
                user=self.user
            ).first()

            if self.two_factor_auth_data is None:
                raise ValidationError('2FA not set up.')

            otp = self.cleaned_data.get('otp')

            if not self.two_factor_auth_data.validate_otp(otp):
                raise ValidationError('Invalid 2FA code.')

            return otp

    def get_form_class(self):
        return self.Form

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        form.user = self.request.user

        return form

    def form_valid(self, form):
        form.two_factor_auth_data.rotate_session_identifier()

        self.request.session['2fa_token'] = str(form.two_factor_auth_data.session_identifier)

        return super().form_valid(form)
