#include "Novel.h"
#include "Chapter.h"

Novel::Novel(int id, const std::string& title, const std::string& synopsis,
             const std::string& cover_image_url, float average_rating, long total_views,
             int total_chapters, NovelStatus status, const std::string& created_at,
             const std::string& updated_at)
    : id(id), title(title), synopsis(synopsis), cover_image_url(cover_image_url),
      average_rating(average_rating), total_views(total_views), total_chapters(total_chapters),
      status(status), created_at(created_at), updated_at(updated_at) {}

Novel::~Novel() {
}

void Novel::updateRating() {
}

std::vector<Chapter*> Novel::getChapters() {
    return std::vector<Chapter*>();
}

int Novel::getFollowerCount() {
    return 0;
}

void Novel::updateStatus(NovelStatus newStatus) {
}
