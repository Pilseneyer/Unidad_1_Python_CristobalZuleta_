from django.db import models

# Create your models here.

class Zona(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Alerta(models.Model):
    fecha_hora=models.DateTimeField(auto_now=True)
    notificacion=models.TextField(blank=False, null=False)
    dispositivo=models.ForeignKey(Dispositivo,on_delete=models.CASCADE)
    
    def __str__(self):
        return super().__str__()

class Medicion(models.Model):
    fecha_hora=models.DateTimeField(auto_now=True)
    consumo=models.IntegerField()
    dispositivo=models.ForeignKey(Dispositivo,on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()