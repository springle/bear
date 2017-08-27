from django.core.management.base import BaseCommand, CommandError
from search import utils

class Command(BaseCommand):
    help = "Scrape classes from Berkeley's API."

    def handle(self, *args, **options):
        c = utils.ClassesAPI().query()
        self.stdout.write(self.style.SUCCESS('Finished scraping classes.'))
