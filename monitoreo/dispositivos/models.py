from django.db import models

# Create your models here.

# MODELO BASE

class BaseModel(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

# Tablas Principales

class Zona(BaseModel):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(BaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Dispositivo(BaseModel):
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