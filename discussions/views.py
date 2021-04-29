from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Discussion, Reply
from .forms import ReplyForm
from django.contrib.auth.decorators import login_required


# Create your views here.


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    model = Discussion
    fields = ["title", "body"]
    template_name = "discussions_form.html"
    success_url = reverse_lazy("discussions_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(DiscussionCreateView, self).form_valid(form)


class DiscussionListView(LoginRequiredMixin, ListView):
    model = Discussion
    template_name = "discussions_list.html"


@login_required
def discussions_detail(request, pk):
    template_name = "discussions_detail.html"
    discussion = get_object_or_404(Discussion, pk=pk)
    replies = discussion.replies.all()
    new_reply = None
    # Comment posted
    if request.method == "POST":
        reply_form = ReplyForm(data=request.POST)
        if reply_form.is_valid():

            # Create Comment object but don't save to database yet
            new_reply = reply_form.save(commit=False)
            # Assign the current post to the comment
            new_reply.parent = discussion
            new_reply.created_by = request.user
            # Save the comment to the database
            new_reply.save()

            return HttpResponseRedirect(str(discussion.id))

    else:
        reply_form = ReplyForm()

    return render(
        request,
        template_name,
        {
            "discussion": discussion,
            "replies": replies,
            "new_reply": new_reply,
            "reply_form": reply_form,
        },
    )
