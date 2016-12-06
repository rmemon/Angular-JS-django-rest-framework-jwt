from django.contrib import admin

# Register your models here.
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['title','charge_perhour','charge_perday','charge_perweek']
    change_form_template = "admin/product/productadd.html"
    # actions = [delete_selected, ]
    # list_filter = ["email_id"]
    list_display_links = None


    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        qs = qs.filter(is_deleted="n")
        if request.user.is_superuser:
            return qs
        return qs.filter(i_by=request.user.id)

    def get_urls(self):
        urls = super(ProductAdmin, self).get_urls()
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



    def add_view(self, request):
        # form = ProductForm()
        # context = {
        #     'form': form,
        # }
        if request.POST:
            # form = ProductForm(request.POST)
            instance2 = Product()
            instance2.title = request.POST.get('title')
            instance2.model = request.POST.get('model')
            instance2.category_id = request.POST.get('category_id')
            instance2.ownername = request.POST.get('ownername')
            current_user = request.user
            instance2.user_id = request.user.id
            instance2.charge_perhour = request.POST.get('charge_perhour')
            instance2.charge_perday = request.POST.get('charge_perday')
            instance2.charge_perweek = request.POST.get('charge_perweek')
            instance2.is_deleted = 'y'
            instance2.is_active = 'y'
            instance2.i_by = request.user.id
            instance2.u_by = request.user.id




            # context = {
            #     'form': form,
            # }
            if request.POST.get('cont'):
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return redirect('/admin/product/product/')
        return render(request, 'admin/product/productadd.html')



admin.site.register(Product, ProductAdmin)