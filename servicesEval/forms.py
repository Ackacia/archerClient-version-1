from django import forms

from servicesEval.models import *


class EvaluationGlobalForm(forms.ModelForm):
    nom_client = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={"class": "form-control",
                                                               "placeholder": "Ex: L'Archer Capital"}))
    telephone_client = forms.CharField(max_length=25,
                                       widget=forms.TextInput(attrs={"class": "form-control",
                                                                     "placeholder": "Ex: 06 000 00 00"}))
    email_client = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control",
                                                                   "placeholder": "name@larchercapital.com"}))
    profession_client = forms.ModelChoiceField(queryset=Profession.objects,
                                               widget=forms.Select(attrs={"class": "form-control"}))
    secteur_activite_client = forms.ModelChoiceField(queryset=SecteurActivite.objects,
                                                     widget=forms.Select(attrs={"class": "form-control"}))
    produit_souscrit = forms.ModelChoiceField(queryset=Produit.objects,
                                              widget=forms.Select(attrs={"class": "form-control"}))

    evaluation_sondages = forms.ModelChoiceField(queryset=Sondage.objects,
                                                 widget=forms.Select(attrs={"class": "form-control"}))
    suivez_nous_sur_les_reseaux_sociaux = forms.ChoiceField(choices=Evaluation.YES_OR_NO_CHOICE,
                                                            widget=forms.Select(attrs={"class": "form-control"}))
    comment_avez_vous_connu_lArcher_capital = forms.ChoiceField(choices=Evaluation.pist_choice,
                                                                widget=forms.Select(attrs={"class": "form-control"}))

    recommanderiez_vous_lArcher_capital = forms.ChoiceField(choices=Evaluation.YES_OR_NO_CHOICE,
                                                            widget=forms.Select(attrs={"class": "form-control"}))
    conseiller = forms.ModelChoiceField(queryset=ConseillerClient.objects,
                                        required=False,
                                        widget=forms.Select(attrs={"class": "form-control"}))
    commentaire = forms.CharField(max_length=500,
                                  required=False,
                                  widget=forms.Textarea(attrs={"class": "form-control",
                                                               "style": "width: 100%; height: 200px"}))

    class Meta:
        model = Evaluation
        fields = "__all__"


class EvaluationUniqueForm(forms.ModelForm):
    nom_client = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={"class": "form-control",
                                                               "placeholder": "Ex: L'Archer Capital"}))
    telephone_client = forms.CharField(max_length=25,
                                       widget=forms.TextInput(attrs={"class": "form-control",
                                                                     "placeholder": "Ex: 06 000 00 00"}))
    email_client = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control",
                                                                   "placeholder": "name@larchercapital.com"}))
    profession_client = forms.ModelChoiceField(queryset=Profession.objects,
                                               widget=forms.Select(attrs={"class": "form-control"}))
    secteur_activite_client = forms.ModelChoiceField(queryset=SecteurActivite.objects,
                                                     widget=forms.Select(attrs={"class": "form-control"}))
    produit_souscrit = forms.ModelChoiceField(queryset=Produit.objects,
                                              widget=forms.Select(attrs={"class": "form-control"}))

    evaluation_sondages = forms.ModelChoiceField(queryset=Sondage.objects,
                                                 widget=forms.Select(attrs={"class": "form-control"}))
    suivez_nous_sur_les_reseaux_sociaux = forms.ChoiceField(choices=Evaluation.YES_OR_NO_CHOICE,
                                                            widget=forms.Select(attrs={"class": "form-control"}))
    comment_avez_vous_connu_lArcher_capital = forms.ChoiceField(choices=Evaluation.pist_choice,
                                                                widget=forms.Select(attrs={"class": "form-control"}))

    recommanderiez_vous_lArcher_capital = forms.ChoiceField(choices=Evaluation.YES_OR_NO_CHOICE,
                                                            widget=forms.Select(attrs={"class": "form-control"}))
    conseiller = forms.ModelChoiceField(queryset=ConseillerClient.objects,
                                        required=False,
                                        widget=forms.Select(attrs={"class": "form-control"}))
    commentaire = forms.CharField(max_length=500,
                                  required=False,
                                  widget=forms.Textarea(attrs={"class": "form-control",
                                                               "style": "width: 100%; height: 200px"}))

    class Meta:
        model = Evaluation
        fields = "__all__"
