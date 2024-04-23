from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / cars_photos/<filename>
    return '{0}/{1}'.format("recipe_photos",filename)


class recipe_data(models.Model):
    recipe_Id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=200, blank=False, null=False )
    recipe_desc = models.CharField(max_length=200, blank=False, null=False)
    recipe_photo = models.FileField(upload_to=user_directory_path, null=True, verbose_name="")

    class Meta:
        db_table = 'recipe' 
