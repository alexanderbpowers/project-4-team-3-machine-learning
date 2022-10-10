function random_result() {
    // for demo purposes
    var resultsTitle = document.getElementById('resultTitle');
    var resultsText = document.getElementById('resultText');

    x = Math.random();
    if(x < 0.5){
        resultsTitle.innerHTML = ' result less than .5';
        resultsText.innerHTML = 'RED';

        resultsTitle.style.color = 'red';
        resultsText.style.color = 'red';
    }else{
        resultsTitle.innerHTML = ' result greater than .5';
        resultsText.innerHTML = 'BLUE';

        resultsTitle.style.color = 'green';
        resultsText.style.color = 'green';
    };

    


}

function urlPasser(urlInput) {
    // variables
    var analyse_textbox_value = document.getElementById('urlTextbox').value;
    var article_heading_text = document.getElementById('article-heading-id');
    var article_body_text = document.getElementById('article-body-id');

    // calling the flask scrapping API

    d3.json("/api/ArticleScrape/" + urlInput).then(function (data) {

        var article_body = data.text;
        var article_title = data.title;
        article_heading_text.innerHTML = article_title;
        article_body_text.innerHTML = article_body;

    });

    

  }

function analyse_click() {
    // variables
    var analyse_textbox_value = document.getElementById('urlTextbox').value;
    var article_heading_text = document.getElementById('article-heading-id');
    var article_body_text = document.getElementById('article-body-id');

    // article_heading_text.innerHTML = 'Test heading';
    // article_body_text.innerHTML = analyse_textbox_value;

    // calling a random result for testing
    random_result();
    // pass URL into the function that calls scrapping API
    urlPasser(analyse_textbox_value);


  }

 