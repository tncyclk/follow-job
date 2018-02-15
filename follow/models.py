from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



# Create your models here.

TRACKER = (
    ('BUG', 'bug'),
    ('FEATURE', 'feature'),
    ('TEST', 'test'),
    ('RESEARCH', 'research'),
    ('SUPPORT', 'support'),
)
STATUS = (
    ('NEW', 'new'),
    ('IN PROGRES', 'in progres'),
    ('TESTING', 'testing'),
    ('RESOLVED', 'resolved')


)

class Project(models.Model):
    project_name = models.CharField(max_length=50, verbose_name="Proje Adı")
    members = models.ManyToManyField(User, null=True, verbose_name="Üyeler", default=None)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.project_name

    def users(self):
        return ",".join([str(p) for p in self.members.all()])

    def get_unique_slug(self):
        slug = slugify(self.project_name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Project.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('follow:detail', kwargs={'slug': self.slug})



class Job(models.Model):
    project_name = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=120, verbose_name="Konu")
    tracker = models.CharField(max_length=50, verbose_name="İşin Tipi", choices=TRACKER, default='bug')
    description = models.TextField(verbose_name="Yorum", blank=True)
    status = models.CharField(max_length=50, verbose_name="Durum", choices=STATUS, default='new')
    assigned_to = models.ManyToManyField(User, null=True, verbose_name="Atanan", default=None)
    start_date = models.DateField(blank=True, null=True, verbose_name="Başlangıç Tarihi")
    end_date = models.DateField(blank=True, null=True, verbose_name="Bitiş Tarihi")
    result = models.TextField(verbose_name="Sonuç", blank=True)
    file = models.FileField(blank=True, verbose_name='Dosya Ekle')
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.subject

    def assigned(self):
        return ",".join([str(p) for p in self.assigned_to.all()])

    def get_absolute_url(self):
        return reverse('follow:detail', kwargs={'slug': self.slug})
        # print("id---->> "+str(self.id))
        #  return "follow/{}".format(slug=self.slug)

    def get_unique_slug(self):
        slug = slugify(self.subject.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Job.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Job, self).save(*args, **kwargs)




    # def get_create_url(self):
    #     #return reverse('post:create', kwargs={'slug': self.slug})
    #     return "/follow/create"
    #
    # def get_update_url(self):
    #     #return reverse('post:update', kwargs={'slug': self.slug})
    #     return "/follow/{}/update".format(self.slug)
    #
    # def get_delete_url(self):
    #     #return reverse('post:delete', kwargs={'slug': self.slug})
    #     return "/follow/{}/delete".format(self.slug)

    class Meta:
        ordering = ['-start_date', 'id']
