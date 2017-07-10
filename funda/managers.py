from django.db import models

string_mapping = [
    ('aangeboden_sinds', 'AangebodenSinds'),
    ('aangeboden_sinds_tekst', 'AangebodenSindsTekst'),
    ('aanmeld_datum', 'AanmeldDatum'),
    ('aantal_woonlagen', 'AantalWoonlagen'),
    ('aanvaarding', 'Aanvaarding'),
    ('adres', 'Adres'),
    ('bijzonderheden', 'Bijzonderheden'),
    ('bouwjaar', 'Bouwjaar'),
    ('bouwvorm', 'Bouwvorm'),
    ('bron_code', 'BronCode'),
    ('contactpersoon_email', 'ContactpersoonEmail'),
    ('contactpersoon_telefoon', 'ContactpersoonTelefoon'),
    ('cv', 'Cv'),
    ('eerste_koop_prijs_lang', 'EersteKoopPrijsLang'),
    ('eigendoms_situatie', 'EigendomsSituatie'),
    ('foto', 'Foto'),
    ('foto_large', 'FotoLarge'),
    ('foto_largest', 'FotoLargest'),
    ('foto_medium', 'FotoMedium'),
    ('foto_secure', 'FotoSecure'),
    ('gelegen_op', 'GelegenOp'),
    ('group_by_object_type', 'GroupByObjectType'),
    ('hoofd_foto', 'HoofdFoto'),
    ('hoofd_foto_secure', 'HoofdFotoSecure'),
    ('guid', 'Id'),
    ('internal_id', 'InternalId'),
    ('isolatie', 'Isolatie'),
    ('koop_prijs_lang', 'KoopPrijsLang'),
    ('koopprijs_formaat', 'KoopprijsFormaat'),
    ('ligging', 'Ligging'),
    ('makelaar', 'Makelaar'),
    ('makelaar_naam', 'MakelaarNaam'),
    ('makelaar_telefoon', 'MakelaarTelefoon'),
    ('mobile_u_r_l', 'MobileURL'),
    ('object_type', 'ObjectType'),
    ('object_type_met_voorvoegsel', 'ObjectTypeMetVoorvoegsel'),
    ('permanente_bewoning', 'PermanenteBewoning'),
    ('plaats', 'Plaats'),
    ('postcode', 'Postcode'),
    ('prijs_geformatteerd', 'PrijsGeformatteerd'),
    ('prijs_geformatteerd_html', 'PrijsGeformatteerdHtml'),
    ('prijs_geformatteerd_text_huur', 'PrijsGeformatteerdTextHuur'),
    ('prijs_geformatteerd_text_koop', 'PrijsGeformatteerdTextKoop'),
    ('publicatie_datum', 'PublicatieDatum'),
    ('schuur_berging', 'SchuurBerging'),
    ('schuur_berging_voorzieningen', 'SchuurBergingVoorzieningen'),
    ('scrambled_id', 'ScrambledId'),
    ('short_u_r_l', 'ShortURL'),
    ('soort_aanbod', 'Soort-aanbod'),
    ('soort_garage', 'SoortGarage'),
    ('soort_parkeergelegenheid', 'SoortParkeergelegenheid'),
    ('soort_woning', 'SoortWoning'),
    ('u_r_l', 'URL'),
    ('verkoop_status', 'VerkoopStatus'),
    ('verwarming', 'Verwarming'),
    ('volledige_omschrijving', 'VolledigeOmschrijving'),
    ('voorzieningen', 'Voorzieningen'),
    ('warm_water', 'WarmWater'),
    ('woonplaats', 'Woonplaats'),
    ('balkon_dakterras', 'BalkonDakterras'),
    ('deeplink', 'Deeplink'),
    ('garage', 'Garage'),
    ('garage_isolatie', 'GarageIsolatie'),
    ('garage_voorzieningen', 'GarageVoorzieningen'),
    ('hoofd_tuin_type', 'HoofdTuinType'),
    ('kenmerken_titel', 'KenmerkenTitel'),
    ('schuur_berging_isolatie', 'SchuurBergingIsolatie'),
    ('soort_dak', 'SoortDak'),
    ('tuin', 'Tuin'),
    ('tuin_ligging', 'TuinLigging'),
]

int_mapping = [
    ('aantal_badkamers', 'AantalBadkamers'),
    ('aantal_kamers', 'AantalKamers'),
    ('global_id', 'GlobalId'),
    ('type_project', 'TypeProject'),
    ('soort_aanbod', 'SoortAanbod'),
    ('soort_plaatsing', 'SoortPlaatsing'),
    ('makelaar_id', 'MakelaarId'),
]

