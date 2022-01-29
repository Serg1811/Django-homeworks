from django.urls import path

from measurement.views import SensorView, SensorIdView, MeasurementsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorIdView.as_view()),
    path('measurements/', MeasurementsView.as_view()),

]
