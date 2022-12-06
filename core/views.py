from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.views import View
from core.models import Manager, Post, Disciplina
from django.urls import reverse_lazy
from .utils import GeraPDFMixin


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['managers'] = Manager.objects.all()
        return context


class DisciplinaMixin():
    model = Disciplina
    fields = ['aluno', 'nome', 'nota']
    success_url = reverse_lazy('index')
    context_object_name = 'disciplina'


class DisciplinaEditarMixin(object):
    def form_valid(self, form):
        form.instance.dono = self.request.user
        return super().form_valid(form)


class DisciplinaListarView(DisciplinaMixin, ListView):
    template_name = 'disciplina/listar.html'


class DisciplinaCriarView(DisciplinaMixin, DisciplinaEditarMixin, CreateView):
    template_name = 'disciplina/form.html'


class DisciplinaExcluirView(DisciplinaMixin, DeleteView):
    template_name = 'disciplina/excluir.html'


class NotasPdfView(View, GeraPDFMixin):
    def get(self, request, *args, **kwargs):
        funcs = Disciplina.objects.all()
        for func in funcs:
            print(func.nome)
        contexto = {
            'disciplina': funcs,
            'request': request
        }
        return self.render_to_pdf('disciplina/notasalunopdf.html', contexto)