boolean_mapping = [
    ('heeft360_graden_foto', 'Heeft360GradenFoto'),
    ('heeft_brochure', 'HeeftBrochure'),
    ('heeft_openhuizen_topper', 'HeeftOpenhuizenTopper'),
    ('heeft_overbruggingsgrarantie', 'HeeftOverbruggingsgrarantie'),
    ('heeft_plattegrond', 'HeeftPlattegrond'),
    ('heeft_tophuis', 'HeeftTophuis'),
    ('heeft_veiling', 'HeeftVeiling'),
    ('heeft_video', 'HeeftVideo'),
    ('ind_basis_plaatsing', 'IndBasisPlaatsing'),
    ('ind_fotos', 'IndFotos'),
    ('ind_ipix', 'IndIpix'),
    ('ind_openhuizen_topper', 'IndOpenhuizenTopper'),
    ('ind_p_d_f', 'IndPDF'),
    ('ind_plattegrond', 'IndPlattegrond'),
    ('ind_project_object_type', 'IndProjectObjectType'),
    ('ind_top', 'IndTop'),
    ('ind_veiling_product', 'IndVeilingProduct'),
    ('ind_video', 'IndVideo'),
    ('is_ingetrokken', 'IsIngetrokken'),
    ('is_searchable', 'IsSearchable'),
    ('is_verhuurd', 'IsVerhuurd'),
    ('is_verkocht', 'IsVerkocht'),
    ('is_verkocht_of_verhuurd', 'IsVerkochtOfVerhuurd'),
    ('toon_bezichtiging_maken', 'ToonBezichtigingMaken'),
    ('toon_brochure_aanvraag', 'ToonBrochureAanvraag'),
    ('toon_makelaar_woningaanbod', 'ToonMakelaarWoningaanbod'),
    ('toon_reageren', 'ToonReageren'),
]

decimal_mapping = [
    ('WGS84_X', 'WGS84_X'),
    ('WGS84_Y', 'WGS84_Y'),
    ('afstand', 'Afstand'),
    ('bijdrage_v_v_e', 'BijdrageVVE'),
    ('eerste_koop_prijs', 'EersteKoopPrijs'),
    ('erfpacht_bedrag', 'ErfpachtBedrag'),
    ('inhoud', 'Inhoud'),
    ('koop_prijs', 'KoopPrijs'),
    ('koopprijs', 'Koopprijs'),
    ('koopprijs_tot', 'KoopprijsTot'),
    ('oppervlakte', 'Oppervlakte'),
    ('publicatie_status', 'PublicatieStatus'),
    ('service_kosten', 'ServiceKosten'),
    ('woon_oppervlakte', 'WoonOppervlakte'),
    ('woon_oppervlakte_tot', 'WoonOppervlakteTot'),
    ('woonoppervlakte', 'Woonoppervlakte'),
    ('perceeloppervlakte', 'Perceeloppervlakte'),
    ('perceel_oppervlakte', 'PerceelOppervlakte'),
]

class WoningManager(models.Manager):
    def from_funda_woning(self, *funda_woning_list):
        for funda_woning in funda_woning_list:
            woning, created = self.get_or_create(url=funda_woning.URL)
            for django_field_name, funda_field_name in string_mapping:
                setattr(woning, django_field_name, getattr(funda_woning, funda_field_name) or '')
            for django_field_name, funda_field_name in int_mapping:
                value = getattr(funda_woning, funda_field_name)
                assert type(value) is int or value is None, 'Expected an integer for {}. Value: {} ({})'.format(
                    funda_field_name, value, type(value)
                )
                if value:
                    setattr(woning, django_field_name, value)
            for django_field_name, funda_field_name in boolean_mapping:
                value = getattr(funda_woning, funda_field_name)
                assert type(value) is bool or value is None, 'Expected an boolean for {}. Value: {} ({})'.format(
                    funda_field_name, value, type(value)
                )
                if value:
                    setattr(woning, django_field_name, value)
            for django_field_name, funda_field_name in decimal_mapping :
                value = getattr(funda_woning, funda_field_name)
                assert type(value) in [int, float] or value is None, 'Expected an int or float for {}. Value: {} ({})'.format(
                    funda_field_name, value, type(value)
                )
                if value:
                    setattr(woning, django_field_name, value)
            woning.save()
