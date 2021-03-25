import csv
import datetime
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.db.models import Q

from lesson_8.models import GameModel, GamerLibraryModel, GamerModel


def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                pass
    return HttpResponse("Done!")


class FilterView(ListView):
    template_name = 'gamemodel_list.html'

    # query with filter
    # queryset = GameModel.objects.filter(name__contains="Hitman")
    # queryset = GameModel.objects.filter(name__exact="Hitman (2016)")
    # queryset = GameModel.objects.filter(name__in=["Hitman (2016)", "Tetris"])
    # queryset = GameModel.objects.filter(na_sales__gte=11.27)
    # queryset = GameModel.objects.filter(name__endswith="ga")
    # queryset = GameModel.objects.filter(name__regex=r'^(An?|The) +')

    # queryset = GameModel.objects.filter(
    #     Q(name__startswith='A') & Q(name__endswith='a') & Q(name__contains="ma")
    # )

    # queryset = GameModel.objects.filter(Q(name__endswith='a'),
    #                                     name__startswith='A')

    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="Ab") | Q(name__startswith="Ad") | Q(name__startswith="Mat")
    # )

    queryset = GameModel.objects.filter(
        ~Q(name__startswith="Ab") | ~Q(name__startswith="Ad") | ~Q(name__startswith="Mat")
    )


def relation_filter_view(request):
    data = GamerLibraryModel.objects.filter(gamer__email__contains='a')
    print(data[0].gamer.email)
    # return HttpResponse(data)
    return HttpResponse(data.order_by())


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman")


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman").order_by('year')


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").union(
        GameModel.objects.filter(name="Tetris")
    )


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").values("name", "platform", "year")

    def get(self, request, *args, **kwargs):
        print(GameModel.objects.filter(name="Hitman (2016)").values("name", "platform", "year"))
        print(list(GameModel.objects.all().values_list("name", "year")))

        return super().get(request, *args, **kwargs)


def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='day')
    print(data)
    return HttpResponse(data)


def get_view(request):
    data = GameModel.objects.get(pk=27)
    print(data)
    return HttpResponse(data)


def create_view(request):
    # 1st method
    # myself = GamerModel()
    # myself.email = "admin@admin.com"
    # myself.nickname = "SomeRandomNicknameSave"
    # myself.save()

    # 2nd method
    # myself = GamerModel(email="admin@admin.com",
    #                     nickname="SomeRandomNicknameSave")
    # myself.save()

    # 3rd method
    # myself = GamerModel(**{"email": "admin@admin.com",
    #                        "nickname": "SomeRandomNicknameSave"})
    # myself.save()

    # 4th method
    # myself = GamerModel.objects.create(**{"email": "admin@admin.com",
    #                        "nickname": "SomeRandomNicknameSave"})

    # 5th method
    # myself = GamerModel.objects.create(email="admin@admin.com",
    #                                    nickname="SomeRandomNicknameSave")

    # 6th method. bulk the fastest method
    # myself = GamerModel.objects.bulk_create([
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameCreate1"
    #     ),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameCreate2"
    #     ),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameCreate3"
    #     ),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameCreate4"
    #     ),
    # ])

    # 7st method
    # my_library = GamerLibraryModel(gamer=GamerModel.objects.get(pk=1), size=10)
    # my_library.save()
    # my_library.game.set([GameModel.objects.get(pk=1),
    #                      GameModel.objects.get(pk=2)])

    # 8th method
    # my_library = GamerLibraryModel.objects.create(gamer=GamerModel.objects.get(pk=1),size=10)
    # my_library.game.set([GameModel.objects.get(pk=1), GameModel.objects.get(pk=2)])

    # 9th method
    # my_library = GamerLibraryModel.objects.bulk_create(
    #     [GamerLibraryModel(gamer=GamerModel.objects.get(pk=1),
    #                        size=10),
    #      GamerLibraryModel(gamer=GamerModel.objects.get(pk=1),
    #                        size=10)
    #      ])

    # add My friend
    # my_friend = GamerModel.objects.get(pk=1)
    # my_friend.nickname = "MyFriend"
    # my_friend.save()


    my_friend = GamerModel.objects.filter(pk=1)
    my_friend.update(nickname="MySecondNickname")

    return HttpResponse(my_friend)
