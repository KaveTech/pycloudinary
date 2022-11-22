from cloudinary.api_client.call_api import call_json_api, call_api
from cloudinary.utils import chunks


def ping(**options):
    options["is_mo"] = True
    return call_api("get", ["ping"], {}, **options)


def invalidate(*urls, **options):
    options["is_mo"] = True
    results = []
    for chunk in chunks(urls, 20):
        results.append(
            call_json_api("post", ["cache_invalidate"], {"urls": chunk}, **options)
        )
    return results


def warm_up(url, **options):
    options["is_mo"] = True
    return call_json_api("post", ["cache_warm_up"], {"url": url}, **options)
