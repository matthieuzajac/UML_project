#include "Chapter.h"

Chapter::Chapter(int id, int chapter_number, const std::string& title,
                 const std::string& content, int word_count, long view_count,
                 const std::string& published_at, bool is_premium)
    : id(id), chapter_number(chapter_number), title(title), content(content),
      word_count(word_count), view_count(view_count), published_at(published_at),
      is_premium(is_premium) {}

Chapter::~Chapter() {
}

std::string Chapter::displayContent() {
    return "";
}

void Chapter::incrementViews() {
}
