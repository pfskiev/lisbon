importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js');

const CACHE_NAME = 'workbox:assets';

// Cache all
const REGEXP_ALL = /.*\.(?:js|css|png|jpg|jpeg|svg|gif)/;

// [OK] Stale While Revalidate
workbox.routing.registerRoute(
  REGEXP_ALL,
  workbox.strategies.staleWhileRevalidate({
    cacheName: `${CACHE_NAME}:stale-while-revalidate`,
  }),
);
