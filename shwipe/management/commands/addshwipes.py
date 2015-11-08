# Django Command Docs: https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError, NoArgsCommand
from shwipe.models import Product
import requests
import time
import json

# https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/#django.core.management.NoArgsCommand
class Command(NoArgsCommand):
    help = "Load in a Kimono Labs generated json file from a scrapped clothing site."

    def handle_noargs(self, **options):

        r = requests.get('https://0d639da22e13ae7e40a4cbd29d1cfb00e8e0c7a6.googledrive.com/host/0B5JJC6KspfT3OG5sOWl4TFBCRzQ')
        r.encoding = 'utf-8'
        time.sleep(5)
    
  
        products = json.loads(r.content)
        counter = 0
    
        """
        ERROR
        'ascii' codec can't encode character u'\xe1'
        http://stackoverflow.com/questions/8590912/python-throws-unicodeencodeerror-although-i-am-doing-str-decode-why
    
        ERROR
        No JSON object could be decoded
        http://stackoverflow.com/questions/14899506/displaying-better-error-message-than-no-json-object-could-be-decoded
        http://stackoverflow.com/questions/20128772/python-no-json-object-could-be-decoded
        """
        # Example of how to navigate Kimono Labs json:
        # Obj.results.collection1[0].website.text);
        for idx,product in enumerate(products):
            product, created = Product.objects.get_or_create( # docs for get_or_create https://docs.djangoproject.com/en/1.8/ref/models/querysets/#get-or-create
                name=products['results']['collection1'][idx]['product_name']['text'], 
                price=products['results']['collection1'][idx]['product_price'], 
                image=products['results']['collection1'][idx]['product_image']['src'], 
                # threat['details'][0]['country']
            )
            
            counter += 1
            product.save()
        return "%s new product records has been created." % (counter)
    
