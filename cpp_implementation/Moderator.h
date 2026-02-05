#ifndef MODERATOR_H
#define MODERATOR_H

#include "Authenticated_user.h"

class Moderator : public Authenticated_user {
private:
    int mod_level;

public:
    Moderator(int id, const std::string& username, const std::string& email,
              const std::string& password_hash, const std::string& created_at, int mod_level);
    virtual ~Moderator() = default;

    void deleteReview(int reviewId);
    void shadowBanUser(int userId);
    void banUser(int userId);
    void moderateContent(int contentId);

    bool isAuthor() const override;
    bool isModerator() const override;
};

#endif
