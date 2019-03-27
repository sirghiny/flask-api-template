""""Register application resources."""

from app.common.urls import urls as common_urls


url_sets = [common_urls]


def add_resources(api):
    """Add API resources to routes."""
    for url_set in url_sets:
        for url in url_set:
            api.add_resource(
                url['resource'],
                *url['routes']
            )
    return api
