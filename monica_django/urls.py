"""monicapuerto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls import url
from collection import views
# from . import views

urlpatterns = [
    # url(r'^$',views.index,name='home'),
    path('', views.index, name='home'),
    # the new url entries
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # kind of a hack... but we want to use the built-in contact js for this bootstrap template
    path('contact/contact-form', views.contact_form, name='contact-form'),

    path('homicides-in-dc/', TemplateView.as_view(template_name='post.html'), name='post1'),
    path('admin/', admin.site.urls),
]
