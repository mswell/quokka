# coding: utf-8

from quokka.core.models import Channel


def configure(app):
    @app.before_first_request
    def initialize():
        print "Called only once, when the first request comes in"
        if not Channel.objects.count():
            # Create homepage if it does not exists
            Channel.objects.create(
                title="home",
                slug="home",
                description="App homepage",
                is_homepage=True,
                include_in_rss=True,
                indexable=True,
                show_in_menu=True,
                canonical_url="/",
                order=0,
                published=True,
            )