from django.db import models

from .managers import WoningManager

none = [
    'AantalBeschikbaar'
    'AantalKavels'
    'AantalSlaapkamers'
    'AfgekochtDatum'
    'BedrijfsruimteCombinatieObject'
    'DatumAanvaarding'
    'DatumOndertekeningAkte'
    'EersteHuurPrijs'
    'EersteHuurPrijsLang'
    'GewijzigdDatum'
    'HuurPrijs'
    'HuurPrijsLang'
    'HuurPrijsTot'
    'Huurprijs'
    'HuurprijsFormaat'
    'InUnitsVanaf'
    'IndTransactieMakelaarTonen'
    'Note'
    'ProjectNaam'
    'SavedDate'
    'StartOplevering'
    'TimeAgoText'
    'TransactieAfmeldDatum'
    'TransactieMakelaarId'
    'TransactieMakelaarNaam'
    'VeilingGeformatteerd'
]

dictionaries = [
    'DetailInfo'
    'Energielabel'
    'KenmerkenKort'
    'Prijs'
    'Project'
    'PromoLabel'
    'Veiling'
    'Video'
]

lists = [
    'BezichtingDagdelen',
    'BezichtingDagen',
    'ChildrenObjects',
    'Kenmerken',
    'MedeAanbieders',
    'Media',
    'Media-Foto',
    'OpenHuis',
    'OpenHuizen',
    'Producten',
    'Titels',
    'ZoekType',
]

