from django.urls import path
from servicesEval.views import *

urlpatterns = [
    path('export_evaluation/', export_evaluation_to_excel, name='export_evaluation'),
    path('export_conseiller/', export_conseiller_to_excel, name="export_conseiller"),
    path("unique-qrcode/lacger-capital-link-form-to-unique-qrcode-evaluation.png",
         download_global_qr_code, name="global_qr_code"),
    path("global-form/", evaluation_global_view, name="global_eval_form"),
    path("unique-form/<int:pk>", evaluation_unique_view, name="unique_eval_form")
]