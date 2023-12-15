import requests
import re

class WebCrawler:

    def __init__(self):
        # Khởi tạo WebCrawler với một danh sách trống để theo dõi các trang web đã phát hiện.
        self.discovered_websites = []

    def crawl(self, start_url):
        # Khởi tạo một hàng đợi với URL khởi đầu và đánh dấu nó là đã phát hiện.
        queue = [start_url]
        self.discovered_websites.append(start_url)

        # Tiếp tục việc lặp qua khi còn URL trong hàng đợi.
        while queue:
            # Lấy URL tiếp theo từ đầu hàng đợi.
            actual_url = queue.pop(0)
            print(actual_url)

            # Lấy nội dung HTML của URL hiện tại.
            actual_url_html = self.read_raw_html(actual_url)

            # Trích xuất các liên kết từ HTML và thêm các URL mới vào hàng đợi.
            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)
    
    def get_links_from_html(self, raw_html):
        # Sử dụng biểu thức chính quy để tìm kiếm các URL trong nội dung HTML gốc.
        return re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', raw_html)
    
    def read_raw_html(self, url):
        # Khởi tạo raw_html là một chuỗi trống.

        raw_html = ''

        try:
            # Sử dụng thư viện requests để lấy nội dung HTML của URL đã cho.
            raw_html = requests.get(url).text
        except Exception as e:
            # Xử lý các ngoại lệ nếu có lỗi khi lấy HTML.
            print(f"Lỗi khi tải {url}: {e}")

        return raw_html
    
if __name__ == '__main__':
    # Tạo một thể hiện của lớp WebCrawler và bắt đầu crawling từ URL được chỉ định.
    crawler = WebCrawler()

