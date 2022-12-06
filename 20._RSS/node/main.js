import Parser from 'rss-parser';
import fs from 'fs';
const parser = new Parser();

// const feed = await parser.parseURL('https://daily-dev-tips.com/sitemap.xml');

const rssFileString = fs.readFileSync("../feedexample.xml").toString();

const feed = await parser.parseString(rssFileString);


console.log(feed.title);

feed.items.forEach((item) => {
    console.log(item.title);
});

    