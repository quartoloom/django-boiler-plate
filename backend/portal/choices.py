from django.db import models
from .constants import *

class UserTypeChoices(models.TextChoices):
    ADMIN        = ADMIN, ADMIN
    STUDENT      = STUDENT, STUDENT
    STAFF        = STAFF, STAFF

class GenderChoices(models.TextChoices):
    MALE   = MALE, MALE
    FEMALE = FEMALE, FEMALE
    OTHER  = OTHER, OTHER

class PriorityChoices(models.TextChoices):
    HIGH   = HIGH, HIGH
    MEDIUM = MEDIUM, MEDIUM
    LOW    = LOW, LOW

class StatusChoices(models.TextChoices):
    NEW           = NEW,NEW
    IN_PROGRESS   = IN_PROGRESS, IN_PROGRESS
    COMPLETED   = COMPLETED, COMPLETED

class PaymentMethod(models.TextChoices):
    CASH   = CASH, CASH
    ONLINE = ONLINE, ONLINE
    CHEQUE = CHEQUE, CHEQUE

class PaymentStatusChoice(models.TextChoices):
    PENDING = PENDING, PENDING
    SUCCESS = SUCCESS, SUCCESS
    FAILURE = FAILURE, FAILURE
