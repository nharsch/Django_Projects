from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class CSVImportForm(forms.Form):
    # File size limited to 2MB
    file = RestrictedFileField(
    #from .fields
        label='CSV File (Max Size 2MB)',
        content_types=['text/csv', 'application/csv'],
        max_upload_size=2097152,
    )

    def __init__(self, *args, **kwargs):
        super(CSVImportForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self. helper.layout = Layout(
            MultiField(
                None,
                Fieldset(
                    'Instructions',
                    HTML(
                        '''
                        To properly import your data, the CSV file must follow
                        this order and format: <br><br>
                        <ol>
                        <li>Value</li>
                        <li>Category (if no matching category in our system,
                        'No Category' will be assigned)</li>
                        <li>Date (in m/d/yyyy format, e.g. 5/6/2014 or
                        05/06/2014)</li>
                        <li> Time (in h:m am/pm format, e.g. 8:01 AM or
                        08:01 PM)</li>
                        <li>Notes</li>
                        </ol>
                        <p>You can also download this template as a guide:
                        <a href="{{ STATIC_URL }}samples/csv_import_template.csv">
                        csv_import_template.csv</a></p>
                        <br>
                        '''
                    ),
                ),
                HTML(
                    '''
                    {% if messages %}
                    {% for message in messages %}
                    <p {% if message.tags %}
                    class="alert alert-{{ message.tags }}"
                    {% endif %}>{{ message }}</p>{% endfor %}{% endif %}
                    '''
                ),
                Div(
                    'file',
                    FormActions(
                        Submit('submit', 'Import'),
                        css_class='pull-right',
                    ),
                    css_class='well col-xs-10 col-sm-8 col-md-8',
                ),
            ),
        )