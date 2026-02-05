#include "Reader.h"
#include "Novel.h"

Reader::Reader(int id, const std::string& username, const std::string& email,
               const std::string& password_hash, const std::string& created_at, int reading_points)
    : Authenticated_user(id, username, email, password_hash, created_at),
      reading_points(reading_points) {}

void Reader::addBookmark(int novelId) {
}

void Reader::postReview(int novelId, const std::string& content, int stars) {
}

std::vector<Novel*> Reader::getLibrary() {
    return std::vector<Novel*>();
}

void Reader::subscribeToNovel(int novelId) {
}

bool Reader::isAuthor() const {
    return false;
}

bool Reader::isModerator() const {
    return false;
}
