from django.db import models


class Model(models.Model):
    auto_field = models.AutoField(primary_key=True)
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    float_field = models.FloatField()
    # many_to_many_field = models.ManyToManyField(OtherModel)
    # foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    # one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE)
    
    # image_field = models.ImageField(upload_to='images/')
    json_field = models.JSONField() 
    text_field = models.TextField()