from django.db import models

# Create your models here.

class Topic(models.Model):
    """temat poznawany przez uzytkownika"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """zwraca reprezentacje modelu w postaci ciagu tekstowego"""
        return self.text

class Entry(models.Model):
    """konkretne informacje zdobyte na dany temat"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ zwraca reprezentacje modelu w postaci ciagu tekstowego """
        return self.text[:50] + "..."
