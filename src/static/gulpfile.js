var gulp   = require('gulp'),
    uglify = require('gulp-uglifyjs'),
    concat = require('gulp-concat'),
    cssmin = require('gulp-cssmin'),
    rename = require('gulp-rename'),
    sass   = require('gulp-sass');
    path = {
        vendor: './vendor',
        custom: './custom/css/dist/'
    };

gulp.task('default', ['js', 'css']);

gulp.task('css', function () {
    gulp.src([
        path.vendor + '/tether/dist/css/tether.css',
        path.vendor + '/bootstrap/dist/css/bootstrap.css',
        path.vendor + '/components-font-awesome/css/font-awesome.css',
        path.vendor + '/jquery-ui/themes/flick/jquery-ui.css',
        path.vendor + '/flag-icon-css/css/flag-icon.css'
    ])
        .pipe(concat('vendor.min.css'))
		.pipe(gulp.dest(path.vendor));
    console.log('[' + new Date().getHours() + ':' + new Date().getMinutes() + ':' + new Date().getSeconds() + ']' + ' css task is done')
});

gulp.task('sass', function () {
    return gulp.src(path.custom + '*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(cssmin())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(path.custom));
});

gulp.task('js', function () {
    gulp.src([
        path.vendor + '/jquery/dist/jquery.js',
        path.vendor + '/jquery-ui/jquery-ui.js',
        path.vendor + '/jquery-mask/jquery.mask.js',
        path.vendor + '/tether/dist/js/tether.js',
        path.vendor + '/bootstrap/dist/js/bootstrap.js',
        path.vendor + '/lodash/dist/lodash.js',
        path.vendor + '/moment/min/moment.min.js'
    ])
        .pipe(uglify('vendor.min.js', {
            outSourceMap: true
        }))
        .pipe(gulp.dest(path.vendor));
    console.log('[' + new Date().getHours() + ':' + new Date().getMinutes() + ':' + new Date().getSeconds() + ']' + ' js task is done')
});