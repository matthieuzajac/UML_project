#ifndef GENRE_H
#define GENRE_H

#include <string>
#include <vector>

class Novel;

class Genre {
private:
    int id;
    std::string name;
    std::string description;

public:
    Genre(int id, const std::string& name, const std::string& description);
    ~Genre();

    std::vector<Novel*> getNovels();
};

#endif
