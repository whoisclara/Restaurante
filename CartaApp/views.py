from django.shortcuts import render, HttpResponse 

# Create your views here.

def home (request):
    return render(request, 'home.html')

def carta(request):
    
    productos = [
        {
            "id": 1,
            "nombre": "Hamburguesa",
            "imagen":"https://www.portafolio.co/files/article_new_multimedia/uploads/2022/04/12/6255e2e41db6c.jpeg",
            "descripcion": "Ven y prueba la variedad de burgers, desde mix de queso hasta triple carnes.",
            "ref":"Ver hamburgesas",
            "precio": 38000,
        },
        {
            "id": 2,
            "nombre": "Pizza",
            "imagen": "https://pbs.twimg.com/media/Bi8peAACcAAzyRs.jpg",
            "descripcion":"Para los amantes del queso, la triple queso es la pizza ideal para ti.",
            "ref":"Ver Pizzas",
            "precio": 35000,
        },
        {
            "id": 3,
            "nombre": "Pastas",
            "imagen":"https://cloudfront-us-east-1.images.arcpublishing.com/elespectador/RCDPFEWWPRCGVLHJEA3ZK2HA3Y.jpg ",
            "descripcion": "Pastas en diferentes salsas (napolitana,alfredo), diferentes estilos con un toque secreto",
            "ref":"Ver Pastas",
            "precio": 34500,
        },
        {
            "id": 4,
            "nombre": "Carnes",
            "imagen":"https://images.pexels.com/photos/27643038/pexels-photo-27643038/free-photo-of-comida-cena-almuerzo-chef.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
            "descripcion": "Tenemos diferentes cortes, baby beef, solomito, punta de anca. Acompañada de la guarnición que elijas",
            "ref":"Ver carnes",
            "precio": 40000,
        }
    ]
    return render(request, 'carta.html', {"productos": productos})

def ubicaciones(request):
    return render(request, 'ubicaciones.html')

def reservas(request):
    return render(request, 'reservas.html')

def sedes(request):
    return render(request, 'sedes.html')
