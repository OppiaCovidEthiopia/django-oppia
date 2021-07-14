from django.urls import path
from reports import views

app_name = 'reports'

urlpatterns = [
    path('',
         views.HomeView.as_view(),
         name="index"),
    path('user-registrations',
         views.UserRegistrationsView.as_view(),
         name="user_registrations"),
    path('course-downloads',
         views.CourseDownloadsView.as_view(),
         name="course_downloads"),
    path('course-activity',
         views.CourseActivityView.as_view(),
         name="course_activity"),
    path('completion-rates',
         views.CompletionRatesView.as_view(),
         name="completion_rates"),
    path('completion-rates/<int:course_id>',
         views.CourseCompletionRatesView.as_view(),
         name="course_completion_rates"),
    path('unique-users',
         views.UniqueUsersView.as_view(),
         name="unique_users"),
    path('daily-active-users',
         views.DailyActiveUsersView.as_view(),
         name="daus"),
    path('monthly-active-users',
         views.MonthlyActiveUsersView.as_view(),
         name="maus"),
    path('total-time-spent',
         views.TotalTimeSpentView.as_view(),
         name="totaltimespent"),
    path('average-time-spent',
         views.AverageTimeSpentView.as_view(),
         name="averagetimespent"),
    path('searches',
         views.SearchesView.as_view(),
         name="searches"),
    path('search-terms',
         views.SearchTermView.as_view(),
         name="search_terms"),
    path('lang-activity',
         views.LanguageActivityView.as_view(),
         name="lang_activity"),
    path('countries',
         views.CountriesView.as_view(),
         name="countries"),
    path('user-course-time-spent',
         views.DownloadTimeSpentView.as_view(),
         name="user-course-time-spent"),
    path('map/', views.MapView.as_view(), name="map"),
    path('inactive-users',
         views.InactiveUsersView.as_view(),
         name="inactive_users"),
]
