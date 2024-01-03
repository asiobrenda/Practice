function send_message(evt){
        var name_ = document.getElementById('name').value;
        var email_ = document.getElementById('email').value;
        var subject_ = document.getElementById('subject').value;
        var message_ = document.getElementById('textarea').value;
        var contactUrl = document.getElementById('sendmessage1').getAttribute('data-contact-url');

        $.post(contactUrl,
          {
             'name': name_,
             'email': email_,
             'subject': subject_,
             'message': message_,
          },
          function(data){
           alert(data[response_data])
          }
        )
}

 var csrftoken = Cookies.get('csrftoken');
            function csrfSafeMethod(method) {
              // these HTTP methods do not require CSRF protection
              return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            $.ajaxSetup({
              beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
              }
            });

  $(document).ready(function () {

  });

