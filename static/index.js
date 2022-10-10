function analyse_click(p1) {
    // variables
    var analyse_textbox_value = document.getElementById('urlTextbox').value;
    var article_heading_text = document.getElementById('article-heading-id');
    var article_body_text = document.getElementById('article-body-id');

    article_heading_text.innerHTML = 'Test heading';
    article_body_text.innerHTML = analyse_textbox_value;

  }