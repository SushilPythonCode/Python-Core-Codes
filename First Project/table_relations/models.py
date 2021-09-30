from django.db import models


class Subcategory(models.Model):
	name = models.CharField(max_length = 100)
	size = models.CharField(max_length = 100)

	# sub = models.ForeignKey(Category, on_delete = models.CASCADE)


class Category(models.Model):
	name = models.CharField(max_length = 100)
	sub = models.ForeignKey(Subcategory, on_delete = models.CASCADE)

class Product(models.Model):
	name = models.CharField(max_length = 100)
	cat = models.ForeignKey(Category,on_delete=models.CASCADE)
	sub = models.ForeignKey(Subcategory, on_delete = models.CASCADE)

# from django.db import models


# class Subcategory(models.Model):
# 	name = models.CharField(max_length = 100)
# 	# sub = models.ForeignKey(Category, on_delete = models.CASCADE)


# class Category(models.Model):
# 	name = models.CharField(max_length = 100)

# class Product(models.Model):
# 	name = models.CharField(max_length = 100)
# 	size = models.CharField(max_length = 100)
# 	cat = models.ForeignKey(Category,on_delete=models.CASCADE)
# 	sub_cat = models.ForeignKey(Subcategory,on_delete=models.CASCADE)