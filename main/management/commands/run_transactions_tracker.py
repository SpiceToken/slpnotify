from django.core.management.base import BaseCommand

from main.bchd.transactions_tracker import TransactionsTracker


class Command(BaseCommand):
    help = "Tracks transactions using BCHD GRPC"

    def handle(self, *args, **options):
        txn_tracker = TransactionsTracker()
        txn_tracker.run()
