from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from blogs.forms import PostForm
from blogs.models import Post


class HomeView(View):

    def get(self, request):
        """
        Renderiza el home con un listado de fotos
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # recupera todas las fotos de la base de datos
        posts = Post.objects.all().order_by('-created_at')
        context = {'posts_list': posts[:4]}
        return render(request, 'blogs/index.html', context)


class PostCreationView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear una foto
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        post_form = PostForm()
        context = {'form': post_form, 'message': message}
        return render(request, 'photos/photo_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear una foto y, en caso de que la petición sea POST la valida
        y la crea en caso de que sea válida
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        post_with_user = Post(owner=request.user)
        post_form = PostForm(request.POST, instance=post_with_user)
        if post_form.is_valid():
            new_post = post_form.save()
            post_form = PostForm()
            message = 'Foto creada satisfactoriamente. <a href="{0}">Ver foto</a>'.format(
                reverse('photos_detail', args=[new_post.pk])
            )

        context = {'form': post_form, 'message': message}
        return render(request, 'photos/photo_creation.html', context)
