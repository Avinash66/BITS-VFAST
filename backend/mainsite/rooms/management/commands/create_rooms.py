from django.core.management.base import BaseCommand
from rooms.models import NormalRoom, DeluxeRoom


class Command(BaseCommand):
    help = 'This is for creating rooms'

    def add_arguments(self, parser):
        parser.add_argument('no_of_rooms', type=int)

    def handle(self, *args, **kwargs):
        no_of_rooms =20
        self.stdout.write("Rooms creation started")
        for i in range(no_of_rooms):
            i = i+1
            n = NormalRoom(room_no=i)
            n.save()
            d = DeluxeRoom(room_no=i)
            d.save()

        self.stdout.write("Rooms creation Done")

