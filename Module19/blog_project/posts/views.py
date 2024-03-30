from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms 
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib import messages

# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
          post_form = forms.PostForm(request.POST)
          if post_form.is_valid():
            #   post_form.cleaned_data['author'] = request.user
              post_form.instance.author = request.user
              post_form.save()
              return redirect('add_post')
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form':post_form})

#Add post using class base view
@method_decorator(login_required,name='dispatch')
class AddPostCreateview(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,"Post created successfully")
        return super().form_valid(form)
        
@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    
    # print(post.title)
    if request.method == 'POST':
          post_form = forms.PostForm(request.POST,instance=post)
          if post_form.is_valid():
              post_form.instance.author = request.user
              post_form.save()
              return redirect('homepage')
        
    return render(request, 'add_post.html',{'form':post_form})

@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('profile')
    
@login_required
def delete_post(request,id):
     post = models.Post.objects.get(pk=id)
     post.delete()
     return redirect('homepage')
 
@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('profile')
    
    
class DetailPostView(DetailView):
    model = models.Post 
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comments_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comments_form.is_valid():
                new_comments= comments_form.save(commit=False)
                new_comments.post = post 
                new_comments.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        
        comments_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comments_form'] = comments_form
        return context