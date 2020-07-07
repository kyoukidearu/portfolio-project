from django.db import models
# import datetime

# Create a Blog model
# title
# pub_date
# body
# image

# Add blog app to settings

# Create migration and then migrate

# Add to admin

class Blog(models.Model):

    title = models.CharField(max_length=120)
    # pub_date = datetime.datetime.now().strftime("%m/%d/%Y")
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
