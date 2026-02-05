#ifndef REVIEW_H
#define REVIEW_H

#include <string>

class Review {
private:
    int id;
    int novel_id;
    int reader_id;
    std::string content;
    int rating;
    std::string date_posted;
    int helpful_count;

public:
    Review(int id, int novel_id, int reader_id, const std::string& content,
           int rating, const std::string& date_posted, int helpful_count);
    ~Review();

    void editContent(const std::string& newContent);
    void markHelpful();
};

#endif
