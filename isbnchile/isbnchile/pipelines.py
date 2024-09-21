import json

from itemadapter import ItemAdapter

from .items import BookDetailItem, BookItem


class CustomJsonPipeline:
    def open_spider(self, spider):
        self.book_file = open('../books/books.ndjson', 'w')
        self.book_detail_file = open('../books/book_details.ndjson', 'w')

    def close_spider(self, spider):
        self.book_file.close()
        self.book_detail_file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False)
        
        if isinstance(item, BookItem):
            self.book_file.write(line)

        elif isinstance(item, BookDetailItem):
            self.book_detail_file.write(line)

        return item