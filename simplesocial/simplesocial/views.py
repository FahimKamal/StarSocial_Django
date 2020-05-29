from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class WelcomePage(TemplateView):
    template_name = 'welcome_page.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
