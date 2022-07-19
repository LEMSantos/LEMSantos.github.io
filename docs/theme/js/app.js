window.addEventListener('load', function (e) {
    window.code_tags = document.getElementsByTagName('pre');
    copy_btn = '<button class="copy-btn"><i class="fa fa-clone fa-lg"></i></button>';

    for (var i = 0, max = code_tags.length; i < max; i++)
    {
        window.code_tags[i].insertAdjacentHTML('beforeend', copy_btn);
    }

    copy_btns = document.querySelectorAll('pre button.copy-btn');

    for (var i = 0, max = copy_btns.length; i < max; i++)
    {
        copy_btns[i].addEventListener('click', function (event) {
            code_tag = event.target.closest('pre');
            copy_btn = event.target.closest('button.copy-btn');

            navigator.clipboard.writeText(window.code_tag.outerText);
            copy_btn.classList.add('copied');

            setTimeout(function () {
                copy_btn.classList.remove('copied');
            }, 2000);
        });
    }
});


