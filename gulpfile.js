/****************** FOR STUDENT PAGE ******************/
const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass');

gulp.task('sass', function () {
    return gulp.src(['unital/static/scss/*.scss'])
        .pipe(sass())
        .pipe(gulp.dest("unital/static/css"))
});
gulp.task('serve', ['sass'], function () {
    gulp.watch(['unital/static/scss/*.scss'], ['sass']);
});
gulp.task('default', ['serve']);
/****************** FOR STUDENT PAGE ******************/




// const gulp = require('gulp');
// const browserSync = require('browser-sync').create();
// const sass = require('gulp-sass');

// // Compile SASS
// gulp.task('sass', function () {
//     return gulp.src(['node_modules/bootstrap/scss/bootstrap.scss', 'unital/static/scss/*.scss'])
//         .pipe(sass())
//         .pipe(gulp.dest("unital/static/css"))
//         // .pipe(browserSync.stream());
// });

// // Move JS Files to SRC
// gulp.task('js', function () {
//     return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/tether/dist/js/tether.min.js','node_modules/jquery.marquee/jquery.marquee.min.js'])
//         .pipe(gulp.dest("unital/static/js"))
//         .pipe(browserSync.stream());
// });

// // Watch SASS & Serve
// gulp.task('serve', ['sass'], function () {
//     // browserSync.init({
//     //     server: "./src"
//     // });

//     gulp.watch(['node_modules/bootstrap/scss/bootstrap.scss', 'unital/static/scss/*.scss'], ['sass']);
//     // gulp.watch("src/*.html").on('change', browserSync.reload);
// });

// // Move Font Awesome Fonts folder to src
// gulp.task('fonts', function () {
//     return gulp.src('node_modules/@fortawesome/fontawesome-free/webfonts/*')
//         .pipe(gulp.dest("unital/static/webfonts"));
// });

// // Move font awesome css file
// gulp.task('fa', function () {
//     return gulp.src('node_modules/@fortawesome/fontawesome-free/css/all.min.css')
//         .pipe(gulp.dest("unital/static/css/"));
// });

// gulp.task('default', ['js', 'fa', 'fonts', 'serve']);
