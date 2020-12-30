import requests
import time
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from hijaponmelatele.web import models


def get_meta_tag(soup, value):
    if meta := soup.find("meta", property=value):
        return meta["content"]


def parse_netflix_link(url):
    headers = {"accept-language": "es-ES,es;q=0.9"}
    page = requests.get(url, headers=headers)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, "html.parser")
    if title := get_meta_tag(soup, "og:title"):
        title = title.split("|")[0].strip()
    meta_url = get_meta_tag(soup, "og:url")
    image = get_meta_tag(soup, "og:image")
    return models.TVEntry(
        title=title,
        url=meta_url,
        image_url=image,
    )


initial_links = [
    "https://www.netflix.com/watch/562050",
    "https://www.netflix.com/watch/60000724",
    "https://www.netflix.com/watch/60000901",
    "https://www.netflix.com/watch/60004478",
    "https://www.netflix.com/watch/60024925",
    "https://www.netflix.com/watch/60034567",
    "https://www.netflix.com/watch/70021660",
    "https://www.netflix.com/watch/70033005",
    "https://www.netflix.com/watch/70136102",
    "https://www.netflix.com/watch/70136107",
    "https://www.netflix.com/watch/70140358",
    "https://www.netflix.com/watch/70140450",
    "https://www.netflix.com/watch/70140457",
    "https://www.netflix.com/watch/70143824",
    "https://www.netflix.com/watch/70143843",
    "https://www.netflix.com/watch/70143844",
    "https://www.netflix.com/watch/70143858",
    "https://www.netflix.com/watch/70153382",
    "https://www.netflix.com/watch/70155547",
    "https://www.netflix.com/watch/70155589",
    "https://www.netflix.com/watch/70155618",
    "https://www.netflix.com/watch/70172485",
    "https://www.netflix.com/watch/70178217",
    "https://www.netflix.com/watch/70178604",
    "https://www.netflix.com/watch/70180387",
    "https://www.netflix.com/watch/70187741",
    "https://www.netflix.com/watch/70195800",
    "https://www.netflix.com/watch/70202138",
    "https://www.netflix.com/watch/70202589",
    "https://www.netflix.com/watch/70204970",
    "https://www.netflix.com/watch/70205012",
    "https://www.netflix.com/watch/70205672",
    "https://www.netflix.com/watch/70219484",
    "https://www.netflix.com/watch/70221402",
    "https://www.netflix.com/watch/70242081",
    "https://www.netflix.com/watch/70242311",
    "https://www.netflix.com/watch/70264888",
    "https://www.netflix.com/watch/70266676",
    "https://www.netflix.com/watch/70281312",
    "https://www.netflix.com/watch/70281562",
    "https://www.netflix.com/watch/70283264",
    "https://www.netflix.com/watch/70285581",
    "https://www.netflix.com/watch/70300800",
    "https://www.netflix.com/watch/70301870",
    "https://www.netflix.com/watch/70302482",
    "https://www.netflix.com/watch/70304358",
    "https://www.netflix.com/watch/80002479",
    "https://www.netflix.com/watch/80017537",
    "https://www.netflix.com/watch/80021955",
    "https://www.netflix.com/watch/80024057",
    "https://www.netflix.com/watch/80025172",
    "https://www.netflix.com/watch/80025384",
    "https://www.netflix.com/watch/80025494",
    "https://www.netflix.com/watch/80025678",
    "https://www.netflix.com/watch/80026226",
    "https://www.netflix.com/watch/80027158",
    "https://www.netflix.com/watch/80027159",
    "https://www.netflix.com/watch/80027563",
    "https://www.netflix.com/watch/80036140",
    "https://www.netflix.com/watch/80049832",
    "https://www.netflix.com/watch/80050063",
    "https://www.netflix.com/watch/80051137",
    "https://www.netflix.com/watch/80057134",
    "https://www.netflix.com/watch/80057281",
    "https://www.netflix.com/watch/80059465",
    "https://www.netflix.com/watch/80074249",
    "https://www.netflix.com/watch/80077977",
    "https://www.netflix.com/watch/80084447",
    "https://www.netflix.com/watch/80094318",
    "https://www.netflix.com/watch/80095532",
    "https://www.netflix.com/watch/80095697",
    "https://www.netflix.com/watch/80100172",
    "https://www.netflix.com/watch/80100929",
    "https://www.netflix.com/watch/80103417",
    "https://www.netflix.com/watch/80108473",
    "https://www.netflix.com/watch/80109415",
    "https://www.netflix.com/watch/80113647",
    "https://www.netflix.com/watch/80113701",
    "https://www.netflix.com/watch/80115297",
    "https://www.netflix.com/watch/80117038",
    "https://www.netflix.com/watch/80117470",
    "https://www.netflix.com/watch/80117526",
    "https://www.netflix.com/watch/80117540",
    "https://www.netflix.com/watch/80117551",
    "https://www.netflix.com/watch/80117552",
    "https://www.netflix.com/watch/80117694",
    "https://www.netflix.com/watch/80117809",
    "https://www.netflix.com/watch/80120640",
    "https://www.netflix.com/watch/80126024",
    "https://www.netflix.com/watch/80133311",
    "https://www.netflix.com/watch/80134695",
    "https://www.netflix.com/watch/80134797",
    "https://www.netflix.com/watch/80135674",
    "https://www.netflix.com/watch/80136311",
    "https://www.netflix.com/watch/80141259",
    "https://www.netflix.com/watch/80150243",
    "https://www.netflix.com/watch/80160037",
    "https://www.netflix.com/watch/80160935",
    "https://www.netflix.com/watch/80174285",
    "https://www.netflix.com/watch/80177342",
    "https://www.netflix.com/watch/80179190",
    "https://www.netflix.com/watch/80179905",
    "https://www.netflix.com/watch/80186475",
    "https://www.netflix.com/watch/80186863",
    "https://www.netflix.com/watch/80189024",
    "https://www.netflix.com/watch/80189221",
    "https://www.netflix.com/watch/80189685",
    "https://www.netflix.com/watch/80191236",
    "https://www.netflix.com/watch/80192098",
    "https://www.netflix.com/watch/80195828",
    "https://www.netflix.com/watch/80197526",
    "https://www.netflix.com/watch/80198991",
    "https://www.netflix.com/watch/80199682",
    "https://www.netflix.com/watch/80200942",
    "https://www.netflix.com/watch/80201035",
    "https://www.netflix.com/watch/80202811",
    "https://www.netflix.com/watch/80203144",
    "https://www.netflix.com/watch/80204890",
    "https://www.netflix.com/watch/80209013",
    "https://www.netflix.com/watch/80209379",
    "https://www.netflix.com/watch/80211991",
    "https://www.netflix.com/watch/80213115",
    "https://www.netflix.com/watch/80216752",
    "https://www.netflix.com/watch/80218306",
    "https://www.netflix.com/watch/80219707",
    "https://www.netflix.com/watch/80220145",
    "https://www.netflix.com/watch/80221207",
    "https://www.netflix.com/watch/80221317",
    "https://www.netflix.com/watch/80223989",
    "https://www.netflix.com/watch/80232398",
    "https://www.netflix.com/watch/80232920",
    "https://www.netflix.com/watch/80233962",
    "https://www.netflix.com/watch/80234304",
    "https://www.netflix.com/watch/80234451",
    "https://www.netflix.com/watch/80237428",
    "https://www.netflix.com/watch/80238399",
    "https://www.netflix.com/watch/80238565",
    "https://www.netflix.com/watch/80240027",
    "https://www.netflix.com/watch/80241001",
    "https://www.netflix.com/watch/80244645",
    "https://www.netflix.com/watch/80988856",
    "https://www.netflix.com/watch/80988988",
    "https://www.netflix.com/watch/80989924",
    "https://www.netflix.com/watch/80993876",
    "https://www.netflix.com/watch/80994666",
    "https://www.netflix.com/watch/80994878",
    "https://www.netflix.com/watch/80997965",
    "https://www.netflix.com/watch/81002370",
    "https://www.netflix.com/watch/81002747",
    "https://www.netflix.com/watch/81004278",
    "https://www.netflix.com/watch/81005492",
    "https://www.netflix.com/watch/81006858",
    "https://www.netflix.com/watch/81017308",
    "https://www.netflix.com/watch/81019069",
    "https://www.netflix.com/watch/81022683",
    "https://www.netflix.com/watch/81026818",
    "https://www.netflix.com/watch/81033361",
    "https://www.netflix.com/watch/81034553",
    "https://www.netflix.com/watch/81037371",
    "https://www.netflix.com/watch/81037871",
    "https://www.netflix.com/watch/81045007",
    "https://www.netflix.com/watch/81051782",
    "https://www.netflix.com/watch/81055408",
    "https://www.netflix.com/watch/81073507",
    "https://www.netflix.com/watch/81075536",
    "https://www.netflix.com/watch/81075958",
    "https://www.netflix.com/watch/81083590",
    "https://www.netflix.com/watch/81088239",
    "https://www.netflix.com/watch/81090319",
    "https://www.netflix.com/watch/81091825",
    "https://www.netflix.com/watch/81094391",
    "https://www.netflix.com/watch/81098497",
    "https://www.netflix.com/watch/81115994",
    "https://www.netflix.com/watch/81144163",
    "https://www.netflix.com/watch/81160045",
    "https://www.netflix.com/watch/81167570",
    "https://www.netflix.com/watch/81168939",
    "https://www.netflix.com/watch/81186615",
    "https://www.netflix.com/watch/81196277",
    "https://www.netflix.com/watch/81237854",
    "https://www.netflix.com/watch/81238721",
    "https://www.netflix.com/watch/81254224",
    "https://www.netflix.com/watch/81266684",
    "https://www.netflix.com/watch/81272752",
    "https://www.netflix.com/watch/81277950",
    "https://www.netflix.com/watch/81291299",
    "https://www.netflix.com/watch/81312563",
    "https://www.netflix.com/watch/81332175",
    "https://www.netflix.com/watch/81344378",
]



class Command(BaseCommand):
    help = "Adds content from netflix"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str)

    def _add_url(self, url):
        try:
            entry = parse_netflix_link(url)
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Failed to add {url}: {e!r}"))
            return
        if not entry.title:
            self.stdout.write(self.style.ERROR(f"Failed to add {url}"))
            return
        try:
            entry.save()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to add {entry}: {e!r}"))
            return
        else:
            self.stdout.write(self.style.SUCCESS(f"Successfully added {entry}"))

    def handle(self, *args, **options):
        url = options["url"]
        if url != "initial-load":
            self._add_url(url)
        else:
            for url in initial_links:
                self._add_url(url)
                time.sleep(60)
