var sitemaps = require('sitemap-stream-parser');

var end_point = 'https://www.liriklagu.info/sitemap_index.xml';
var urls = [];
var all_urls = [];

var date = Date().toString();

sitemaps.parseSitemaps(end_point, function(url) { all_urls.push(url); }, function(err, sitemaps) {
    var i;
    const fs = require('fs');
    var stream = fs.createWriteStream("result--" + date + ".txt");
    stream.once('open', function(fd) {
        for (i = 0; i < all_urls.length; i++) {
            stream.write(all_urls[i] + ',');
        }
        stream.end();
    });
});