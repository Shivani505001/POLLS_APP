from django.db import models
#the data base layout
# Create your models here.


class Question(models.Model):
    #we r letiing django that the question of type model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self): #whenever we return the object it will return the question text
        return self.question_text
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #everychoice we create is related to a single question - so foriegn key comes in
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
# Question

# Question_text
# Publish_date


# Choices 

# Choice_text
# No_of_votes
# Link 