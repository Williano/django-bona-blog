
$(document).ready(function () {

     // Execute this function when the Preview button is clicked.
    $('#preview-article').on('click', function (e) {

        // Hide article detail modal
         $('#dynamic-content').hide();

         // show loader when data is being sent to server
              $('#modal-loader').show();

         // Get form data
         let articleAction = $(this).attr("value");
         let articleURL = $(this).attr("data-url");

         let articleTitle = $('#id_title').val();
         let articleCategory = $('#id_category').val();
         let articleImage = $('#id_image').val();
         let articleBody = $('#id_body').val();
         let articleTags = $('#id_tags').val();
         let articleStatus = $('#id_status').val();

         // Create an article object with extracted form data.
         let articleData = {csrfmiddlewaretoken: $.cookie("csrftoken"), action: articleAction,
                            title: articleTitle, category: articleCategory,
                            image: articleImage, body: articleBody,
                            tags: articleTags, status: articleStatus
         };

         // Call post article function and send the data to the endpoint
         postArticle(articleURL, articleData);

         e.preventDefault();

    });

});


function postArticle(articleURl, articleData) {

     // post data to endpoint
     $.post(articleURl, articleData)
         // Display data from endpoint in modal
         .done(function(data){
             // hide ajax loader when view is displayed
              $('#modal-loader').hide();

              $('#dynamic-content').show(); // show dynamic div
                 console.log(data)
                // Display data from server in HTML template
                  let articlePreviewHtml = `
                       <article class="blog-post px-3 py-5 p-md-5">
                            <div class="container">
                                <header class="blog-post-header">
                                    <h2 class="title mb-2" id="article-title">${data.title}</h2>
                                    <div class="meta mb-3"><span class="date" id="category">${data.category}</span></div>
                                </header>

                                <div class="blog-post-body">
                                    <figure class="blog-banner">
                                       <img class="img-fluid" id="article-image" src="${data.image}" alt="image">
                                        <figcaption class="mt-2 text-center image-caption">
                                        Image Credit: <a href="https://made4dev.com?ref=devblog" target="_blank">
                                        made4dev.com (Premium Programming T-shirts)</a></figcaption>
                                    </figure>
                                    <p id="article-body">${data.body}</p>
                                </div>
                            </div>
                      </article>
                   `;

               // Display the HTML template with data in view.
              $('#article-content').html(articlePreviewHtml);
  })
         // Display error if something went wrong.
         .fail(function(){

      $('.modal-body').html('<i class="fas fa-info-circle"></i>' +
          " Something went wrong, Please try again...");
  });
}