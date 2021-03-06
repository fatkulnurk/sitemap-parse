var sitemaps = require('sitemap-stream-parser');

var end_point = 'https://liriklaguindonesia.net/sitemap.xml';
var all_urls = [];

var date = new Date().getDate().toString();
var name = "result-liriklaguindonesianet.txt";

sitemaps.parseSitemaps(end_point, function(url) { all_urls.push(url); }, function(err, sitemaps) {
    var i;
    const fs = require('fs');
    fs.open(name, 'w', function(err, file) {
        if (err) throw err;
        console.log('Saved!');
    });

    var stream = fs.createWriteStream(name);
    stream.once('open', function(fd) {
        for (i = 0; i < all_urls.length; i++) {
            stream.write(all_urls[i] + ',');
        }
        stream.end();
    });
});