from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Person(models.Model):
    name            = models.CharField(max_length=200)
    name_short      = models.CharField(max_length=100, blank=True)
    company         = models.CharField(max_length=200, blank=True)
    company_short   = models.CharField(max_length=100, blank=True)
    country         = models.CharField(max_length=50, blank=True)
    city            = models.CharField(max_length=50, blank=True)
    zip_code        = models.CharField(max_length=15, blank=True)
    address         = models.CharField(max_length=100, blank=True)
    email           = models.EmailField()
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone           = models.CharField(validators=[phone_regex], max_length=15)
    comment         = models.CharField(max_length=500, blank=True)
    birthday        = models.DateField(blank=True)
    agent           = models.CharField(max_length=200, blank=True)
    agent_short     = models.CharField(max_length=100, blank=True)
    client          = models.BooleanField(default=False)
    model           = models.BooleanField(default=False)
    photographe     = models.BooleanField(default=False)
    make_up         = models.BooleanField(default=False)
    styling         = models.BooleanField(default=False)
    other           = models.BooleanField(default=False)
    comment_other   = models.CharField(max_length=200, blank=True)
    sedcard_cost    = models.IntegerField(null=True, blank=True)
    sedcard_payed   = models.IntegerField(null=True, blank=True)
    sedcard_statut  = models.BooleanField(default=False)
    bank_regex      = RegexValidator(regex=r'^DE\d{2}\s?([0-9a-zA-Z]{4}\s?){4}[0-9a-zA-Z]{2}$', message="Bank account must be entered in the format: 'DE12 3456 7890 1234 5678 90'. Up to 27 digits allowed.")
    bank_account    = models.CharField(validators=[bank_regex], max_length=27)
    IBAN            = models.CharField(max_length=200, blank=True)
    website         = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Project(models.Model):
    name                    = models.CharField(max_length=200)
    client                  = models.ForeignKey(Person, on_delete=models.CASCADE)
    start                   = models.DateField()
    finish                  = models.DateField()
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    comment                 = models.CharField(max_length=500, blank=True)
    sort                    = models.CharField(max_length=8, choices=(('Angebot', 'angebot'), ('Auftrag', 'aufttrag'), ('Job', 'job'),), default='Angebot')
    all_day                 = models.IntegerField(null=True, blank=True)
    half_day                = models.IntegerField(null=True, blank=True)
    half_day_price_pro      = models.IntegerField(null=True, blank=True)
    all_day_price_pro       = models.IntegerField(null=True, blank=True)
    over_price_pro          = models.IntegerField(null=True, blank=True)
    all_in_price_pro        = models.IntegerField(null=True, blank=True)
    half_day_price_semipro  = models.IntegerField(null=True, blank=True)
    all_day_price_semipro   = models.IntegerField(null=True, blank=True)
    over_price_semipro      = models.IntegerField(null=True, blank=True)
    all_in_price_semipro    = models.IntegerField(null=True, blank=True)
    country                 = models.CharField(max_length=50, blank=True)
    city                    = models.CharField(max_length=50, blank=True)
    zip_code                = models.CharField(max_length=15, blank=True)
    address                 = models.CharField(max_length=100, blank=True)
    comment_address         = models.CharField(max_length=500, blank=True)
    honorary_base           = models.IntegerField(null=True, blank=True)
    honorary_plus           = models.IntegerField(null=True, blank=True)
    quantity_models_honorary_plus = models.IntegerField(null=True, blank=True)
    ms_price                = models.IntegerField(null=True, blank=True)
    ms_hours                = models.IntegerField(null=True, blank=True)
    requirement_price       = models.IntegerField(null=True, blank=True)
    requirement_hours       = models.IntegerField(null=True, blank=True)
    requisiten_price_for_each_model = models.IntegerField(null=True, blank=True)
    other_title             = models.CharField(max_length=50, blank=True)
    other_description       = models.CharField(max_length=200, blank=True)
    other_price             = models.IntegerField(null=True, blank=True)
    other_hours             = models.IntegerField(null=True, blank=True)
    photo_price             = models.IntegerField(null=True, blank=True)
    photo_hours             = models.IntegerField(null=True, blank=True)
    total_price             = models.IntegerField(null=True, blank=True)
    tax                     = models.IntegerField(default=19)
    statut                  = models.CharField(max_length=9, choices=(('Draft', 'draft'), ('yyy', 'active'), ('xxx', 'facture_sent'), ('bezhal', 'payed'), ('Absagen', 'canceled'),), default='Draft')

    class Meta:
        verbose_name        = 'Project'
        verbose_name_plural = 'Projects'
        
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
    


