#ifndef NOVEL_H
#define NOVEL_H

#include "Enums.h"
#include <string>
#include <vector>

class Chapter;
class Genre;
class Tag;

class Novel {
private:
    int id;
    std::string title;
    std::string synopsis;
    std::string cover_image_url;
    float average_rating;
    long total_views;
    int total_chapters;
    NovelStatus status;
    std::string created_at;
    std::string updated_at;

public:
    Novel(int id, const std::string& title, const std::string& synopsis,
          const std::string& cover_image_url, float average_rating, long total_views,
          int total_chapters, NovelStatus status, const std::string& created_at,
          const std::string& updated_at);
    ~Novel();

    void updateRating();
    std::vector<Chapter*> getChapters();
    int getFollowerCount();
    void updateStatus(NovelStatus newStatus);
};

#endif
