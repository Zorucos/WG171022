import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):#name
	name = tables.TemplateColumn('<a href="{% url \'person_detail\' record.id %}"></a>')

	class Meta:
		model = Person
		template = 'django_tables2/bootstrap.html'
		fields = [
            'name',
            'name_short',
            'company',
            'company_short',
        ]
