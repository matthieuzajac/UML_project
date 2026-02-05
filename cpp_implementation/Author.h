#ifndef AUTHOR_H
#define AUTHOR_H

#include "Reader.h"
#include <string>

struct Statistics {
    long totalViews;
    int subscriberCount;
    float averageRating;
};

class Novel;

class Author : public Reader {
private:
    long total_views;
    std::string bio;

public:
    Author(int id, const std::string& username, const std::string& email,
           const std::string& password_hash, const std::string& created_at,
           int reading_points, long total_views, const std::string& bio);
    virtual ~Author() = default;

    void createNovel(const std::string& title);
    void publishChapter(int novelId, const std::string& content);
    Statistics viewAnalytics(int novelId);

    bool isAuthor() const override;
    bool isModerator() const override;
};

#endif
