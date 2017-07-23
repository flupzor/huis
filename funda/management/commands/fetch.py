from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

import reversion

from ...models import Woning
from ...funda import Funda


class Command(BaseCommand):
    help = 'Retrieve woningen'

    def handle(self, *args, **options):
        def interesting(obj):
            return not obj.IsVerkocht

        with reversion.create_revision():
            existing_objects = [{'Id': guid} for guid in Woning.objects.values_list("guid", flat=True)]
            funda = Funda(api_key=settings.FUNDA_API_KEY, query=settings.FUNDA_QUERY,
                          existing_objects=existing_objects)
            funda_woningen = [w for w in funda if interesting(w)]
            Woning.objects.from_funda_woning(*funda_woningen)
            self.stdout.write(self.style.SUCCESS('Found {} unlisted woningen '.format(len(funda.unlisted_objs))))
            self.stdout.write(self.style.SUCCESS('Processed {} woningen '.format(len(funda_woningen))))
