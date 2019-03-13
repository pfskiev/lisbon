importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js');

const CACHE_NAME = 'workbox:js';

const APP_JS = new RegExp('/static/custom/.*\.js');
const APP_ANGULAR_JS = new RegExp('/static/custom/app/.*\.js');
const VENDOR_JS = new RegExp('/static/vandor/.*\.js');

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
