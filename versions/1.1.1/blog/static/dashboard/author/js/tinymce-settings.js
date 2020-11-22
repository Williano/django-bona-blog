 tinymce.init({
      selector: '#content',
      max_width: 500,
      max_height: 700,
      min_height: 500,
      min_width: 400,
      plugins: 'autolink lists media table  ' +
          'emoticons anchor pagebreak visualchars code ' +
          'fullscreen autolink  charmap print  hr searchreplace ' +
          'wordcount visualblocks table advlist fullscreen  ' +
          'insertdatetime  nonbreaking save link image media preview ' +
          'codesample',
      toolbar1: 'checklist table fullscreen preview bold ' +
                'italic underline | fontselect fontsizeselect | forecolor backcolor |' +
                'alignleft alignright | aligncenter alignjustify | indent outdent ' +
                'bullist numlist | link image media | code | emoticons | visualblocks ' +
                'visualchars | charmap hr pagebreak nonbreaking anchor | codesample',
      toolbar_mode: 'floating',
      custom_undo_redo_levels: 20,
      codesample_global_prismjs: true,
      apply_source_formatting : true
    });
