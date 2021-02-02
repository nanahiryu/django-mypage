from django.views.generic import TemplateView, FormView


class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["num_services"] = 0
        context["skills"] = [
            "Python",
            "Django",
            "HTML",
        ]
        return context


class EveresView(TemplateView):
    template_name = "everes.html"
