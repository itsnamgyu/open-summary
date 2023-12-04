import json

from django.conf.urls.static import static
from django.db import models

print("Loading parse and summarize modules...")

from parse import parse
from summarize import summarize

print("Completed loading parse and summarize modules")


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    pdf = models.FileField(upload_to="pdfs/")
    preview_image = models.ImageField(upload_to="images/", null=True)

    def parse(self):
        content = parse(self.pdf.path)
        ArticleText.objects.create(article=self, content=json.dumps(content))

    def summarize(self):
        summary = summarize(json.loads(self.parsed.content))
        ArticleSummary.objects.create(article=self, content=summary["total_summary"])
        self.title = summary["title"]
        self.save()

    @property
    def preview_image_url(self):
        if self.preview_image:
            return self.preview_image.url
        return static("core/img/article.jpg")

    def __str__(self):
        return self.title


class ArticleText(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name="parsed")
    content = models.TextField()


class ArticleSummary(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name="summary")
    content = models.TextField()
