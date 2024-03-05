from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', LoginView.as_view(template_name='login.html'), name='login'),
                  path('recipes/', views.recipe_list, name='recipe_list'),
                  path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
                  path('recipe/new/', views.recipe_new, name='recipe_new'),
                  path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
                  path('signup/', generic.CreateView.as_view(
                      template_name='signup.html',
                      form_class=UserCreationForm,
                      success_url=reverse_lazy('login')),
                       name='signup'),
                  path('login/', LoginView.as_view(
                      template_name='login.html',
                  ), name='login', ),
                  path('logout/', views.logout_view, name='logout'),
                  path('category/new/', views.category_new, name='category_new'),
                  path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
