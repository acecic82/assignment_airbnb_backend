from django.contrib import admin


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Filter by Elon Musk!"

    parameter_name = "Elon Musk"

    def lookups(self, request, model_admin):
        return [
            ("Elon Musk", "Elon Musk"),
        ]

    def queryset(self, request, tweets):
        # self.value는 결국 Lookups 의 tuple의 앞에 인자를 가져옴
        word = self.value()
        print(word)
        if word == None:
            return tweets.all()
        return tweets.filter(payload__contains=word)
