#ifndef READER_H
#define READER_H

#include "Authenticated_user.h"
#include <vector>

class Novel;
class Chapter;

class Reader : public Authenticated_user {
private:
    int reading_points;

public:
    Reader(int id, const std::string& username, const std::string& email,
           const std::string& password_hash, const std::string& created_at, int reading_points);
    virtual ~Reader() = default;

    void addBookmark(int novelId);
    void postReview(int novelId, const std::string& content, int stars);
    std::vector<Novel*> getLibrary();
    void subscribeToNovel(int novelId);

    bool isAuthor() const override;
    bool isModerator() const override;
};

#endif
