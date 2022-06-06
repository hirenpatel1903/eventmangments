$(document).ready(function() {

    // var site_url = "{% url %}";

    jQuery.validator.addMethod("validphone", function(value, element) {
        return this.optional(element) || /^(?=.*[0-9])[- +()0-9]+$/.test(value);
    }, "Please enter valid phone number.");

    $.validator.addMethod("maxFilesToSelect", function(value, element, params) {
        var fileCount = element.files.length;
        if (fileCount > params) {
            return false;
        } else {
            return true;
        }
    }, 'You can not upload more than 15 media.');

    /* Forgot password custom validation */
    $('#forgotFormValidation').validate({
        rules: {
            email: {
                required: true,
                maxlength: 50,
                email: true
            }
        },
        submitHandler: function(form) {
            if ($("#forgotFormValidation").validate().checkForm()) {
                $('.requestbutton').addClass('disabled').attr('disabled', true);
                $(".cancelbutton").addClass("disabled");
                form.submit();
            }
        }
    })

    /* Login custom validation */
    $('#loginFormValidation').validate({
        rules: {
            email: {
                required: true,
                maxlength: 50,
                email: true
            },
            password: {
                required: true,
                minlength: 8,
                maxlength: 20,
            },
        },
        submitHandler: function(form) {
            if ($("#loginFormValidation").validate().checkForm()) {
                $('.requestbutton').addClass('disabled').attr('disabled', true);
                $(".cancelbutton").addClass("disabled");
                form.submit();
            }
        }
    });

    /* Login custom validation */
    $('#registerFormValidation').validate({
        rules: {
            name: {
                required: true,
                maxlength: 50,
            },
            email: {
                required: true,
                maxlength: 50,
                email: true,
                remote: {
                    url: "/checkEmail/",
                    type: "POST",
                    headers: {
                        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                    },
                    data: {
                        email: function() { return $('input[name=email]').val(); },
                    },
                },
            },
            address: {
                required: true,
            },
            country: {
                required: true,
                maxlength: 50,
            },
            state: {
                required: true,
                maxlength: 50,
            },
            city: {
                required: true,
                maxlength: 50,
            },
            mobile_number: {
                required: true,
                validphone: true,
                maxlength: 15,
                remote: {
                    url: "/checkMobilenumber/",
                    type: "POST",
                    headers: {
                        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                    },
                    data: {
                        mobile_number: function() { return $('input[name=mobile_number]').val(); },
                    },
                },
            },
            category: {
                required: true,
            },
            catering: {
                required: true,
            },
            max_capacity: {
                required: true,
            },
            number_of_events: {
                required: true,
            },
            media: {
                required: true,
                extension: "jpg|jpeg|png",
                maxFilesToSelect: 15,
            },
            password: {
                required: true,
                minlength: 8,
                maxlength: 20,
            },
            password_confirmation: {
                required: true,
                minlength: 5,
                maxlength: 20,
                equalTo: "#password"
            },
            terms_confirmed: {
                required: true,
            },
        },
        messages: {
            mobile_number: { remote: "Mobile number is already taken." },
            email: { remote: "Email is already taken." },
            terms_confirmed: { required: "" }
        },
        submitHandler: function(form) {
            if ($("#registerFormValidation").validate().checkForm()) {
                $('.requestbutton').addClass('disabled').attr('disabled', true);
                $(".cancelbutton").addClass("disabled");
                form.submit();
            }
        }
    })


    /* Password Show and Hide */
    $(".toggle-password").click(function() {
        $(this).toggleClass("eye");
        input = $(this).parent().find("input");
        if (input.attr("type") == "password") {
            // $(this).find('.eye').attr("data-feather", "eye-close");
            input.attr("type", "text");
        } else {
            // $(this).find('.eye').attr("data-feather", "eye");
            input.attr("type", "password");
        }
    });
});

function getPageLengthDatatable() {
    return [
        [10, 25, 50, -1],
        [10, 25, 50, "All"]
    ];
}

var myThing = (function() {
    function getParameterDataTable(page_length, settings) {
        return [{
            processing: true,
            serverSide: true,
            bLengthChange: false,
            pagingType: "simple_numbers",
            sScrollY: '600px',
            pageLength: page_length,
            drawCallback: function(settings) {
                feather.replace();
            }
        }];
    }
});


$(document).ready(function() {
    var notFound = $("#notFound")
    var oddFound = $(".odd")
        // make it hidden by default
    notFound.hide()
        // select notFound row
    $("#search_text").on("keyup", function() {
        var value = $(this).val().toLowerCase()

        // select all items
        var allItems = $("#datalist_table tbody tr")

        // get list of matched items, (do not toggle them)
        var matchedItems = $("#datalist_table tbody tr").filter(function() {
            return $(this).text().toLowerCase().indexOf(value) > -1
        });

        // hide all items first
        allItems.toggle(false)

        // then show matched items
        matchedItems.toggle(true)

        // if no item matched then show notFound row, otherwise hide it
        if (matchedItems.length == 0) {
            oddFound.removeClass('d-none')
            notFound.show()
        } else {
            notFound.hide()
            oddFound.addClass('d-none')
        }
    });
});


var historyModalDiv = $("#commentHistory_table");
$(".commentHistorybtn").on("click", function(e) {
    e.preventDefault();
    $.ajax({
        url: $(this).attr("data-popup-url"),
        success: function(data) {
            historyModalDiv.html(data);
        }
    });
});

$("#commentHistory_table").DataTable({
    paging: false,
    bLengthChange: false,
    searching: false,
    responsive: true,
    searchDelay: 500,
    processing: false,
    bInfo: false,
});


// // pagination
// var items = $("#datalist_table tbody tr");
// var numItems = items.length;
// var perPage = 10;

// items.slice(perPage).hide();

// $('#pagination-container').pagination({
//     items: numItems,
//     itemsOnPage: perPage,
//     prevText: "&laquo;",
//     nextText: "&raquo;",
//     onPageClick: function(pageNumber) {
//         var showFrom = perPage * (pageNumber - 1);
//         var showTo = showFrom + perPage;
//         items.hide().slice(showFrom, showTo).show();
//     }
// });

// $(function() {
//     const rowsPerPage = 1;
//     const rows = $('#datalist_table tbody tr');
//     const rowsCount = rows.length;
//     const pageCount = Math.ceil(rowsCount / rowsPerPage); // avoid decimals
//     const numbers = $('#numbers');

//     // Generate the pagination.
//     for (var i = 0; i < pageCount; i++) {
//         numbers.append('<li class="paginate_button page-item"><a href="#" class="page-link">' + (i + 1) + '</a></li>');
//     }

//     // Mark the first page link as active.
//     $('#numbers li:first-child a').addClass('active');

//     // Display the first set of rows.
//     displayRows(1);

//     // On pagination click.
//     $('#numbers li a').click(function(e) {
//         var $this = $(this);
//         e.preventDefault();

//         // Remove the active class from the links.
//         $('#numbers li a').removeClass('active');

//         // Add the active class to the current link.
//         $this.addClass('active');

//         // Show the rows corresponding to the clicked page ID.
//         displayRows($this.text());
//     });

//     // Function that displays rows for a specific page.
//     function displayRows(index) {
//         var start = (index - 1) * rowsPerPage;
//         var end = start + rowsPerPage;

//         // Hide all rows.
//         rows.hide();

//         // Show the proper rows for this page.
//         rows.slice(start, end).show();
//     }
// });