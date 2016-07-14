var gulp   = require('gulp'),
    uglify = require('gulp-uglifyjs'),
    concat = require('gulp-concat'),
    cssmin = require('gulp-cssmin'),
    rename = require('gulp-rename');

gulp.task('default', function() {
    gulp.src([
        'vendor/tether/dist/css/tether.min.css',
        'vendor/bootstrap/dist/css/bootstrap.min.css',
        'vendor/components-font-awesome/css/font-awesome.min.css',
        'vendor/jquery-ui/themes/flick/jquery-ui.min.css',
        'vendor/flag-icon-css/css/flag-icon.min.css'

    ])
        .pipe(concat('vendor.min.css'))
		.pipe(gulp.dest('vendor/'));

    gulp.src([
        'vendor/jquery/dist/jquery.js',
        'vendor/jquery-ui/jquery-ui.js',
        'vendor/jquery-mask/jquery.mask.js',
        'vendor/tether/dist/js/tether.js',
        'vendor/bootstrap/dist/js/bootstrap.js',
        'vendor/lodash/dist/lodash.js',
        'vendor/moment/min/moment.min.js'
    ])
        .pipe(uglify('vendor.min.js', {
            outSourceMap: true
        }))
        .pipe(gulp.dest('vendor/'))
});