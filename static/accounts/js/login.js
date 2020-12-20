var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder='Username..';

form_fields[2].placeholder='Enter password...';


for (var field in form_fields){
    form_fields[field].className += 'form-control'
}

