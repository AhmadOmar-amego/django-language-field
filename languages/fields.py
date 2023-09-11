from django.db.models.fields import CharField


class LanguageField(CharField):
    """
    A language field for Django models.
    """

    def __init__(self, *args, **kwargs):
        # Local import so the languages aren't loaded unless they are needed.
        from .languages import LANGUAGES
        # fix max length
        # actual error bug
        # user_settings.CoreUserSettings.app_languages: (fields.E009) 'max_length' is
        # too small to fit the longest value in 'choices' (8 characters).

        kwargs.setdefault('max_length', 10)
        kwargs.setdefault('choices', LANGUAGES)
        kwargs.setdefault('db_collation', None)

        super().__init__(*args, **kwargs)
