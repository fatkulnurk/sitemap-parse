//https://www.npmjs.com/package/advanced-sitemap-generator

const SitemapGenerator = require('sitemap-generator');

// create generator
const generator = SitemapGenerator('https://www.azlyrics.com', {
    stripQuerystring: false,
    ignoreHreflang: true,
    maxDepth: 0,
    filepath: path.join(process.cwd(), 'sitemap.xml'),
    maxEntriesPerFile: 500000,
    excludeFileTypes: ['gif', 'jpg', 'jpeg', 'png', 'ico', 'bmp', 'ogg', 'webp', 'mp4', 'webm', 'mp3', 'ttf',
    'woff', 'json', 'rss', 'atom', 'gz', 'zip', 'rar', '7z', 'css', 'js', 'gzip', 'exe', 'svg',
    'xml'],
    excludeURLs: ['cxyz']
});

// register event listeners
generator.on('done', () => {
    // sitemaps created
    console.log('Sitemap Berhasil dibuat');
});

// start the crawler
generator.start();