class Attachment(models.Model):
    sort            = models.CharField(max_length=9, choices=(('angebot', 'angebot'), ('aufttrag', 'aufttrag'), ('job', 'job'), ('facture_client', 'facture_client'), ('facture_person', 'facture_person'),), default='angebot')
    file            = models.FileField()
    send_date       = models.DateField()
    answer_date     = models.DateField(null=True, blank=True)
    statut          = models.CharField(max_length=14, choices=(('waiting answer', 'waiting answer'), ('accepted', 'accepted'), ('rejected', 'rejected'),), default='waiting answer')
    comment_WG      = models.CharField(max_length=500, blank=True)
    comment_client  = models.CharField(max_length=500, blank=True)
    project         = models.ForeignKey(Project, on_delete=models.CASCADE)
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name        = 'Attachment'
        verbose_name_plural = 'Attachments'

    def __str__(self):
        return self.sort


class Assignment(models.Model):
    project             = models.ForeignKey(Project, on_delete=models.CASCADE)
    person              = models.ForeignKey(Person, on_delete=models.CASCADE)
    model_type          = models.CharField(max_length=14, choices=(('pro', 'pro'), ('semipro', 'semipro'),), default='pro')
    travel_cost         = models.IntegerField(null=True, blank=True)
    hotel_cost          = models.IntegerField(null=True, blank=True)
    other_cost          = models.IntegerField(null=True, blank=True)
    comment_WG          = models.CharField(max_length=500, blank=True)
    comment_model       = models.CharField(max_length=500, blank=True)
    statut              = models.CharField(max_length=14, choices=(('created', 'created'), ('waiting answer', 'waiting answer'), ('confirmed', 'confirmed'), ('not possible', 'not possible'), ('realized', 'realized'), ('acquitted', 'acquitted'),), default='created')
    send_date           = models.DateField(null=True, blank=True)
    confirmation_date   = models.DateField(null=True, blank=True)
    payment_date        = models.DateField(null=True, blank=True)
    total_price         = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name        = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return self.person.name + ' - ' + self.project.name

    def get_absolute_url(self):
        return reverse('assignment_detail', kwargs={'pk': self.pk})


class Horaire(models.Model):
    assignment      = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    date            = models.DateField()
    start_time      = models.TimeField()
    finish_time     = models.TimeField()
    start_time_real = models.TimeField(null=True, blank=True)
    finish_time_real= models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name        = 'Horaire'
        verbose_name_plural = 'Horaires'

    def get_absolute_url(self):
        return reverse('horaire_detail', kwargs={'pk': self.pk})


class Cost(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    date    = models.DateField()
    amount  = models.IntegerField()
    title   = models.CharField(max_length=100)
    statut  = models.CharField(max_length=14, choices=(('planned', 'planned'), ('complete', 'complete'),), default='planned')

    class Meta:
        verbose_name        = 'Cost'
        verbose_name_plural = 'Costs'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cost_detail', kwargs={'pk': self.pk})


class Time(models.Model):
    title       = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    comment     = models.CharField(max_length=500, blank=True)
    date        = models.DateField()
    start_time  = models.TimeField()
    finish_time = models.TimeField()
    project     = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name        = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('time_detail', kwargs={'pk': self.pk})
