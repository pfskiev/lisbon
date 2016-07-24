var gulp   = require('gulp'),
    uglify = require('gulp-uglifyjs'),
    concat = require('gulp-concat'),
    cssmin = require('gulp-cssmin'),
    rename = require('gulp-rename'),
    vendor = {
        path: 'vendor'
    };

gulp.task('default', ['js', 'css']);

gulp.task('css', function () {
    gulp.src([
        vendor.path + '/tether/dist/css/tether.css',
        vendor.path + '/bootstrap/dist/css/bootstrap.css',
        vendor.path + '/components-font-awesome/css/font-awesome.css',
        vendor.path + '/jquery-ui/themes/flick/jquery-ui.css',
        vendor.path + '/flag-icon-css/css/flag-icon.css'
    ])
        .pipe(concat('vendor.min.css'))
		.pipe(gulp.dest(vendor.path));
    console.log('[' + new Date().getHours() + ':' + new Date().getMinutes() + ':' + new Date().getSeconds() + ']' + ' css task is done')
});

gulp.task('js', function () {
    gulp.src([
        vendor.path + '/jquery/dist/jquery.js',
        vendor.path + '/jquery-ui/jquery-ui.js',
        vendor.path + '/jquery-mask/jquery.mask.js',
        vendor.path + '/tether/dist/js/tether.js',
        vendor.path + '/bootstrap/dist/js/bootstrap.js',
        vendor.path + '/lodash/dist/lodash.js',
        vendor.path + '/moment/min/moment.min.js'
    ])
        .pipe(uglify('vendor.min.js', {
            outSourceMap: true
        }))
        .pipe(gulp.dest(vendor.path));
    console.log('[' + new Date().getHours() + ':' + new Date().getMinutes() + ':' + new Date().getSeconds() + ']' + ' js task is done')
});