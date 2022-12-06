import feedparser

local_feed_url = "../feedexample.xml"

example_feed = feedparser.parse(local_feed_url)

print(example_feed.feed.title)


# feed_url = "https://vaibhavkumar.hashnode.dev/rss.xml"
  
# blog_feed = feedparser.parse(feed_url)

# print(blog_feed.feed.title)
# print(blog_feed.feed.link)
# print(len(blog_feed.entries))

# print()

# print(blog_feed.entries[0].title)
# print(blog_feed.entries[0].link)
# print(blog_feed.entries[0].author)
# print(blog_feed.entries[0].published)


# tags = [tag.term for tag in blog_feed.entries[0].tags]
# authors= [author.name for author in blog_feed.entries[0].authors]

