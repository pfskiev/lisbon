importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js');

const CACHE_NAME = 'workbox:js';

const APP_JS = new RegExp('/static/custom/js/.*\.js');
const APP_ANGULAR_JS = new RegExp('/static/custom/js/app/.*\.js');
const VENDOR_JS = new RegExp('/static/vendor/js/.*\.js');

workbox.routing.registerRoute(
    '/',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'pages-home',
    })
  );

workbox.routing.registerRoute(
    APP_JS,
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'app-js',
    })
  );

workbox.routing.registerRoute(
    APP_ANGULAR_JS,
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'angular-js',
    })
  );

workbox.routing.registerRoute(
    VENDOR_JS,
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'vendor-js',
    })
  );
