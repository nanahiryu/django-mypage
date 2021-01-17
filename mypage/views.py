from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    # djangoが用意したデータを取得する関数
    def get_context_data(self):
        context = super().get_context_data()
        context["username"] = "るーろん"
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["num_services"] = 12345678
        context["skills"] = [
            "Python",
            "Django",
            "HTML",
        ]
        return context
