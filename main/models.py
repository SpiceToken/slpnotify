from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Token(models.Model):
    name = models.CharField(max_length=100, null=True)
    tokenid = models.CharField(max_length=200, null=True, blank=True)
    confirmation_limit = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

class BlockHeight(models.Model):
    number = models.IntegerField(default=0, unique=True)
    transactions_count = models.IntegerField(default=0)
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    processed = models.BooleanField(default=False)
    currentcount = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_datetime = timezone.now()
        if self.processed:
            self.updated_datetime = timezone.now()
        super(BlockHeight,self).save(*args, **kwargs)

class Transaction(models.Model):
    txid = models.CharField(max_length=200)
    address = models.CharField(max_length=500,null=True)
    amount = models.FloatField(default=0)
    acknowledge = models.BooleanField(default=False)
    blockheight = models.ForeignKey(BlockHeight, on_delete=models.CASCADE, related_name='transactions', null=True)
    source = models.CharField(max_length=200, null=True)
    created_datetime = models.DateTimeField(default=timezone.now)
    token = models.ForeignKey(Token, on_delete=models.DO_NOTHING)
    scanning = models.BooleanField(default=False)
    subscribed = models.BooleanField(default=False)
    spentIndex = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('txid', 'address', 'spentIndex')

    def __str__(self):
        return self.txid

class SendTo(models.Model):
    address = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Send To'
        verbose_name_plural = 'Send To'

class SlpAddress(models.Model):
    address = models.CharField(max_length=200, unique=True)
    transactions = models.ManyToManyField(Transaction, related_name='slpaddress', blank=True)

    class Meta:
        verbose_name = 'SLP Address'
        verbose_name_plural = 'SLP Addresses'
        
    def __str__(self):
        return self.address

class BchAddress(models.Model):
    address = models.CharField(max_length=200, unique=True)
    transactions = models.ManyToManyField(Transaction, related_name='bchaddress', blank=True)
    scanned = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'BCH Address'
        verbose_name_plural = 'BCH Addresses'
        
    def __str__(self):
        return self.address

class Subscription(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE, related_name='subscription', null=True)
    address = models.ManyToManyField(SendTo, related_name='subscription')
    slp = models.ForeignKey(SlpAddress, on_delete=models.CASCADE, related_name='subscription', null=True)
    bch = models.ForeignKey(BchAddress, on_delete=models.CASCADE, related_name='subscription', null=True)

class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscriber')
    subscription = models.ManyToManyField(Subscription, related_name='subscriber')
    confirmed = models.BooleanField(default=False)
    date_started = models.DateTimeField(default=timezone.now)
    telegram_user_details = JSONField(default=dict, blank=True)

    slack_user_details = JSONField(default=dict, null=True, blank=True)
    # slack_user_details = {
    #   "id": string,
    #   "channel_id": string (DM channel ID for the bot to reply to)
    # }
