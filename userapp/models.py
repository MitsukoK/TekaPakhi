from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class NewUser(AbstractUser):
    # age = models.IntegerField(null=True, blank=True)
    # nickname = models.CharField(max_length=20, null=True, blank=True)
    # MOBILE RECHARGE
    AIRTEL = "Airtel"
    BANGLALINK = "Banglalink"
    GRAMEEN_PHONE = "Grameen Phone"
    ROBI = "Robi"
    TELETALK = "Teletalk"
    # MOBILE BANKING
    MKASH = "Mkash"
    BKASH = "Bkash"
    ROKET = "Roket"
    UPAY = "Upay"
    SURECASH = "Surecash"
    NAGAD = "Nagad"
    # BANK
    ASIA_BANK = "Asia Bank"
    BRACK_BANK = "Brack Bank"
    CITY_BANK = "City Bank"
    DBBL = "DBBL"
    EBL = "EBL"
    EXIM_BANK = "Exim Bank"
    ISLAMI_BANK = "Islami Bank"
    MUTUAL_TRUST_BANK = "Mutual Trust Bank"
    ONE_BANK = "One Bank"
    PRIME_BANK = "Prime Bank"
    UCB_BANK = "UCB Bank"
    # GIFTCARD
    AMAZON = "Amazon"
    GOOGLE_PLAY = "Google Play"

    MOBILE_BANKING = (
        (MKASH, "Mkash"),
        (BKASH, "Bkash"),
        (ROKET, "Roket"),
        (UPAY, "Upay"),
        (SURECASH, "Surecash"),
        (NAGAD, "Nagad"),
    )
    BANK = (
        (ASIA_BANK, "Asia Bank"),
        (BRACK_BANK, "Brack Bank"),
        (CITY_BANK, "City Bank"),
        (DBBL, "DBBL"),
        (EBL, "EBL"),
        (EXIM_BANK, "Exim Bank"),
        (ISLAMI_BANK, "Islami Bank"),
        (MUTUAL_TRUST_BANK, "Mutual Trust Bank"),
        (ONE_BANK, "One Bank"),
        (PRIME_BANK, "Prime Bank"),
        (UCB_BANK, "UCB Bank"),
    )
    GIFT_CARD = (
        (AMAZON, "Amazon"),
        (GOOGLE_PLAY, "Google Play"),
    )
    MOBILE_RECHARGE = (
        (AIRTEL, "Airtel"),
        (BANGLALINK, "Banglalink"),
        (GRAMEEN_PHONE, "Grameen Phone"),
        (ROBI, "Robi"),
        (TELETALK, "Teletalk"),
    )

    phone_number = PhoneNumberField(
        blank=True,
        region="BD",
    )  # type: ignore
    client_identity_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    # client current balance
    current_balance = models.IntegerField(
        validators=[
            MinValueValidator(0_000_000_000_000),
            MaxValueValidator(9_999_999_999_999),
        ],
        default=0,
    )
    user_pin = models.IntegerField(
        validators=[
            MinValueValidator(0_000),
            MaxValueValidator(9_999),
        ],
        default=0000,
    )
    mobile_banking = MultiSelectField(
        choices=MOBILE_BANKING,
        max_length=100,
        default=BKASH,
        # max_choices=5,
    )  # type: ignore
    mobile_recharge = MultiSelectField(
        max_length=100,
        choices=MOBILE_RECHARGE,
        default=AIRTEL,
        # max_choices=4,
    )  # type: ignore
    # gift_card = MultiSelectField(
    #     max_length=100,
    #     choices=GIFT_CARD,
    #     # max_choices=1,
    # )  # type: ignore
    bank = MultiSelectField(
        max_length=100,
        choices=BANK,
        default=DBBL,
        # max_choices=10,
    )  # type: ignore

    # transaction = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    # notification = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)


# TRANSACTION_CHOICES = [
#     (
#         "Mobile Banking",
#         (
#             (MKASH, "Mkash"),
#             (BKASH, "Bkash"),
#             (ROKET, "Roket"),
#             (UPAY, "Upay"),
#             (SURECASH, "Surecash"),
#             (NAGAD, "Nagad"),
#         ),
#     ),
#     (
#         "Bank",
#         (
#             (ASIA_BANK, "Asia Bank"),
#             (BRACK_BANK, "Brack Bank"),
#             (CITY_BANK, "City Bank"),
#             (DBBL, "DBBL"),
#             (EBL, "EBL"),
#             (EXIM_BANK, "Exim Bank"),
#             (ISLAMI_BANK, "Islami Bank"),
#             (MUTUAL_TRUST_BANK, "Mutual Trust Bank"),
#             (ONE_BANK, "One Bank"),
#             (PRIME_BANK, "Prime Bank"),
#             (UCB_BANK, "UCB Bank"),
#         ),
#     ),
#     (
#         "Mobile Recharge",
#         (
#             (AIRTEL, "Airtel"),
#             (BANGLALINK, "Banglalink"),
#             (GRAMEEN_PHONE, "Grameen Phone"),
#             (ROBI, "Robi"),
#             (TELETALK, "Teletalk"),
#         ),
#     ),
#     (
#         "Gift Card",
#         (
#             (AMAZON, "Amazon"),
#             (GOOGLE_PLAY, "Google Play"),
#         ),
#     ),
# ]
