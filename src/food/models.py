from django.db import models



class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Food Categories'
    def __str__(self):
        return self.name


class Food(models.Model):
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='food_images')
    url = models.CharField(max_length=200)


    def __str__(self):
        return self.name
