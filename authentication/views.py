from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import SiginUpForm, LoginForm
from django.contrib.auth import authenticate, login, get_user_model

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = SiginUpForm

    def get(self, request):
        context = {'form':SiginUpForm}
        context['title']='Registre-se'
        return render(request, self.template_name,context)
    
    def post(self, request):
        form = SiginUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if get_user_model().objects.filter(username=username).exists():
                context = {}
                context['form'] = self.form_class
                context['error'] = self.form_class.errors
                context['title']='Registre-se'
                return render(request, 'accounts/register.html',context)
            
            else:
                form.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)

                if user is not None:
                    login(request,user)
                    #criar view
                    return redirect('login')
                else:
                    #criar view
                    return redirect('login')
                
        else:
            context = {}
            context['form'] = self.form_class
            context['error'] = form.errors
            context['title']='Registre-se'
            return render(request, self.template_name, context)


class LoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get(self, request):
        context = {'form':self.form_class}
        context['title']='Login'

        return render(request, self.template_name, context)