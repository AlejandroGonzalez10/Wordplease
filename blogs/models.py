from django.contrib.auth.models import User
from django.db import models


LICENSE_COPYRIGHT = 'RIG'
LICENSE_COPYLEFT = 'LEF'
LICENSE_CC = 'CC'

LICENSES = (
    (LICENSE_COPYRIGHT, 'Copyright'),
    (LICENSE_COPYLEFT, 'Copyleft'),
    (LICENSE_CC, 'Creative commons')
)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Pública'),
    (VISIBILITY_PRIVATE, 'Privada')
)


class Post(models.Model):
    owner = models.ForeignKey(User)
    titulo = models.CharField(max_length=150)
    texto = models.CharField(max_length=300)
    cuerpo = models.TextField(blank=True, null=True, default="")
    url = models.URLField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    hora = models.TimeField(auto_now_add=True)
    categorias = models.CharField(max_length=5, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    def __str__(self):
        return self.titulo
