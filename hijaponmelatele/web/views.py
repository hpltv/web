import datetime as dt
import logging

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render

from . import models

logger = logging.getLogger(__name__)


def view(request, public_name):
    config = models.DisplayConfig.objects.get(public_name=public_name)
    context = {
        "config": config,
        "edit": False,
    }
    return render(request, "display.html", context)


def edit(request, private_id):
    config = models.DisplayConfig.objects.get(private_id=private_id)
    context = {
        "config": config,
        "edit": True,
    }
    return render(request, "display.html", context)


def add_url(request, private_id):
    config = models.DisplayConfig.objects.get(private_id=private_id)
    url = request.POST["url"]
    image_url = request.POST["image_url"]
    entry = models.TVEntry(url=url, image_url=image_url)
    entry.save()
    entry.configs.add(config)
    entry.save()
    return redirect("edit", private_id=private_id)


def remove_entry(request, private_id):
    config = models.DisplayConfig.objects.get(private_id=private_id)
    entry_id = request.POST.get("entry_id")
    entry = models.TVEntry.objects.get(id=entry_id)
    config.entries.remove(entry)
    config.save()
    return redirect("edit", private_id=private_id)


DEFAULT_ENTRIES = [
    "tve",
    "Antena 3",
]


def create_config(request):
    title = request.POST["title"]
    suffix = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    config = models.DisplayConfig(public_name=f"{title}-{suffix}")
    config.save()
    for entry_id in DEFAULT_ENTRIES:
        entry = models.TVEntry.objects.get(title=entry_id)
        config.entries.add(entry)
    config.save()
    return redirect("edit", private_id=config.private_id)


def get_meta_tag(soup, value):
    if meta := soup.find("meta", property=value):
        return meta["content"]


def sanitize_url(url):
    return url


def extract_metadata(request):
    url = sanitize_url(request.GET["url"])
    if entry := models.TVEntry.objects.filter(url=url).first():
        return JsonResponse(
            {
                "url": entry.url,
                "image_url": entry.image_url,
            }
        )

    try:
        headers = {"accept-language": "es-ES,es;q=0.9"}
        page = requests.get(url, headers=headers)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")
    except KeyError as e:
        return HttpResponseBadRequest()
    except requests.exceptions.RequestException as e:
        logger.info(f"Failed to extract {url}: {e}")
        return HttpResponseBadRequest()
    meta_url = get_meta_tag(soup, "og:url") or url
    image = get_meta_tag(soup, "og:image")
    if not image:
        return HttpResponseBadRequest()
    return JsonResponse(
        {
            "url": meta_url,
            "image_url": image,
        }
    )
