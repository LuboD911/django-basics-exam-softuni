from django.db import models

class NoteModel(models.Model):

    title = models.CharField(
        max_length=30,
    )

    image_url = models.URLField(

    )

    content = models.TextField(

    )
