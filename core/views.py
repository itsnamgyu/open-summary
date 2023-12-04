import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from time import sleep

from django.core.files import File
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView, DetailView
from django.views.generic.detail import SingleObjectMixin
from pdf2image import convert_from_bytes

from core.forms import ArticleCreateForm
from core.models import Article


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        context["form"] = ArticleCreateForm()
        return context


class ArticleCreateView(FormView):
    form_class = ArticleCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.title = Path(form.cleaned_data["pdf"].name).stem
        pdf = form.cleaned_data["pdf"]
        pages = convert_from_bytes(pdf.file.read())
        if pages:
            with NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                pages[0].save(temp_file.name, "JPEG")
                with open(temp_file.name, "rb") as f:
                    self.object.preview_image.save("preview.jpg", File(f))
                os.remove(temp_file.name)

        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:article", kwargs={"slug": self.object.id})


class ArticleView(DetailView):
    model = Article
    template_name = "core/article.html"
    context_object_name = "article"
    slug_field = "id"


class ArticleParseView(SingleObjectMixin, View):
    model = Article
    slug_field = "id"

    def post(self, request, *args, **kwargs):
        sleep(3)
        article = self.get_object()
        article.parse()
        return HttpResponse("OK")


class ArticleSummarizeView(SingleObjectMixin, View):
    model = Article
    slug_field = "id"

    def post(self, request, *args, **kwargs):
        sleep(3)
        article = self.get_object()
        article.summarize()
        return HttpResponse("OK")


class ArticleResetSummaryView(SingleObjectMixin, View):
    model = Article
    slug_field = "id"

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        if article.parsed:
            article.parsed.delete()
        if article.summary:
            article.summary.delete()
        return HttpResponse("OK")
