#ifndef AUTHENTICATED_USER_H
#define AUTHENTICATED_USER_H

#include <string>
#include "Enums.h"

class Authenticated_user {
protected:
    int id;
    std::string username;
    std::string email;
    std::string password_hash;
    std::string created_at;
    bool is_banned;
    bool is_shadowbanned;

public:
    Authenticated_user(int id, const std::string& username, const std::string& email,
                       const std::string& password_hash, const std::string& created_at);
    virtual ~Authenticated_user() = default;

    bool login();
    void logout();
    void updateProfile();
    bool resetPassword(const std::string& token);

    virtual bool isAuthor() const = 0;
    virtual bool isModerator() const = 0;
};

#endif
