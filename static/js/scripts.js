/*!
* Start Bootstrap - Blog Home v5.0.7 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

$(function () {
    $(".comment-list").slice(0, 4).show();
    $("#load-comments").on('click', function () {
        $(".comment-list:hidden").slice(0, 4).slideDown();
    });
});

$(function () {
    $(".category-list").slice(0, 6).show();
    $("#load-categories").on('click', function () {
        $(".category-list:hidden").slice(0, 6).slideDown();
    });
});

$(document).ready(function(){
    $('#summernote').summernote({
        placeholder: 'Hello stand alone ui',
        tabsize: 2,
        height: 120,
        toolbar: [
        ['style', ['style']],
        ['font', ['bold', 'underline', 'clear']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video']],
        ['view', ['fullscreen', 'codeview', 'help']]
        ]
    });
});