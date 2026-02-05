#include "Authenticated_user.h"
#include <iostream>

Authenticated_user::Authenticated_user(int id, const std::string& username, const std::string& email,
                                       const std::string& password_hash, const std::string& created_at)
    : id(id), username(username), email(email), password_hash(password_hash),
      created_at(created_at), is_banned(false), is_shadowbanned(false) {}

bool Authenticated_user::login() {
    return true;
}

void Authenticated_user::logout() {
}

void Authenticated_user::updateProfile() {
}

bool Authenticated_user::resetPassword(const std::string& token) {
    return true;
}
