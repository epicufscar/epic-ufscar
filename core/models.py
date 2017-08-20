import os
from django.db import models
from django.dispatch import receiver


# CONTENT: models the website content
# Contents should have a headline and they must be written in HTML format
# Contents should also include all styles and scripts it needs
class Content(models.Model):
    class Meta:
        verbose_name = 'conteúdo'
        verbose_name_plural = 'conteúdos'

    def __str__(self):
        return '[' + self.content_id + '] ' + self.headline

    content_id = models.CharField(blank=False, unique=True, max_length=25, verbose_name='ID textual')
    headline = models.CharField(blank=False, max_length=200, verbose_name='título')
    html_text = models.TextField(blank=False, verbose_name='conteúdo HTML')


# IMAGE CONTENT: stores images needed for contents
# Image paths can be included in appropriate HTML tags to create the website contents
class ImageContent(models.Model):
    class Meta:
        verbose_name = 'imagem'
        verbose_name_plural = 'imagens'

    def __str__(self):
        return str(self.image)

    alt = models.CharField(blank=True, max_length=50, verbose_name='texto alternativo (ALT)')
    image = models.ImageField(blank=False, upload_to='core/static/images/content/', verbose_name='imagem')


# MEMBERS: models the team members' information
class Members(models.Model):
    class Meta:
        verbose_name = 'membro'
        verbose_name_plural = 'membros'

    def __str__(self):
        return self.full_name.split()[0] + ' ' + self.full_name.split()[-1]

    STATUS = (
        ('AT', 'Ativo'),
        ('IN', 'Inativo'),
        ('AF', 'Afastado')
    )

    TYPE = (
        ('COOR', 'Docente Coordenador'),
        ('GRAD', 'Estudante de Graduação'),
        ('EXTR', 'Participante Externo')
    )

    PROGRAM = (
        ('BCC', 'Bacharelado em Ciência da Computação'),
        ('EnC', 'Engenharia de Computação')
    )

    full_name = models.CharField(blank=False, max_length=100, verbose_name='nome completo')
    email = models.CharField(blank=True, max_length=100, verbose_name='email')
    linkedin = models.CharField(blank=True, max_length=50, verbose_name='LinkedIn ID')
    github = models.CharField(blank=True, max_length=50, verbose_name='GitHub ID')
    program = models.CharField(blank=True, max_length=3, choices=PROGRAM, verbose_name='curso')
    type = models.CharField(blank=False, max_length=4, choices=TYPE, verbose_name='tipo')
    status = models.CharField(blank=False, max_length=2, choices=STATUS, verbose_name='status')
    dateIn = models.DateField(blank=False, verbose_name='data de início')
    dateOut = models.DateField(blank=True, null=True, verbose_name='data de saída')
    image = models.ImageField(blank=True, upload_to='core/static/images/members/', verbose_name='foto')


# PLAN TYPE: defines financial plans types
class PlanType(models.Model):
    class Meta:
        verbose_name = 'tipo de plano de apoio'
        verbose_name_plural = 'tipos de plano de apoio'

    def __str__(self):
        return self.type

    type = models.CharField(blank=False, max_length=25, verbose_name='tipo')


# PLAN BENEFIT: lists benefits for each Plan
class PlanBenefit(models.Model):
    class Meta:
        ordering = ['priority']
        verbose_name = 'benefício de plano de apoio'
        verbose_name_plural = 'benefícios de plano de apoio'

    def __str__(self):
        return str(self.priority) + ' - [' + self.type.type + '] ' + self.benefit

    type = models.ForeignKey(PlanType, blank=False, verbose_name='tipo')
    priority = models.PositiveIntegerField(blank=False, unique=True, verbose_name='prioridade')
    benefit = models.CharField(blank=False, max_length=500, verbose_name='benefício')


# PLAN: lists princing plans for financial support
class Plan(models.Model):
    class Meta:
        verbose_name = 'plano de apoio'
        verbose_name_plural = 'planos de apoio'

    def __str__(self):
        return '[' + self.type.type + '] ' + self.name

    type = models.ForeignKey(PlanType, blank=False, verbose_name='tipo')
    name = models.CharField(blank=False, max_length=25, verbose_name='nome')
    price = models.FloatField(blank=False, verbose_name='valor')
    benefits = models.ManyToManyField(PlanBenefit, blank=False, verbose_name='benefícios')


# SUPPORTER: models financial supporters
class Supporters(models.Model):
    class Meta:
        verbose_name = 'Apoiador'
        verbose_name_plural = 'Apoiadores'

    def __str__(self):
        return self.name

    STATUS = (
        ('AT', 'Ativo'),
        ('IN', 'Inativo'),
        ('SP', 'Sem Pagamento')
    )

    name = models.CharField(blank=False, max_length=100, verbose_name='nome')
    brand = models.CharField(blank=True, max_length=100, verbose_name='organização')
    email = models.CharField(blank=False, max_length=100, verbose_name='email')
    fone = models.CharField(blank=True, max_length=20, verbose_name='telefone')
    page = models.CharField(blank=True, max_length=100, verbose_name='site')
    plan = models.ForeignKey(Plan, blank=False, verbose_name='plano')
    value = models.FloatField(blank=False, verbose_name='valor')
    start_date = models.DateField(blank=False, null=True, verbose_name='data de início')
    end_date = models.DateField(blank=True, null=True, verbose_name='data de fim')
    status = models.CharField(blank=False, max_length=2, choices=STATUS, verbose_name='Status')
    pay_date = models.DateField(blank=False, null=True, verbose_name='data de pagamento')
    image = models.ImageField(blank=False, upload_to='core/static/images/supporters/', verbose_name='logo')
    notes = models.TextField(blank=True, verbose_name='anotações')


# Delete file from the given path
def _delete_file_(path):
    if os.path.isfile(path):
        os.remove(path)


# Backup image's current path for potential deletion or update
@receiver(models.signals.post_init, sender=Members)
@receiver(models.signals.post_init, sender=ImageContent)
@receiver(models.signals.post_init, sender=Supporters)
def backup_image_path(sender, instance, **kwargs):
    if instance.image:
        instance._current_image_file = instance.image.path


# Delete old file in case of updating an image
@receiver(models.signals.post_save, sender=Members)
@receiver(models.signals.post_save, sender=ImageContent)
@receiver(models.signals.post_save, sender=Supporters)
def delete_old_image(sender, instance, **kwargs):
    if not instance.image or (instance.image and hasattr(instance, '_current_image_file') and instance.image.path != instance._current_image_file):
        if hasattr(instance, '_current_image_file'):
            _delete_file_(instance._current_image_file)


# Delete file when an image is not needed anymore
@receiver(models.signals.post_delete, sender=Members)
@receiver(models.signals.post_delete, sender=ImageContent)
@receiver(models.signals.post_delete, sender=Supporters)
def delete_file(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_file_(instance.image.path)