class Woning(models.Model):
    url = models.CharField(max_length=255)

    # CharFields
    aangeboden_sinds = models.CharField(max_length=255)
    aangeboden_sinds_tekst = models.CharField(max_length=255)
    aanmeld_datum = models.CharField(max_length=255)
    aantal_woonlagen = models.CharField(max_length=255)
    aanvaarding = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    bijzonderheden = models.CharField(max_length=255)
    bouwjaar = models.CharField(max_length=255)
    bouwvorm = models.CharField(max_length=255)
    bron_code = models.CharField(max_length=255)
    contactpersoon_email = models.CharField(max_length=255)
    contactpersoon_telefoon = models.CharField(max_length=255)
    cv = models.CharField(max_length=255)
    eerste_koop_prijs_lang = models.CharField(max_length=255)
    eigendoms_situatie = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    foto_large = models.CharField(max_length=255)
    foto_largest = models.CharField(max_length=255)
    foto_medium = models.CharField(max_length=255)
    foto_secure = models.CharField(max_length=255)
    gelegen_op = models.CharField(max_length=255)
    group_by_object_type = models.CharField(max_length=255)
    hoofd_foto = models.CharField(max_length=255)
    hoofd_foto_secure = models.CharField(max_length=255)
    guid = models.CharField(max_length=255)
    internal_id = models.CharField(max_length=255)
    isolatie = models.CharField(max_length=255)
    koop_prijs_lang = models.CharField(max_length=255)
    koopprijs_formaat = models.CharField(max_length=255)
    ligging = models.CharField(max_length=255)
    makelaar = models.CharField(max_length=255)
    makelaar_naam = models.CharField(max_length=255)
    makelaar_telefoon = models.CharField(max_length=255)
    mobile_u_r_l = models.CharField(max_length=255)
    object_type = models.CharField(max_length=255)
    object_type_met_voorvoegsel = models.CharField(max_length=255)
    permanente_bewoning = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    prijs_geformatteerd = models.CharField(max_length=255)
    prijs_geformatteerd_html = models.CharField(max_length=255)
    prijs_geformatteerd_text_huur = models.CharField(max_length=255)
    prijs_geformatteerd_text_koop = models.CharField(max_length=255)
    publicatie_datum = models.CharField(max_length=255)
    schuur_berging = models.CharField(max_length=255)
    schuur_berging_voorzieningen = models.CharField(max_length=255)
    scrambled_id = models.CharField(max_length=255)
    short_u_r_l = models.CharField(max_length=255)
    soort_aanbod = models.CharField(max_length=255)
    soort_garage = models.CharField(max_length=255)
    soort_parkeergelegenheid = models.CharField(max_length=255)
    soort_woning = models.CharField(max_length=255)
    u_r_l = models.CharField(max_length=255)
    verkoop_status = models.CharField(max_length=255)
    verwarming = models.CharField(max_length=255)
    volledige_omschrijving = models.CharField(max_length=255)
    voorzieningen = models.CharField(max_length=255)
    warm_water = models.CharField(max_length=255)
    woonplaats = models.CharField(max_length=255)
    balkon_dakterras = models.CharField(max_length=255)
    deeplink = models.CharField(max_length=255)
    garage = models.CharField(max_length=255)
    garage_isolatie = models.CharField(max_length=255)
    garage_voorzieningen = models.CharField(max_length=255)
    hoofd_tuin_type = models.CharField(max_length=255)
    kenmerken_titel = models.CharField(max_length=255)
    schuur_berging_isolatie = models.CharField(max_length=255)
    soort_dak = models.CharField(max_length=255)
    tuin = models.CharField(max_length=255)
    tuin_ligging = models.CharField(max_length=255)

    # IntegerFields
    aantal_badkamers = models.IntegerField(null=True, blank=True)
    aantal_kamers = models.IntegerField(null=True, blank=True)
    global_id = models.IntegerField(null=True, blank=True)
    type_project = models.IntegerField(null=True, blank=True)
    soort_aanbod = models.IntegerField(null=True, blank=True)
    soort_plaatsing = models.IntegerField(null=True, blank=True)
    makelaar_id = models.IntegerField(null=True, blank=True)

    # Decimal fields
    afstand = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bijdrage_v_v_e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    eerste_koop_prijs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    erfpacht_bedrag = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    inhoud = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    koop_prijs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    koopprijs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    koopprijs_tot = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    oppervlakte = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    publicatie_status = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    service_kosten = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    woon_oppervlakte = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    woon_oppervlakte_tot = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    woonoppervlakte = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    perceeloppervlakte = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    perceel_oppervlakte = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    WGS84_X = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    WGS84_Y = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)

    # Booleans
    heeft360_graden_foto = models.BooleanField(default=False)
    heeft_brochure = models.BooleanField(default=False)
    heeft_openhuizen_topper = models.BooleanField(default=False)
    heeft_overbruggingsgrarantie = models.BooleanField(default=False)
    heeft_plattegrond = models.BooleanField(default=False)
    heeft_tophuis = models.BooleanField(default=False)
    heeft_veiling = models.BooleanField(default=False)
    heeft_video = models.BooleanField(default=False)
    ind_basis_plaatsing = models.BooleanField(default=False)
    ind_fotos = models.BooleanField(default=False)
    ind_ipix = models.BooleanField(default=False)
    ind_openhuizen_topper = models.BooleanField(default=False)
    ind_p_d_f = models.BooleanField(default=False)
    ind_plattegrond = models.BooleanField(default=False)
    ind_project_object_type = models.BooleanField(default=False)
    ind_top = models.BooleanField(default=False)
    ind_veiling_product = models.BooleanField(default=False)
    ind_video = models.BooleanField(default=False)
    is_ingetrokken = models.BooleanField(default=False)
    is_searchable = models.BooleanField(default=False)
    is_verhuurd = models.BooleanField(default=False)
    is_verkocht = models.BooleanField(default=False)
    is_verkocht_of_verhuurd = models.BooleanField(default=False)
    toon_bezichtiging_maken = models.BooleanField(default=False)
    toon_brochure_aanvraag = models.BooleanField(default=False)
    toon_makelaar_woningaanbod = models.BooleanField(default=False)
    toon_reageren = models.BooleanField(default=False)

    objects = WoningManager()
