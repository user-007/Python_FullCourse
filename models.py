from audioop import reverse

from django.db import models
from win32ui import CreateView


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, deault="https://livings......")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_disc', 'item_price', 'item_image']

    def form_valid(self, form):
        form.instance.user_name = self.request.user

    # return super().form_valid(form)
