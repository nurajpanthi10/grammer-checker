from django.db import models


class UserInput(models.Model):
    text = models.TextField()

class CorrectedSentence(models.Model):
    original = models.OneToOneField(UserInput, on_delete=models.CASCADE)
    corrected_text = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
