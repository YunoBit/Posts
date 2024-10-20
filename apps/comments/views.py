from django.views import generic
from django.urls import reverse_lazy

from apps.comments.models import Comments
from apps.comments.forms import CommentForm


class CommentCreateView(generic.CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'comments/com_create.html'
    success_url = reverse_lazy('detail')

class CommentUpdateView(generic.UpdateView):
    model = Comments
    form_class = CommentForm
    template_name = 'comments/com_update.html'
    success_url = reverse_lazy('detail')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs = {'pk': self.object.pk})
    
class CommentDeleteView(generic.DeleteView):
    model = Comments
    template_name = 'comments/com_delete.html'
    success_url = reverse_lazy('detail')