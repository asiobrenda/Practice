
var pages = {};
var data_path = document.getElementById('defaultOpen').getAttribute('data_path');
var csrfToken = document.getElementById('csrfToken').getAttribute('data-csrf');
function OpenSource(evt, source) {

   evt.preventDefault();
    //alert(source);

    var page = pages[source];
    if (!page) {
        $.ajax({

            type: 'POST',
            url: data_path,
            headers: {
                'X-CSRFToken': csrfToken
            },
            data: {
                source: source,
                csrfmiddlewaretoken: csrfToken // Add CSRF token to the data sent
            },
            success: function(data) {
                var elm = document.getElementById(source);
                if (elm) {
                    elm.innerHTML = data;
                    pages[source] = 1;
                    //alert(elm.innerHTML);
                }
            },
            error: function(xhr, errmsg, err) {
                // Handle error
            }
        });
    }

  var i, tabcontent_, tablinks_;
  tabcontent_ = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent_.length; i++) {
    tabcontent_[i].style.display = "none";
  }
  tablinks_ = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks_.length; i++) {
    tablinks_[i].className = tablinks_[i].className.replace(" active", "");
  }
  document.getElementById(source).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();