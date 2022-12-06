from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import User


class Base(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    modifiy_at = models.DateTimeField(auto_now=True)
    active_at = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Manager(Base):
    name = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    bio = models.TextField('Texto', max_length=1000)
    photo = StdImageField('Photo',
                          upload_to='manager',
                          variations={'thumbnail': {'width': 600,
                                                    'height': 600,
                                                    'crop': True}})
    facebook = models.CharField('Face', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    instagram = models.CharField('Insta', max_length=100)

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"

    def __str__(self):
        return self.name


class Post(Base):
    title = models.CharField('Título', max_length=100)
    text = models.TextField('Texto', max_length=1000)
    image = StdImageField('Imagem',
                          upload_to='post',
                          variations={'thumbnail': {'width': 600,
                                                    'height': 600,
                                                    'crop': True}})
    author = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Disciplina(Base):
    DISC_CHOICES = (
        ('Matemática', 'Matemática'),
        ('Português', 'Português'),
        ('Biologia', 'Biologia'),
        ('Física', 'Física'),
    )
    aluno = models.ManyToManyField(User)
    nome = models.CharField('Nome', max_length=100, choices=DISC_CHOICES)
    nota = models.CharField('Nota', max_length=100)

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return f'{self.aluno.all}'