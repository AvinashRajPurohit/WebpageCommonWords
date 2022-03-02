from django.db import models

# Create your models here.


class WebSiteEssentials(models.Model):
    """Model that will record the  website's essentials information."""
    # website name can work as index data (Task: 7)
    website_name = models.CharField(max_length=100, unique=True)
    html_content = models.TextField()
    # will have only clean data because we are only going to work with it.
    clean_html_content = models.TextField(blank=True, null=True)
    # calculate words once and use many times
    clean_corpus_words = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.website_name

