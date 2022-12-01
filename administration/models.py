from django.db import models

class allAssessment(models.Model):
    assessmentName = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.assessmentName

class userFeedback(models.Model):
    user_name = models.CharField(max_length=255,null=True)
    feedback = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.user_name

class Question(models.Model):
    quostion= models.CharField(max_length=255,null=True)
    assessment = models.ForeignKey(allAssessment, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.quostion