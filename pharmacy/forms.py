from django.forms import ModelForm, DateInput, modelformset_factory

from pharmacy.models import AppointmentList, StockTacking, AcceptanceList


class DateInputType(DateInput):
    input_type = 'date'


class SheetAssignmentForm(ModelForm):
    class Meta:
        model = AppointmentList
        exclude = ('patient','doctor','beginAppointment')
        widgets = {
            'beginAppointment': DateInputType(),
            'endAppointment': DateInputType(),

        }

EditStockTackingFormset = modelformset_factory(StockTacking, exclude=('date',), extra=0)


class UseDrugForPatientForm(ModelForm):
    class Meta:
        model = AcceptanceList
        exclude = ('appointmentList','acceptDate')
        # fields = '__all__'
