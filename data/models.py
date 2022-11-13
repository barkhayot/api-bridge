from django.db import models

# Create your models here.
class Data(models.Model):
    product_code    = models.CharField(max_length=255, null=True, blank=True)
    company         = models.CharField(max_length=255, null=True, blank=True)
    weight          = models.CharField(max_length=255, null=True, blank=True)
    product_name    = models.CharField(max_length=255, null=True, blank=True)
    purchase_price  = models.CharField(max_length=255, null=True, blank=True)
    sale_price      = models.CharField(max_length=255, null=True, blank=True)
    profit_rate     = models.CharField(max_length=255, null=True, blank=True)
    progress        = models.CharField(max_length=255, null=True, blank=True)
    event_price     = models.CharField(max_length=255, null=True, blank=True)
    eveent_sale     = models.CharField(max_length=255, null=True, blank=True)
    event_buy       = models.CharField(max_length=255, null=True, blank=True)
    ex_profit_rate  = models.CharField(max_length=255, null=True, blank=True)
    main_category   = models.CharField(max_length=255, null=True, blank=True)
    account         = models.CharField(max_length=255, null=True, blank=True)
    quantity        = models.CharField(max_length=255, null=True, blank=True)
    abc             = models.CharField(max_length=255, null=True, blank=True)
    situation       = models.CharField(max_length=255, null=True, blank=True)
    date_of_change  = models.CharField(max_length=255, null=True, blank=True)
    last_pur_date   = models.CharField(max_length=255, null=True, blank=True)
    last_sale_date  = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.product_code









    
