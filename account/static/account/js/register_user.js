$(document).ready(function () {
    $('.form-register').submit(function (e) {
        e.preventDefault();
        console.log('in form submit')

        let form = $(this);
        let csrftoken = $("[name=csrfmiddlewaretoken]").val();

        let email = $('#id_email');
        console.log('email', email)
        let password = $('#id_password');
        let re_password = $('#id_re_password');
        let email_validation = $('.email_validation');
        // let password_container = $('.password-container');

        if (email.val() == "") {
            email_validation.show();
            $('.email_validation span').text('ایمیل را وارد کنید');
            email.focus();
            return false;
        }
        if (IsEmail(email.val()) == false) {
            email_validation.show();
            $('.email_validation span').text('آدرس ایمیل درست نیست!');
            email.focus();
            return false;
        } else if (IsEmail(email.val()) == true) {
            email_validation.hide();
        }

        if (passivization(password.val(), re_password.val()) == false) {
            $('.password_validation').show();
            password.focus();
            return false;
        } else if (passivization(password.val(), re_password.val()) == true) {
            $('.password_validation').hide();
        }


        $.ajax({
            type: "POST",
            headers: {
                "X-CSRFToken": csrftoken
            },
            url: '',
            data: form.serialize(),

            success: function (e) {

            },
            error: function (rs, e) {
            },
        })
        $('.modal').modal('hide');
        return false;
    });

    function IsEmail(email) {
        let regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (!regex.test(email)) {
            return false;
        } else {
            return true;
        }
    }

    function passivization(pass_value, re_pass_value) {
        if (pass_value.length === 0){
            $('.password_validation span').text('کلمه عبور خالی است و یا کوتاه است!');
            return false;
        }
        if (pass_value.length < 8){
            $('.password_validation span').text('طول گذرواژه باید از 8 کاراکتر بیشتر باشد!');
            return false;
        }
        else if(pass_value.length > 12){
            $('.password_validation span').text('طول گذرواژه باید از 12 کاراکتر کمتر باشد!');
             return false;
        } else if(pass_value !== re_pass_value){
             $('.password_validation span').text('گذرواژه اشتباه وارد شده است!');
             return false;
        }
        else{
            return true;
        }
    }

})
