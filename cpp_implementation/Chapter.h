#ifndef CHAPTER_H
#define CHAPTER_H

#include <string>

class Chapter {
private:
    int id;
    int chapter_number;
    std::string title;
    std::string content;
    int word_count;
    long view_count;
    std::string published_at;
    bool is_premium;

public:
    Chapter(int id, int chapter_number, const std::string& title,
            const std::string& content, int word_count, long view_count,
            const std::string& published_at, bool is_premium);
    ~Chapter();

    std::string displayContent();
    void incrementViews();
};

#endif
