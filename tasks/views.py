from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from tasks.models import TaskModel, ComplTaskModel
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from django.template.context import Context
from django.template.loader import get_template
import json

# Create your views here.


def start(request):
    # code to replace LOGIN_REDIRECT_URL in settings.py
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('week_plan'))
    else:
        return render(request, 'start.html', {})


def tasks_list(request):
    tasks = TaskModel.objects.all()
    c_tasks = ComplTaskModel.objects.all()

    for c_task in c_tasks:
        for task in tasks:
            if task.checkbox == True:
                # the line below added to not replace existing objects
                c_task = ComplTaskModel(c_task_content='', c_check_list=False)
                #
                c_task.c_task_content = task.task_content
                task.delete()
                c_task.save()
                return HttpResponse(1)
            if c_task.c_check_list == True:
                # the line below added to not replace existing objects
                task = TaskModel(task_content='', checkbox=False)
                #
                task.task_content = c_task.c_task_content
                c_task.delete()
                task.save()
                return HttpResponse(1)

    if request.is_ajax():
        data = request.POST
        present = data['present'] and True or False
        task = TaskModel.objects.get(pk=data['pk'])
        if present == True:
            task.checkbox = True
            task.save()
            return HttpResponse(1)
    else:
        if tasks == False:
            return render(request, 'week_plan.html', {'c_tasks': c_tasks})
        else:
            return render(request, 'week_plan.html', {'tasks': tasks, 'c_tasks': c_tasks})


@login_required
def task_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # TODO: validate input from user
            errors = {}
            if not errors:
                # create task object
                task= TaskModel(
                    task_content=request.POST['task_content'],
                )
                # save it to database
                task.save()
                # redirect user to tasks list
                return HttpResponseRedirect(reverse('week_plan'))
            else:
                # render form with errors and previous user input
                return render(request, 'add_task.html',
                  {'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to week_plan page on cancel button
            return HttpResponseRedirect(reverse('week_plan'))
    else:
        # initial form render
        return render(request, 'add_task.html', {})


class TaskUpdateForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('edit_task', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
        Submit('add_button', 'Save', css_class="btn btn-primary"),
        Submit('cancel_button', 'Cancel', css_class="btn btn-link"),
        )


class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = 'edit_task.html'
    form_class = TaskUpdateForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('week_plan')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect('%s?status_message=Canceled!' % reverse('week_plan'))
        else:
            return super(TaskUpdateView, self).post(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'delete_task.html'
    fields = '__all__'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('week_plan')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect('%s?status_message=Canceled!' % reverse('week_plan'))
        else:
            return super(TaskDeleteView, self).post(request, *args, **kwargs)



