const { mix } = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('resources/assets/js/app.js', 'static/js')
   .sass('resources/assets/sass/app.scss', 'static/css');

mix.scripts([
    'resources/assets/js/plugins/jquery.js',
    'resources/assets/js/plugins/prism.js',
    'resources/assets/js/plugins/bootstrap.js',
    'resources/assets/js/plugins/scotchPanels.js',
    'resources/assets/js/plugins/typeahead.js',
    'resources/assets/js/plugins/hogan.js',
    'resources/assets/js/plugins/mousetrap.js',
], 'static/js/plugins.js');
