from datetime import date

from django import forms
from siteinfo.models import RestaurantProfile
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_name', 'table', 'date', 'time_slot', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()}),
            'time_slot': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'booking_name': 'Name',
        }

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        guests = cleaned_data.get('guests')
        time_slot = cleaned_data.get('time_slot')
        booking_date = cleaned_data.get('date')

        if table and guests and guests > table.capacity:
            self.add_error('guests', f"Table {table.table_number} seats a maximum of {table.capacity} guests.")

        if booking_date and booking_date < date.today():
            self.add_error('date', "You can't book a table for a past date.")

        if time_slot:
            profile = RestaurantProfile.objects.first()
            if profile and profile.opening_time and profile.closing_time:
                if not (profile.opening_time <= time_slot <= profile.closing_time):
                    self.add_error(
                        'time_slot',
                        f"Bookings are only available between {profile.opening_time.strftime('%I:%M %p')} and {profile.closing_time.strftime('%I:%M %p')}."
                    )

        return cleaned_data