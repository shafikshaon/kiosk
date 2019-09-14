__author__ = 'Shafikur Rahman'

from django.contrib.auth.models import Permission


class RolePermission(Permission):
    class Meta:
        proxy = True
        ordering = ('content_type__app_label', 'content_type__model',
                    'codename')

    def __str__(self):
        return "%s | %s" % (
            self.convert_to_sentence_case(self.content_type),
            self.convert_to_sentence_case(self.codename)
        )

    @staticmethod
    def convert_to_sentence_case(x):
        return x and str(x)[0].upper() + str(x)[1:].replace('_', ' ')

    def natural_key(self):
        return (self.codename,) + self.content_type.natural_key()

    natural_key.dependencies = ['contenttypes.contenttype']
