from django.shortcuts import render, HttpResponse

def registro(request):
    return HttpResponse("""
        <h2>Portada registro asesores</h2>
        <p>Esto es para registro de asesores.</p>
    """)

