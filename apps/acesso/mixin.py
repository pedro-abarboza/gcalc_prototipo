from django.contrib.auth.models import Permission, Group

class AcessoMixin:

    def get_list_permissions(self):
        """
        Returns a list of permissions for the user.
        """
        return list(Permission.objects.filter().exclude(content_type_id__in=[1,5,6]).values_list('id', 'codename'))