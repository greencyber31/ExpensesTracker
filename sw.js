const CACHE_NAME = 'expenses-tracker-v13';
const ASSETS = [
    './',
    './index.html',
    './Expenses_tracker.html',
    './sw.js'
];

self.addEventListener('install', (event) => {
    self.skipWaiting(); // Force new service worker to take over
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS);
        })
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(clients.claim()); // Take control of all pages immediately
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
