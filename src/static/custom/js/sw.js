importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js');

workbox.routing.registerRoute(
    '/',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'pages-home',
    })
  );

workbox.routing.registerRoute(
    '/static/custom/js/main.js',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'app-js',
    })
  );

workbox.routing.registerRoute(
    '/static/custom/css/dist/styles.min.css',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'app-css',
    })
  );

workbox.routing.registerRoute(
    '/static/vendor/vendor.min.js',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'vendor-js',
    })
  );

workbox.routing.registerRoute(
    '/static/vendor/vendor.min.css',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'vendor-css',
    })
  );
