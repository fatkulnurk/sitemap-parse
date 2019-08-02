var sitemaps = require('sitemap-stream-parser');

var end_point = 'https://liriklaguindonesia.org/sitemap_index.xml';
var all_urls = [];

var date = Date().getDate().toString();
var name = "result-" + end_point + "-" + date + ".txt";

sitemaps.parseSitemaps(end_point, function(url) { all_urls.push(url); }, function(err, sitemaps) {
    var i;
    const fs = require('fs');
    fs.appendFile(name);
    var stream = fs.createWriteStream(name);
    stream.once('open', function(fd) {
        for (i = 0; i < all_urls.length; i++) {
            stream.write(all_urls[i] + ',');
        }
        stream.end();
    });
});