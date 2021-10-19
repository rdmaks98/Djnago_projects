from django.utils.text import slugify
import string
import random


# slug make random using this method
def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

# call in blogmodel sulg field to create new slug
def generate_slug(text):
    new_slug = slugify(text)
    from home.models import BlogModel
    if BlogModel.objects.filter(slug=new_slug).first():
        return generate_slug(text + generate_random_string(7))
    return new_slug