/*
Copyright (c) 2003-2012, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

CKEDITOR.editorConfig = function( config )
{
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    // config.filebrowserBrowseUrl = '/browser/browse.py';
    // config.filebrowserUploadUrl = '/uploader/upload.py';
    config.width = '620px';
    config.height = '500px';
    config.toolbar = 'MyToolbar';
    config.toolbar_MyToolbar =
        [
            { name: 'document', items : [ 'Source','-','Preview' ] },
            { name: 'clipboard', items : [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ] },
            { name: 'insert', items : [ 'Image','Table','HorizontalRule','Smiley','SpecialChar'] },
            { name: 'paragraph', items : [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote' ] },
            '/',
            { name: 'styles', items : [ 'Styles','Format', 'Font','FontSize'  ] },
            { name: 'basicstyles', items : [ 'Bold','Italic','Strike','-','RemoveFormat', '-','JustifyLeft','JustifyCenter','JustifyRight' ] },
            { name: 'tools', items : [ 'Maximize'] }
        ];
};
