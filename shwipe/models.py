# https://docs.djangoproject.com/en/1.8/topics/db/models/
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
import sys

from django.db.models.signals import post_syncdb

from allauth.utils import get_current_site
from allauth.socialaccount.providers import registry
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.oauth.provider import OAuthProvider
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

def setup_dummy_social_apps(sender, **kwargs):
    """
    `allauth` needs tokens for OAuth based providers. So let's
    setup some dummy tokens
    """
    request = kwargs.get('request')

    site = get_current_site(request)
    for provider in registry.get_list():
        if (isinstance(provider, OAuth2Provider)
            or isinstance(provider, OAuthProvider)):
            try:
                SocialApp.objects.get(provider=provider.id,
                                      sites=site)
            except SocialApp.DoesNotExist:
                print ("Installing dummy application credentials for %s."
                       " Authentication via this provider will not work"
                       " until you configure proper credentials via the"
                       " Django admin (`SocialApp` models)" % provider.id)
                app = SocialApp.objects.create(provider=provider.id,
                                               secret='secret',
                                               client_id='client-id',
                                               name='Dummy %s app' % provider.id)
                app.sites.add(site)


# We don't want to interfere with unittests et al
if 'syncdb' in sys.argv:
    post_syncdb.connect(setup_dummy_social_apps, sender=sys.modules[__name__])


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.URLField(blank=True, null=True, unique=True)
    price = models.CharField(max_length=255)
    shwiped = models.BooleanField(default=False)
    
    def __str__(self):
        return unicode(self.name)

class Shwiper(models.Model):
    user = models.OneToOneField(User)
    product = models.ForeignKey(Product)