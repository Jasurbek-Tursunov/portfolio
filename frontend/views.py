from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from frontend.forms import MessagesForm
from frontend.models import Info, Client, Resume, Social, Skill, Message, ResumeCategory, Category, Project, Blog


class HomeView(View):
    def get(self, request, **kwargs):
        info = Info.get_solo()
        socials = Social.objects.all()
        skills = Skill.objects.all()
        testimonials = Message.objects.filter(is_checked=True)
        clients = Client.objects.all()
        resume_categories = ResumeCategory.objects.all()
        resume = Resume.objects.all()
        categories = Category.objects.all()
        projects = Project.objects.all()
        blogs = Blog.objects.all()
        return render(
            request,
            "index.html",
            {
                "info": info,
                "socials": socials,
                "skills": skills,
                "testimonials": testimonials,
                "clients": clients,
                "resume_categories": resume_categories,
                "resume": resume,
                "categories": categories,
                "projects": projects,
                "blogs": blogs
            }
        )


class ReceiveProjectView(View):
    def get(self, request, slug, **kwargs):
        try:
            info = Info.get_solo()
            socials = Social.objects.all()
            project = Project.objects.get(slug=slug)
            return render(
                request,
                "project.html",
                {
                    "info": info,
                    "socials": socials,
                    "project": project,
                }
            )

        except Project.DoesNotExist:
            raise Http404


class ReceiveBlogView(View):
    def get(self, request, slug, **kwargs):
        try:
            info = Info.get_solo()
            socials = Social.objects.all()
            blog = Blog.objects.get(slug=slug)
            return render(
                request,
                "blog.html",
                {
                    "info": info,
                    "socials": socials,
                    "blog": blog,
                }
            )

        except Blog.DoesNotExist:
            raise Http404


class ReceiveMessage(View):
    """ Receive message from Clients"""

    def post(self, request):
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
        messages.info(request, 'Successfully Sent The Message!')
        return redirect("/")
