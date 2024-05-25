from django.db import models

from servicesEval.models import Profession, SecteurActivite


YES_OR_NO_CHOICES = (
    ("OUI", "Oui"),
    ("NON", "Non")
)

YES_OR_NO_OR_PT_CHOICES = (
        ('OUI', 'Oui'),
        ('PEUT-ETRE', 'Peut-être'),
        ('NON', 'Non'),
    )


class Evenements(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name_evenement = models.CharField(max_length=250, null=False, unique=True)
    edition = models.CharField(max_length=300, null=False)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    inscription_limite = models.IntegerField(default=100)
    decription = models.TextField(blank=True, null=True)
    baniere_image = models.ImageField(upload_to="evements/baniere/", null=True, blank=True)
    baniere_image_2 = models.ImageField(upload_to="evements/baniere/", null=True, blank=True)

    def __str__(self):
        return self.name_evenement

    class Meta:
        verbose_name = "Evénements"
        verbose_name_plural = "Evénements"


class Participants(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    code_insc = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=300, null=False, db_index=True)
    email = models.EmailField(db_index=True, null=False)

    RECIDENCE_CHOICES = (
        ("BRAZZAVILLE", "Brazzaville"),
        ("POINTE-NOIRE", "Pointe-Noire"),
    )

    residence = models.CharField(max_length=200, choices=RECIDENCE_CHOICES, default="BRAZZAVILLE")
    phoneNumber = models.CharField(max_length=200, db_index=True, null=False)
    proffession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    secteurActivite = models.ForeignKey(SecteurActivite, on_delete=models.CASCADE)

    PIST_CHOICES = (
        ("PROSPECTION", "Prospection"),
        ("RESEAUX-SOCIAUX", "Réseaux sociaux"),
        ("BOUCHE-A-OREILLE", "Bouche à oreille")
    )

    commment_avez_vous_entendu_parler_des_rencontres_ELLE = models.CharField(max_length=200,
                                                                             choices=PIST_CHOICES,
                                                                             default="PROSPECTION")
    connaissez_vous_archer_Capital = models.CharField(max_length=10, default="NON", choices=YES_OR_NO_CHOICES)
    recevoir_infos = models.BooleanField(default=False)
    evenement = models.ForeignKey(Evenements, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"


class CoverRecontreSondage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    libelle = models.CharField(max_length=250)

    def __str__(self):
        return self.libelle


class Avis(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    que_pensez_vous_du_concept = models.CharField(max_length=300, null=True, blank=True)
    quelles_etaient_vos_attentes = models.CharField(max_length=300, null=True, blank=True)
    vos_attentes_ont_elles_ete_comblees = models.CharField(max_length=300,
                                                           choices=YES_OR_NO_CHOICES, default="OUI")
    les_themes_abordes_ont_ils_ete_pertinents_selon_vous = models.CharField(max_length=300,
                                                                            choices=YES_OR_NO_CHOICES,
                                                                            default="OUI")
    souhaiteriez_vous_participer_a_autres_evenements_de_ce_type = models.CharField(max_length=300,
                                                                                   choices=YES_OR_NO_CHOICES,
                                                                                   default="OUI")
    sujets_que_vous_aimeriez_voir_abordes = models.TextField(null=True, blank=True)
    inviteriez_vous_une_amie_prochainement = models.CharField(max_length=300, null=True, blank=True)
    avez_vous_besoin_un_accompagnement_personalise = models.CharField(max_length=300,
                                                                      choices=YES_OR_NO_CHOICES,
                                                                      default="NON")
    evenement = models.ForeignKey(Evenements, on_delete=models.CASCADE, related_name="avis")
    participant = models.ForeignKey(Participants, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.created_at} ({self.participant.name})"

    class Meta:
        verbose_name = "Avis"
        verbose_name_plural = "Avis"





