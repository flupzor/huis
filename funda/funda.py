import requests


class FundaWoning:
    def __init__(self, result_obj):
        self.result_obj = result_obj

    def __getattr__(self, key):
        return self.result_obj[key]


class Funda:
    """
    API Wrapper for the following Funda API

    http://content.funda.nl/opdrachten/cmd-amsterdam/maart-2017
    """

    api_url = 'http://partnerapi.funda.nl/feeds/Aanbod.svc/json'
    list_url = '{api_url}/{api_key}/?type={type}&zo={query}&page={page}&pagesize=25'
    detail_url = '{api_url}/detail/{api_key}/koop/{guid}'

    def __init__(self, api_key, type=None, query=None, existing_objects=None):
        self.type = type or 'koop'
        self.query = query or ''
        self.api_key = api_key
        self.objects = self.get_list()

        # Retrieve existing objects, which aren't listed as well.
        existing_objects = existing_objects or []
        ids = [obj['Id'] for obj in self.objects]
        self.unlisted_objs = [obj for obj in existing_objects if obj['Id'] not in ids]
        self.objects += self.unlisted_objs

    def get_list_url(self, page=1):
        return self.list_url.format(
            api_url=self.api_url, api_key=self.api_key, page=page,
            type=self.type, query=self.query)

    def get_detail_url(self, guid):
        return self.detail_url.format(api_url=self.api_url, api_key=self.api_key, guid=guid)

    def get_page(self, page=1):
        response = requests.get(self.get_list_url(page=page))
        return response.json()

    def get_list(self):
        initial_page = self.get_page()
        new_list = list(initial_page['Objects'])
        for page in range(initial_page['Paging']['HuidigePagina'], initial_page['Paging']['AantalPaginas'] + 1):
            page = self.get_page(page=page)
            new_list += page['Objects']

        return new_list

    def get_detail(self, guid):
        response = requests.get(self.get_detail_url(guid))
        return response.json()

    def __iter__(self):
        for obj in self.objects:
            detail_obj = self.get_detail(obj['Id'])
            new_obj = {}
            new_obj.update(detail_obj)
            new_obj.update(obj)
            yield FundaWoning(new_obj)


if __name__ == '__main__':
    api_key = '271175433a7c4fe2a45750d385dd9bfd'

    def interesting(obj):
        return not obj.IsVerkocht

    funda = Funda(api_key=api_key, query='/hilversum/2000000+/')
    for obj in funda:
        keys = ['Id', 'AantalKamers', 'Adres', 'Koopprijs', 'MakelaarNaam', 'Oppervlakte', 'Perceeloppervlakte', 'Postcode',
        'URL', 'VerkoopStatus', 'WoonOppervlakteTot', 'Woonoppervlakte', 'Woonplaats',]

        if interesting(obj):
            print(', '.join(['{}: {}'.format(key, getattr(obj, key)) for key in keys]))

