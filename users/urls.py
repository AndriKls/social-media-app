from django.urls import path
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='index'),
    path('logout/confirm/', views.LogOutConfirmView.as_view(), name='logout_confirm'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile-edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('profile/<str:username>', views.ProfileView.as_view(), name='profile'),
    path('gallery/upload/', views.GalleryUploadView.as_view(), name='gallery_upload'),
    
    # path('profile/delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
]
