# preprocessRawText
preprocessRawText NLP

- Chạy lệnh cài đặt : sudo pip install preprocessRawText
- có 2 funtion :
    + clean_text(text) : truyền vào 1 đoạn text và trả về text đã được xử lý
    + clean_text_file(url): truyền vào url file csv (có định dạng string) và trả về 1 json

- ví dụ :

    from preprocessRawText.pretreatment import clean_text

    def demo(text):
          return clean_text(text)