from typing import Type
from django.db.models import Model
from django.utils.text import slugify
import uuid

def generate_unique_slug(model: Type[Model], slug: str, base_slug: str = None):
    slug = slugify(slug, allow_unicode=True)

    if not base_slug:
        base_slug = slug

    c = 1
    while model.objects.filter(slug=base_slug).exists():
        base_slug = f'{slug}-{uuid.uuid4().hex[:6]}-{c}'

    return slug
