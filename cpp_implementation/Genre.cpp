#include "Genre.h"
#include "Novel.h"

Genre::Genre(int id, const std::string& name, const std::string& description)
    : id(id), name(name), description(description) {}

Genre::~Genre() {
}

std::vector<Novel*> Genre::getNovels() {
    return std::vector<Novel*>();
}
