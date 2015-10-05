'use strict';

var counter = 0;
angular.module('AniTheme').directive('ckedit', function ($parse) {
    CKEDITOR.disableAutoInline = true;
        var prefix = '__ckd_';

    return {
        restrict: 'A',
        link: function (scope, element, attrs, controller) {
            var getter = $parse(attrs.ckedit),
                setter = getter.assign;

            attrs.$set('contenteditable', true); // inline ckeditor needs this
            if (!attrs.id) {
                attrs.$set('id', prefix + (++counter));
            }

            var options = {};
            options.on = {
                blur: function (e) {
                    if (e.editor.checkDirty()) {
                        var ckValue = e.editor.getData();
                        scope.$apply(function () {
                            setter(scope, ckValue);
                        });
                        ckValue = null;
                        e.editor.resetDirty();
                    }
                }
                , contentDom: function (ev) {
                    //console.log(ev);
                    //var xhr = ev.data.fileLoader.xhr;
                    //console.log(xhr);

                },
                dialogDefinition: function (ev) {
                    //console.log(ev);
                }

            };
            options.extraPlugins = 'lineutils,notification,uploadwidget,uploadimage';
            options.removePlugins = 'sourcearea';
            options.filebrowserUploadUrl = '/api/v1/file/upload';
            options.extraPlugins = 'lineutils,notification,uploadwidget,uploadimage';
            options.removePlugins = 'sourcearea';
            options.filebrowserUploadUrl = '/api/v1/file/upload';

            options.toolbar = [
                {
                    name: 'document',
                    items: ['Source', '-', 'NewPage', 'Preview', '-', 'Templates', 'Image', 'Table', 'Bold', 'Italic']
                },	// Defines toolbar group with name (used to create voice label) and items in 3 subgroups.
                ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']

            ];

            //CKEDITOR.replace(editorangular, {
            //    filebrowserUploadUrl: '/uploader/upload.php'
            //});


            var editorangular = CKEDITOR.replace(element[0], options); //invoke


            scope.$watch(attrs.ckedit, function (value) {
                editorangular.setData(value);
            });
        }
    }

});


