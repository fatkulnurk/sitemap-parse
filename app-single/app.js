var sitemaps = require('sitemap-stream-parser');

var end_point = 'https://liriklaguindonesia.net/sitemap.xml';
var urls = [];
var all_urls = [];

sitemaps.parseSitemaps(end_point, function(url) {
    urls.push(url);
}, function(err, sitemaps) {
    sitemaps.parseSitemaps(urls, function(u) {
        all_urls.push(u);
    }, function(err, sitemaps) {
        console.log(all_urls);
        console.log('All done!');
    });
});

var i;
const fs = require('fs');
var stream = fs.createWriteStream("result.txt");
stream.once('open', function(fd) {
    for (i = 0; i < all_urls.length; i++) {
        stream.write(all_urls[i] + ',');
    }
    stream.end();
});

console.log('finish');