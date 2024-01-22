from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path("portfolio/<slug:slug>", views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path("blog/<slug:slug>", views.BlogDetailView.as_view(), name='blog-detail'),
    path("message/", views.MessageView.as_view(), name='message')
]
