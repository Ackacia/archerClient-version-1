from django.db import models


class Produit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nom_produit = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_produit


class Profession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    libelle = models.CharField(max_length=250, unique=True)
    autre_infos = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return self.libelle


class SecteurActivite(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    intitule = models.CharField(max_length=250, unique=True)
    autres_infos = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Secteur d'activite"
        verbose_name_plural = "Secteurs d'activites"

    def __str__(self):
        return self.intitule


class ConseillerClient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nom_conseiller = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    secteur_activite = models.ForeignKey(SecteurActivite, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'ConseillerClient'
        verbose_name_plural = 'Conseillers'

    def __str__(self):
        return f"{self.nom_conseiller}"


class Sondage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    libelle = models.CharField(max_length=250)

    def __str__(self):
        return self.libelle


class Evaluation(models.Model):
    # client infos
    nom_client = models.CharField(max_length=250)
    email_client = models.EmailField()
    telephone_client = models.CharField(max_length=25)
    profession_client = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    secteur_activite_client = models.ForeignKey(SecteurActivite, on_delete=models.SET_NULL, null=True, blank=True)

    # evaluation infos
    created_at = models.DateTimeField(auto_now_add=True)
    evaluation_sondages = models.ForeignKey(Sondage, on_delete=models.CASCADE)

    pist_choice = (
        ("Panneau Publicitaire", "Panneau Publicitaire"),
        ("Radio", "Radio"),
        ("Télévision", "Télévision"),
        ("Réseaux Sociaux", "Réseaux Sociaux"),
        ("Magazine", "Magazine"),
        ("Recommandation Tiers", "Recommandation Tiers"),
        ("Autres", "Autres"),
    )
    comment_avez_vous_connu_lArcher_capital = models.CharField(max_length=250,
                                                               null=False,
                                                               choices=pist_choice, default="Panneau Publicitaire")
    YES_OR_NO_CHOICE = (("OUI", "Oui"),
                        ("NON", "Non"),
                        )
    recommanderiez_vous_lArcher_capital = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default="OUI")
    commentaire = models.TextField()

    suivez_nous_sur_les_reseaux_sociaux = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default="OUI")
    produit_souscrit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="evaluations")
    conseiller = models.ForeignKey(ConseillerClient, on_delete=models.CASCADE, related_name="evaluations")

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'

    def __str__(self):
        return f"{self.nom_client.upper()}"
