from django.db import models
from solo.models import SingletonModel


class Configuration(SingletonModel):
    token = models.CharField(verbose_name="Bot Token", max_length=46)
    chat_id = models.CharField(verbose_name="Chat ID", max_length=15)

    def __str__(self):
        return self.chat_id

    class Meta:
        verbose_name = "Configuration"


class Info(SingletonModel):
    site_title = models.CharField(verbose_name='Site Title', max_length=200)
    avatar = models.ImageField(verbose_name='Avatar', upload_to=f'./avatars')
    full_name = models.CharField(verbose_name='Full name', max_length=50)
    professional = models.CharField(verbose_name='Professional', max_length=50)
    email = models.EmailField(verbose_name='E-mail', max_length=50)
    phone = models.CharField(verbose_name='Phone', max_length=20)
    birthday = models.DateField(verbose_name='Birthday')
    location = models.CharField(verbose_name='Location', max_length=200)
    location_url = models.URLField(verbose_name='Location URL')
    about = models.TextField(verbose_name='About Me')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Info'


class Social(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'


class Skill(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    icon = models.FileField(verbose_name='Icon', upload_to="./icons")
    short_text = models.CharField(verbose_name='Short Text', max_length=200)
    percent = models.PositiveSmallIntegerField(verbose_name='Percent')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Client(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    url = models.URLField(verbose_name='URL')
    logo = models.ImageField(verbose_name='Logo', upload_to=f'./logos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class ResumeCategory(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)

    def __str__(self):
        return self.title


class Resume(models.Model):
    category = models.ForeignKey(verbose_name='Category', to=ResumeCategory, on_delete=models.CASCADE)
    short_text = models.CharField(verbose_name='Short Text', max_length=200)
    period = models.CharField(verbose_name='Time Period', max_length=20)
    description = models.TextField(verbose_name='Description')
    order = models.PositiveSmallIntegerField(verbose_name='Order', unique=True)

    def __str__(self):
        return f'{self.period}'

    class Meta:
        ordering = ["order"]
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Project(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    category = models.ForeignKey(verbose_name='Category', to='Category', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Image', upload_to='./images')
    slug = models.SlugField(verbose_name='Alias', unique=True)
    short_text = models.CharField(verbose_name='Short Text', max_length=200)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Blog(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    category = models.ForeignKey(verbose_name='Category', to='Category', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Image', upload_to='./images')
    slug = models.SlugField(verbose_name='Alias', unique=True)
    short_text = models.CharField(verbose_name='Short Text', max_length=200)
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Message(models.Model):
    avatar = models.ImageField(verbose_name='Avatar', upload_to='./avatars', null=True, blank=True)
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Text')
    created_at = models.DateTimeField(verbose_name="Time of create", auto_now_add=True)
    is_checked = models.BooleanField(verbose_name='Is Checked?', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
