from datetime import date
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse, reverse_lazy
from .forms import CustomUserCreationForm, ProfileEditForm, UserEditForm, ProfileEditForm, MultiPhotoUploadForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Gallery, Profile
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model







class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'users/index.html'

class LogOutConfirmView(TemplateView):
    template_name = 'registration/logout_confirm.html'


CustomUser = get_user_model()  # Dünaamiline kasutajamudeli tuvastamine

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')  # Võtab kasutajanime URL-ist
        try:
            user = CustomUser.objects.get(username=username)  # Otsib kasutaja kasutajanime järgi
            return user.profile  # Tagastab seotud profiili
        except CustomUser.DoesNotExist:
            raise Http404("Kasutajat ei leitud")
        except Profile.DoesNotExist:
            raise Http404("Profiili ei leitud")
    
    def calculate_age(self):
        if self.user.date_of_birth:
            today = date.today()
            born = self.user.date_of_birth
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            return age
        return None


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_edit.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile  # Assumes `Profile` is linked to `CustomUser` via OneToOneField
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('profile', kwargs={'username': user.username}))

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })
    


class GalleryUploadView(LoginRequiredMixin, FormView):
    template_name = 'users/gallery_upload.html'
    form_class = MultiPhotoUploadForm

    def form_valid(self, form):
        profile = self.request.user.profile
        images = self.request.FILES.getlist('images')  # Mitme faili käsitlemine
        for image in images:
            Gallery.objects.create(profile=profile, image=image)
        return redirect(reverse('profile', kwargs={'username': self.request.user.username}))