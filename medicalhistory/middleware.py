from django.utils import translation


class TranslationMiddleware(object):

    def process_request(self, request):
        language = 'ky'
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
