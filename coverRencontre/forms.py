from django import forms
from django.forms import TextInput, Select, Textarea

from coverRencontre.models import Participants, Avis, YES_OR_NO_CHOICES, Evenements, YES_OR_NO_OR_PT_CHOICES
from servicesEval.models import Profession, SecteurActivite


class ParticipantsForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Votre nom et prénom'
    }))

    email = forms.EmailField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Votre email'
    }))

    phoneNumber = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Votre Téléphone'
    }))

    residence = forms.ChoiceField(choices=Participants.RECIDENCE_CHOICES, widget=Select(attrs={
        'class': 'form-control',
    }))

    proffession = forms.ModelChoiceField(queryset=Profession.objects, widget=Select(attrs={
        'class': 'form-control',
        'placeholder': 'Votre profession'
    }))

    secteurActivite = forms.ModelChoiceField(queryset=SecteurActivite.objects, widget=Select(attrs={
        'class': 'form-control',
        'placeholder': "Votre secteur d'activité"
    }))

    commment_avez_vous_entendu_parler_des_rencontres_ELLE = forms.ChoiceField(choices=Participants.PIST_CHOICES,
                                                                              widget=Select(
                                                                                  attrs={'class': 'form-control',
                                                                                         }))

    connaissez_vous_archer_Capital = forms.ChoiceField(choices=YES_OR_NO_CHOICES,
                                                       required=True,
                                                       widget=forms.RadioSelect(attrs={'class': 'form-control-inline'}),
                                                       )

    recevoir_infos = forms.BooleanField(required=False,
                                        widget=forms.CheckboxInput(attrs={'class': 'form-control-inline',
                                                                          'style': 'width: 18px; height: 18px;'}))

    code_insc = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Code Iscription'}))
    evenement = forms.ModelChoiceField(queryset=Evenements.objects,
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Participants
        fields = "__all__"


class AvisForm(forms.ModelForm):
    code_id = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "2-DG6EG-203"
    }))

    que_pensez_vous_du_concept = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'style': 'height: 130px;'
    }), required=False, empty_value=True)

    quelles_etaient_vos_attentes = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'style': 'height: 130px;'
    }), required=False, empty_value=True)

    vos_attentes_ont_elles_ete_comblees = forms.ChoiceField(choices=YES_OR_NO_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    les_themes_abordes_ont_ils_ete_pertinents_selon_vous = forms.ChoiceField(choices=YES_OR_NO_CHOICES,
                                                                             widget=forms.Select(attrs={
                                                                                 'class': 'form-control',
                                                                             }))

    souhaiteriez_vous_participer_a_autres_evenements_de_ce_type = forms.ChoiceField(
        choices=YES_OR_NO_CHOICES, widget=forms.Select(attrs={
            'class': 'form-control',
        }))

    quels_sont_les_sujets_que_vous_aimeriez_voir_abordes_lors_des_prochaines_rencontres = forms.CharField(
        widget=Textarea(attrs={
            'class': 'form-control', 'style': 'height: 130px;'
        }), required=False, empty_value=True)

    inviteriez_vous_une_amie_prochainement = forms.ChoiceField(choices=YES_OR_NO_OR_PT_CHOICES,
                                                               widget=Select(attrs={
                                                                   'class': 'form-control'}))

    avez_vous_besoin_un_accompagnement_personalise = forms.ChoiceField(choices=YES_OR_NO_CHOICES, widget=Select(attrs={
        'class': 'form-control'}))

    participant = forms.ModelChoiceField(required=False, queryset=Participants.objects,
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    evenement = forms.ModelChoiceField(required=False, queryset=Evenements.objects,
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Avis
        fields = "__all__"
