#include "Moderator.h"

Moderator::Moderator(int id, const std::string& username, const std::string& email,
                     const std::string& password_hash, const std::string& created_at, int mod_level)
    : Authenticated_user(id, username, email, password_hash, created_at),
      mod_level(mod_level) {}

void Moderator::deleteReview(int reviewId) {
}

void Moderator::shadowBanUser(int userId) {
}

void Moderator::banUser(int userId) {
}

void Moderator::moderateContent(int contentId) {
}

bool Moderator::isAuthor() const {
    return false;
}

bool Moderator::isModerator() const {
    return true;
}
