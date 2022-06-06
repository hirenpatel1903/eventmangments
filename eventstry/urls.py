from cgitb import handler
from django.contrib import admin
from django.urls import path
from eventstry import views
from django.conf.urls.static import static
from eventstry import settings
from app.web_views import auth_views, dashboard_views
from app.web_views.admin import lead_admin_views, vendor_admin_views
from app.web_views.vendor import lead_vendor_views
from app.api_views.admin import lead_views as lead_api_views
from app.api_views.admin import vendor_views
from app.api_views.vendor import lead_views as lead_vendor_api_views
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from django.urls import include, re_path

urlpatterns = [
    
    # ______________________ WEB URLS ______________________-
    path('clear_cache/', views.clear_cache),

    # _______________________ GENERAL ________________________
    path('admin/', admin.site.urls),
    path('', auth_views.login_user, name='users'),

    # # AUTH URLS
    path('login/', auth_views.login_user, name='login'),
    path('login/<token>/', auth_views.login_usercheck, name='login'),
    path('register/', auth_views.register, name='register'),
    path('logout/', auth_views.logout_user, name='logout'),
    path('forgotPassword/', auth_views.forgot_password, name='forgotPassword'),
    path('change_password/<token>/', auth_views.change_passwords, name='change_password'),
    path('contactDetails/', auth_views.contact_details, name='contactDetails'),
    path('checkEmail/', auth_views.check_email, name='checkEmail'),
    path('checkEmailUser/', auth_views.check_user_email, name='checkEmailUser'),
    path('checkMobilenumber/', auth_views.check_mobilenumber, name='checkMobilenumber'),
    path('checkMobilenumberUser/', auth_views.check_user_mobilenumber, name='checkMobilenumberUser'),

    path('changePassword/', auth_views.change_password, name='changePassword'),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('profile/', dashboard_views.profile, name='profile'),
    path('profile/<int:USER_ID>', dashboard_views.profile_store, name='profileStore'),
    path('media/delete/<int:MEDIA_ID>', dashboard_views.delete_media, name='mediaDelete'),

    # # ADMIN-VENDOR URLS 
    path('vendor/index/', vendor_admin_views.index, name='vendorIndex'),
    path('vendor/changeStatus/', vendor_admin_views.change_status, name='vendorchangeStatus'),
    path('vendor/view/<int:vendor_id>', vendor_admin_views.view, name='vendorView'),

    # # ADMIN-LEAD URLS
    path('lead/index/', lead_admin_views.index, name='leadIndex'),
    path('lead/create/', lead_admin_views.create, name='leadCreate'),
    path('lead/store/', lead_admin_views.store, name='leadStore'),
    path('lead/changeStatus/', lead_admin_views.change_status, name='leadchangeStatus'),
    path('lead/edit/<int:LEAD_ID>', lead_admin_views.edit, name='leadEdit'),
    path('lead/update/<int:LEAD_ID>', lead_admin_views.update, name='leadUpdate'),
    path('lead/delete/<int:LEAD_ID>', lead_admin_views.delete, name='leadDelete'),
    path('lead/view/<int:LEAD_ID>', lead_admin_views.view, name='leadView'),
    path('lead/assign/<int:LEAD_ID>', lead_admin_views.assign, name='leadAssign'),
    path('lead/assignstore/<int:LEAD_ID>', lead_admin_views.assign_store, name='leadAssignStore'),
    path('lead/assigndelete/<int:assign_id>', lead_admin_views.assign_delete, name='leadAssignDelete'),
    path('lead/commentlist/<int:ASSIGN_ID>/<int:LEAD_ID>', lead_admin_views.comment_list, name='leadCommentList'),

    # # VENDOR-LEAD URLS
    path('vendor/lead/index/', lead_vendor_views.index_lead_vendor, name='leadIndexVendor'),
    path('vendor/lead/view/<int:LEAD_ASSIGN_ID>', lead_vendor_views.view_lead_vendor, name='leadViewVendor'),
    path('vendor/lead/store/<int:LEAD_ASSIGN_ID>', lead_vendor_views.store_lead_vendor, name='leadStoreVendor'),

    # ______________________ API URLS ______________________-

    # # ADMIN-VENDOR URLS 
    path('api/vendor/data/', vendor_views.VendorDetail.data, name='vendorData'),

    # # ADMIN-LEAD URLS
    path('api/lead/data/', lead_api_views.data, name='leadData'),

    # # VENDOR-LEAD URLS
    path('api/vendor/lead/data/', lead_vendor_api_views.vendor_lead_data, name='vendorLeadData'),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATICFILES_DIRS[0]}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

]