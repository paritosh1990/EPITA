(function() {
  var editor, authorship, cursorManager;

  editor = new Quill('.advanced-wrapper .editor-container', {
    modules: {
      'authorship': {
        enabled: true
      },
      'toolbar': {
        container: '.advanced-wrapper .toolbar-container'
      },
      'link-tooltip': true,
      'image-tooltip': true,
      'multi-cursor': false
    },
    theme: 'snow'
  });

}).call(this);
