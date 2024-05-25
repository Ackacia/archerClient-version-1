import qrcode
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse, path
from django.utils.html import format_html

from PIL import Image, ImageDraw
from io import BytesIO

from django.contrib.auth.models import Group

from coverRencontre.models import *


admin.site.unregister(Group)


@admin.register(Evenements)
class EvenementsAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name_evenement', "date_debut", "date_fin", "inscription_limite", "action")

    search_fields = ['name_evenement']
    list_filter = ["date_debut", "date_fin"]

    def run_insc_download(self, request, account_id):
        qr_image = qrcode.make(request.build_absolute_uri(f'/cover-rencontre-elle/inscription/{account_id}'))
        canvas = Image.new("RGB", (qr_image.pixel_size, qr_image.pixel_size), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        canvas.close()
        return HttpResponse(buffer.getvalue(),
                            content_type="test/png")

    def download_insc_qr_code(self, request, account_id, *args, **kwargs):
        return self.run_insc_download(request=request, account_id=account_id)

    def run_not_download(self, request, account_id):
        qr_image = qrcode.make(request.build_absolute_uri(f'/cover-rencontre-elle/avis/{account_id}'))
        canvas = Image.new("RGB", (qr_image.pixel_size, qr_image.pixel_size), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        canvas.close()
        return HttpResponse(buffer.getvalue(),
                            content_type="test/png")

    def download_not_qr_code(self, request, account_id, *args, **kwargs):
        return self.run_not_download(request=request, account_id=account_id)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:account_id>/download/Inscription-Link-QR-Code.png',
                 self.admin_site.admin_view(self.download_insc_qr_code),
                 name="inscription-code"),

            path('<int:account_id>/download/Avis-Link-QR-Code.png',
                 self.admin_site.admin_view(self.download_not_qr_code),
                 name="avis-code"
                 )
        ]

        return custom_urls + urls

    def action(self, obj):
        return format_html(
            '<a class="button" href="{}">Inscripion QR Code</a>&nbsp;'
            '<a class="button" href="{}">Avis QR Code</a>',
            reverse('admin:inscription-code', args=[obj.pk]),
            reverse('admin:avis-code', args=[obj.pk]),
        )

    action.short_description = 'Action'
    action.allow_tags = True


@admin.register(Participants)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phoneNumber", "evenement", "code_insc", "created_at")

    search_fields = ['name', 'email']
    list_filter = ["evenement", "created_at", "secteurActivite", "proffession"]

    change_list_template = 'admin/coverRencontre/Participants/change_list.html'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_edit_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(CoverRecontreSondage)
class CoverRecontreSondageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "libelle")


@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('participant',
                    'que_pensez_vous_du_concept',
                    'quelles_etaient_vos_attentes',
                    'vos_attentes_ont_elles_ete_comblees',
                    'les_themes_abordes_ont_ils_ete_pertinents_selon_vous',
                    'souhaiteriez_vous_participer_a_autres_evenements_de_ce_type',
                    'sujets_que_vous_aimeriez_voir_abordes',
                    'inviteriez_vous_une_amie_prochainement',
                    'avez_vous_besoin_un_accompagnement_personalise',
                    'created_at',
                    'evenement')

    list_filter = ['evenement', 'created_at']

    change_list_template = 'admin/coverRencontre/Avis/change_list.html'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_edit_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False