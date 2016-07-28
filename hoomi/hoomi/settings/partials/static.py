# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

import os

from .base import BASE_DIR, PROJECT_ROOT_DIR

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "hoomi", "static"),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "images")

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'vendor': {
            'source_filenames': (
                # bootstarp
                'css/bootstrap.min.css',
                'css/bootstrap-social.css',
                'css/portfolio.jquery.css',
                'css/overlay-bootstrap.min.css',

            ),
            'output_filename': 'css/vendor.css',
        },
        'vendor-font-images': {
            'source_filenames': (
                # font-awesome
                'css/font-awesome.min.css',
            ),
            'output_filename': 'css/vendor-font.css',
            'variant': 'datauri',
        },
        'hoomi': {
            'source_filenames': (
                'css/application.css',
                'css/hoomi.css',
            ),
            'output_filename': 'css/hoomi.css',
        },
        'resume': {
            'source_filenames': (
                'css/style.css',
            ),
            'output_filename': 'css/resume.css'
        }
    },
    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
                'js/jquery-ui.min.js',
                'js/jquery.bootstrap-growl.min.js',
                'js/jquery.cookie.js',
                'js/list.pagination.min.js',
                'js/bootstrap.min.js',
                'js/jquery.validate.min.js',
                'js/additional-methods.min.js',
                'js/messages_ko.min.js',
                'js/jquery.form.js',
            ),
            'output_filename': 'js/vendor.js',
        },
        'hoomi': {
            'source_filenames': (
                'js/application.js',
            ),
            'output_filename': 'js/hoomi.js',
        },
        'skill-select': {
            'source_filenames': (
                'js/jobs/select.js',
            ),
            'output_filename': 'js/jobs/select.js',
        },
        'resume': {
            'source_filenames': (
                'js/jobs/resume.js',
            ),
            'output_filename': 'js/resume.js',
        }
    },
}
