from io import BytesIO

import qrcode
from PIL import Image, ImageDraw
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, reverse
from django.utils.html import format_html

from servicesEval.models import *
# Register your models here.


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("created_at", "libelle", "autre_infos")
    search_fields = ["libelle"]


@admin.register(Produit)
class produitAdmin(admin.ModelAdmin):
    list_display = ("created_at", "nom_produit", "description")
    search_fields = ["nom_produit"]


@admin.register(SecteurActivite)
class SecteurActiviteAdmin(admin.ModelAdmin):
    list_display = ("created_at", "intitule", "autres_infos")
    search_fields = ["intitule"]


@admin.register(Sondage)
class SondageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'libelle')


@admin.register(ConseillerClient)
class ConseillerAdmin(admin.ModelAdmin):
    list_display = ("created_at", "nom_conseiller", "email",
                    "telephone", "profession", "secteur_activite", "account_actions")
    search_fields = ["nom_conseiller"]
    list_filter = ["profession", "secteur_activite"]
    date_hierarchy = "created_at"

    def run_download(self, request, account_id):
        qr_image = qrcode.make(request.build_absolute_uri(f'/service-evaluation/unique-form/{account_id}'))
        canvas = Image.new("RGB", (qr_image.pixel_size, qr_image.pixel_size), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        canvas.close()
        return HttpResponse(buffer.getvalue(),
                            content_type="test/png")

    def download_qr_code(self, request, account_id, *args, **kwargs):
        return self.run_download(request=request, account_id=account_id)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:account_id>/download_qr_code/lacger-capital-link-form-to-conseiller-qrcode-evaluation.png',
                 self.admin_site.admin_view(self.download_qr_code),
                 name="download-conseiller-code"
                 ),
        ]

        return custom_urls + urls

    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">QR-Code</a>',
            reverse('admin:download-conseiller-code', args=[obj.pk]),
        )

    account_actions.short_description = 'Action'
    account_actions.allow_tags = True


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("created_at", "nom_client", "email_client",
                    "telephone_client", "produit_souscrit",
                    "evaluation_sondages", "conseiller")
    search_fields = ["nom_client"]
    list_filter = ["profession_client", "secteur_activite_client", "produit_souscrit"]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_edit_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False