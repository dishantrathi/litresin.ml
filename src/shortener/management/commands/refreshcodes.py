from django.core.management.base import BaseCommand, CommandError

from shortener.models import LitresinURL


class Command(BaseCommand):
    help = 'Refrehes all LitresinURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return LitresinURL.objects.refresh_shortcodes(items=options['items'])