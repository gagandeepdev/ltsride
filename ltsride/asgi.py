"""
ASGI config for ltsride project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import AsgiHandler
import inbox.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ltsride.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        "websocket": AuthMiddlewareStack(
            URLRouter(inbox.routing.websocket_urlpatterns)
        ),
        # Just HTTP for now. (We can add other protocols later.)
    }
)
