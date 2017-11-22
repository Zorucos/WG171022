import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
	edit_entries = tables.TemplateColumn('<a href="{% url \'person_detail\' record.id %}">Edit</a>')

	class Meta:
		model = Person
		template = 'django_tables2/bootstrap.html'
		fields = [
            'name',
            'name_short',
            'company',
            'company_short',
        ]
