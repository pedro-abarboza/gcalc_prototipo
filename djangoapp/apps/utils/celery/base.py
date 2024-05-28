from datetime import datetime

from core.celery import app


class CeleryTaskMixin(object):

    progressbar_template_name = 'base/celery_progress.html'

    @property
    def get_celery_worker_status(self):
        """
        Get status celery task
        """
        i = app.control.inspect()
        return i.stats()

    @property
    def set_task_params(self):
        """
        This method captures the context_data of the view,
        get celery status and sends it to the celery template,
        as it needs to set the screen title, menu and breadcrumbs.
        """
        context = self.get_context_data()
        context['stats'] = self.get_celery_worker_status

        context['task_id'] = self.task_result.task_id
        context['task_datetime'] = datetime.now()
        return context
