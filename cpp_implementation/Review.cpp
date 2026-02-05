#include "Review.h"

Review::Review(int id, int novel_id, int reader_id, const std::string& content,
               int rating, const std::string& date_posted, int helpful_count)
    : id(id), novel_id(novel_id), reader_id(reader_id), content(content),
      rating(rating), date_posted(date_posted), helpful_count(helpful_count) {}

Review::~Review() {
}

void Review::editContent(const std::string& newContent) {
}

void Review::markHelpful() {
}
