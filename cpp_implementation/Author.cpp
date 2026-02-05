#include "Author.h"
#include "Novel.h"

Author::Author(int id, const std::string& username, const std::string& email,
               const std::string& password_hash, const std::string& created_at,
               int reading_points, long total_views, const std::string& bio)
    : Reader(id, username, email, password_hash, created_at, reading_points),
      total_views(total_views), bio(bio) {}

void Author::createNovel(const std::string& title) {
}

void Author::publishChapter(int novelId, const std::string& content) {
}

Statistics Author::viewAnalytics(int novelId) {
    Statistics stats = {0, 0, 0.0f};
    return stats;
}

bool Author::isAuthor() const {
    return true;
}

bool Author::isModerator() const {
    return false;
}
