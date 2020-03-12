from django.conf import settings

def send_settings(request):
	analytics_id = settings.ANALYTICS_ID
	return { 'analytics_id': analytics_id }