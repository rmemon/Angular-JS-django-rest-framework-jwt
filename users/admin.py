from django.contrib import admin

from users.models import User



class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['profile_name', 'username',]
    # actions = [delete_selected, ]
    # list_filter = ["email_id"]
    list_display_links = None
    search_fields = ["profile_name", ]


    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        qs = qs.filter(is_deleted=0)
        if request.user.is_superuser:
            return qs
        return qs.filter(i_by=request.user.id)

    def get_urls(self):
        urls = super(UserAdmin, self).get_urls()
            #  my_urls = [
            #      # url(r'^view/(?P<user_id>[0-9]+)/$', self.viewuser, name="view"),
            # #            url(r'^change_password/(?P<user_id>[0-9]+)/$', self.change_password, name="change_password"),
            # #            url(r'^usercheck/$', self.usercheck, name="usercheck"),
            # #            url(r'^userstatus/$', self.userstatus, name="userstatus"),
            # #            url(r'^email_me/$', self.email_me, name="email_me"),
            # #            url(r'^email_all/$', self.email_all, name="email_all"),
            # #            url(r'^notify_all/$', self.notify_all, name="notify_all"),
            # #            url(r'^notify_me/$', self.notify_me, name="notify_me"),
            # #            url(r'^emailcheck/$', self.emailcheck, name="emailcheck"),
            # #            url(r'^emailcheck_admin/$', self.emailcheck_admin, name="emailcheck_admin"),
            # #            url(r'^contactcheck/$', self.contactcheck, name="contactcheck"),
            # #            url(r'^group_name_check/$', self.group_name_check, name="group_name_check"),
            # #            url(r'^verify_ssn/$', self.verify_ssn, name="verify_ssn"),
            # #            url(r'^verify_ein/$', self.verify_ein, name="verify_ein"),
            #
            #            ]

        return urls



admin.site.register(User, UserAdmin)