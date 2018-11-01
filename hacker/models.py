from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from multiselectfield import MultiSelectField

SHIRT_SIZE_CHOICES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
) 

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('NB', 'Non-binary'),
    ('NA', 'Prefer not to disclose'),
)

CLASSIFICATION_CHOICES = (
    ('U1', 'U1'),
    ('U2', 'U2'),
    ('U3', 'U3'),
    ('U4', 'U4'),
    ('U5', 'U5'),
)


DIETARY_RESTRICTION_CHOICES = (
    ('Vegan', 'Vegan'),
    ('Vegaterian', 'Vegarterian'),
    ('Halal', 'Halal'),
    ('Kosher', 'Kosher'),
    ('Food Allergies', 'Food Allergies'),
)

GRAD_YEAR_CHOICES = [(i,i) for i in range(timezone.now().year, timezone.now().year + 6)]        # TO-DO TEST


class Hacker(AbstractUser):
    admitted = models.NullBooleanField(blank=True)
    checked_in = models.NullBooleanField(blank=True)
    admitted_datetime = models.DateTimeField(null=True, blank=True)
    checked_in_datetime = models.DateTimeField(null=True, blank=True)

    # Overrides AbstractUser.first_name to require not blank
<<<<<<< HEAD
    first_name = models.CharField(max_length=30, blank=False, verbose_name='First Name')

    # Overrides AbstractUser.last_name to require not blank
    last_name = models.CharField(max_length=150, blank=False, verbose_name='Last Name')
=======
    first_name = models.CharField(max_length=30, blank=False, verbose_name='first name')

    # Overrides AbstractUser.last_name to require not blank
    last_name = models.CharField(max_length=150, blank=False, verbose_name='last name')
>>>>>>> 109ebc8217e1148a45e8ae06c434fc09a9cf5923
    
    # Overrides AbstractUser.email to require not blank
    email = models.EmailField(blank=False)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
<<<<<<< HEAD


class HackerProfile(models.Model):
    hacker = models.OneToOneField(          # TO-DO TEST
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    major = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    classification = models.CharField(choices=CLASSIFICATION_CHOICES, max_length=2)
    grad_year = models.IntegerField(choices=GRAD_YEAR_CHOICES, verbose_name='Graduation Year')

    class Meta:         # TO-DO TEST
=======


class HackerProfile(models.Model):
    # should only include Hackers w/ verified emails, w/ active status, w/o pre-existing application
    major = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    classification = models.CharField(choices=CLASSIFICATION_CHOICES, max_length=2)
    grad_year = models.IntegerField(choices=GRAD_YEAR_CHOICES, verbose_name='graduation year')
    hacker = models.OneToOneField(          
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:         
>>>>>>> 109ebc8217e1148a45e8ae06c434fc09a9cf5923
        abstract = True


class Application(HackerProfile):
<<<<<<< HEAD
    #resume = models.FileField( ... )           # TO-DO TEST
    interests = models.TextField(max_length=200)
    essay = models.TextField(max_length=200)
    approved = models.NullBooleanField(blank=True)
    date_approved = models.DateField(null=True, blank=True)         # TO-DO TEST
    date_submitted = models.DateField(auto_now_add=True, blank=True)
    notes = models.TextField(max_length=300, blank=True, help_text='Provide any additional notes and/or comments in the text box provide')


=======
    #resume = models.FileField( ... )           
    interests = models.TextField(max_length=200)
    essay = models.TextField(max_length=200)
    approved = models.NullBooleanField(blank=True)
    date_approved = models.DateField(null=True, blank=True)         
    date_submitted = models.DateField(auto_now_add=True, blank=True)
    notes = models.TextField(max_length=300, blank=True, help_text='Provide any additional notes and/or comments in the text box provide')

>>>>>>> 109ebc8217e1148a45e8ae06c434fc09a9cf5923
    def __str__(self):
        return '%s, %s - Profile' % (self.hacker.last_name, self.hacker.first_name)


class Confirmation(models.Model):
<<<<<<< HEAD
    shirt_size = models.CharField(          # TO-DO TEST
        max_length=3,
        choices=SHIRT_SIZE_CHOICES,
        verbose_name='Shirt Size',
    )
    dietary_restrictions = MultiSelectField(choices=DIETARY_RESTRICTION_CHOICES, verbose_name='Dietary Restrictions', blank=True)                                                # TO-DO TEST
    travel_reimbursement_required = models.BooleanField(default=False)          # TO-DO TEST
    date_confirmed = models.DateField(auto_now_add=True, blank=True)
    notes = models.TextField(max_length=300, blank=True, help_text='Provide any additional notes and/or comments in the text box provide')
    hacker = models.OneToOneField(              # TO-DO TEST
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(           # TO-DO TEST
=======
    dietary_restrictions = MultiSelectField(choices=DIETARY_RESTRICTION_CHOICES, verbose_name='dietary restrictions', blank=True)                                                # TO-DO TEST
    travel_reimbursement_required = models.BooleanField(default=False)          
    date_confirmed = models.DateField(auto_now_add=True, blank=True)
    notes = models.TextField(max_length=300, blank=True, help_text='Provide any additional notes and/or comments in the text box provide')
    shirt_size = models.CharField(         
        max_length=3,
        choices=SHIRT_SIZE_CHOICES,
        verbose_name='shirt size',
    )
    hacker = models.OneToOneField(              
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(           
>>>>>>> 109ebc8217e1148a45e8ae06c434fc09a9cf5923
        'Team', 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
    )

    def __str__(self):
        return '%s, %s - Confirmation' % (self.hacker.last_name, self.hacker.first_name)


class Team(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
<<<<<<< HEAD

'''
class Wave(models.Model):
    confirmation_period_start = models.DateTimeField()
    confirmation_period_end = models.DateTimeField()
'''

=======
    

# `Hacker.admitted` Values:
    #       1. 'True' - application approved & confirmation period has begun
    #       2. 'False' - application approved & confirmation period has NOT begun
    #       3. 'NULL' - application rejected, pending review, cancelled, or DNE

# Possible Values:
    #       1. 'True' - has been checked in by staff/volunteers (day of event)
    #       2. 'False' - has NOT been checked in by staff/volunteers (day of event)
    #       3. 'NULL' - will not be attending event
>>>>>>> 109ebc8217e1148a45e8ae06c434fc09a9cf5923
