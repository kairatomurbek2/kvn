from django.contrib import admin

from social.models import Post, Team, Events, RequestTeam, Crown, PostComment

admin.site.register(Post)
admin.site.register(Team)
admin.site.register(Events)
admin.site.register(RequestTeam)
admin.site.register(Crown)
admin.site.register(PostComment)
