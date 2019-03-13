importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js');

const CACHE_NAME = 'workbox:js';

const APP_JS = new RegExp('/static/custom/.*\.js');
const APP_ANGULAR_JS = new RegExp('/static/custom/app/.*\.js');
const VENDOR_JS = new RegExp('/static/vandor/.*\.js');


// [OK] Stale While Revalidate
workbox.routing.registerRoute(
  APP_JS,
  workbox.strategies.staleWhileRevalidate({
    cacheName: `${CACHE_NAME}:stale-while-revalidate`,
  }),
);

// [OK] Stale While Revalidate
workbox.routing.registerRoute(
  APP_ANGULAR_JS,
  workbox.strategies.staleWhileRevalidate({
    cacheName: `${CACHE_NAME}:stale-while-revalidate`,
  }),
);

// [OK] Stale While Revalidate
workbox.routing.registerRoute(
  VENDOR_JS,
  workbox.strategies.staleWhileRevalidate({
    cacheName: `${CACHE_NAME}:stale-while-revalidate`,
  }),
);
