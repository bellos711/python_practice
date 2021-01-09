from django.db import models

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be more than 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        if len(postData['network']) < 2:
            errors['network'] = "Network should be more than 2 characters"
        if len(postData['release_date']) < 5:
            errors['release_date'] = "There should be an appropriate date"
        return errors



class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date=models.DateTimeField()
    desc = models.TextField(default='default description...')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
