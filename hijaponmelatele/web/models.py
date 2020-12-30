import uuid
from urllib.parse import urlparse

from django.db import models

PROVIDER_URL_DOMAINS = [
    ("netflix", "netflix"),
]


def create_id():
    return str(uuid.uuid4())


class TVEntry(models.Model):
    id = models.AutoField(primary_key=True, editable=False, blank=True)
    title = models.CharField(max_length=100, db_index=True, unique=True)
    url = models.URLField(max_length=200, db_index=True)
    image_url = models.URLField(max_length=200)

    def portal(self):
        domain = urlparse(self.url).netloc
        for domain_name, domain_match in PROVIDER_URL_DOMAINS:
            if domain_match in domain:
                return domain_name
        return "other"

    def __repr__(self):
        return str(self.title)

    __str__ = __repr__


class DisplayConfig(models.Model):
    id = models.AutoField(primary_key=True, editable=False, blank=True)
    public_name = models.CharField(max_length=100, unique=True, db_index=True)
    private_id = models.CharField(
        max_length=64,
        editable=False,
        unique=True,
        db_index=True,
        default=create_id,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, db_index=True, blank=True
    )
    entries = models.ManyToManyField(TVEntry, related_name="configs")

    def __repr__(self):
        return self.public_name

    __str__ = __repr__
