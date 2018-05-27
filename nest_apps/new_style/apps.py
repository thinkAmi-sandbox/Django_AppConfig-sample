from django.apps import AppConfig


class NewStyleConfig(AppConfig):
    # if set `name='new_style'`, raise exception.
    # --------------------------------------------
    # django.core.exceptions.ImproperlyConfigured: 
    # Cannot import 'new_style'. 
    # Check that 'nest_apps.new_style.apps.NewStyleConfig.name' is correct.

    # incorrect
    # name = 'new_style'

    # correct
    name = 'nest_apps.new_style'
