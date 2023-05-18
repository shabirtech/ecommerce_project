from django.contrib import admin

# Register your models here.

from conversation.models import Conversation, ConversationMessage


admin.site.register(ConversationMessage)
admin.site.register(Conversation)
