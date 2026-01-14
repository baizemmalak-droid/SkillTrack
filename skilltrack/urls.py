urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),   # ⬅️ الأول
    path('', include('students.urls')),   # ⬅️ الثاني
]