import os

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
        'social.backends.facebook.FacebookOAuth2',

        'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY')

SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/main/"

SIGNUP_SUCCESS_MESSAGE = "성공적으로 회원가입 되었습니다"
LOGIN_SUCCESS_MESSAGE = "성공적으로 로그인 되었습니다"
LOGOUT_SUCCESS_MESSAGE = "성공적으로 로그아웃 되었습니다"
LOGIN_FAIL_MESSAGE = "로그인이 실패 되었습니다"

# solved conflict social_pipeline with pipeline
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',

)
