
# Create your models here.
from django.db import models

# Create your models here.
 
class Author(models.Model):
        name = models.CharField(max_length=255, db_index=True)
        ol_id = models.CharField(max_length=16, unique=True)
        alternate_names = models.CharField(max_length=1024, blank=True)
        year_of_birth = models.CharField(max_length=50, blank=True)
        year_of_death = models.CharField(max_length=50, blank=True)

        class Meta:
                 db_table = "Author"
                 ordering = ['name'] 

        def prepare_author(self, obj):
                 return "%s <%s>" % (obj.user.get_full_name(), obj.user.email)        

